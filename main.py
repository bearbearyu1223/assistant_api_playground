import os
import time
import logging
from datetime import datetime 
from pathlib import Path
import openai
from openai import OpenAI
from dotenv import load_dotenv
import pygame
import urllib.request 
from PIL import Image 

load_dotenv()
logging.basicConfig(level=logging.INFO)

def play_mp3(path):
    """
    Play a mp3 file 
    :param path: path to the mp3 file
    """
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load(path)

    # Play the MP3 file
    pygame.mixer.music.play()

    # Wait for the music to play
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def wait_for_run_completion(client, thread_id, run_id, sleep_interval=5):
    """
    Waits for a run to complete and prints the elapsed time.
    :param client: The OpenAI client object.
    :param thread_id: The ID of the thread.
    :param run_id: The ID of the run.
    :param sleep_interval: Time in seconds to wait between checks.
    """
    while True:
        try:
            run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
            if run.completed_at:
                elapsed_time = run.completed_at - run.created_at
                formatted_elapsed_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
                logging.info(f"Run completed in {formatted_elapsed_time}")
                break
        except Exception as e:
            logging.error(f"An error occurred while retrieving the run: {e}")
            break
        logging.info("Waiting for run to complete...")
        time.sleep(sleep_interval)

if __name__=="__main__": 
    client = OpenAI()
    file_ids=[]
    for file in os.listdir("./cookbook/"):
        filepath = "./cookbook/"+file
        file_object = client.files.create(
            file = open(filepath, 'rb'), 
            purpose='assistants', 
        )
        file_ids.append(file_object.id)

    assistant = client.beta.assistants.create(
        name="cooking assistant", 
        instructions="You are a cooking assistant. Your role is to guide users through recipes,\
                      offer cooking tips, and provide ingredient substitutions.\
                      You can answer culinary questions in real-time, help plan meals based on\
                      dietary preferences or restrictions,\
                      and create grocery shopping lists based off recipes.",
        tools=[{"type": "retrieval"}, {"type": "code_interpreter"}], 
        model="gpt-4-1106-preview", 
        file_ids=file_ids,           
    )
    
    thread = client.beta.threads.create()
    i = 0
    recipe_info=[]
    while True:
        try:
            message = input('Enter a query related to food preparation and cooking: ')
            message = client.beta.threads.messages.create(
                thread_id=thread.id, role="user", content=message)
            
            instructions="""
            Address the user as 'Han' in all communications. Respond to Han's queries exclusively using information from the cookbooks she has provided. 
            In cases where Han specifically requests a visual representation of a recipe, 
            reply with: 'Absolutely! Prepare for a delightful visual preview of the recipe, coming up shortly. Please hold on!'
            When providing a recipe in response to Han's question, always begin your response with: 'Here's a recipe I found!' 
            Then, concisely summarize the recipe using a few bullet points, ensuring the summary is no longer than 150 words. 
            If you're unable to find a suitable recipe or answer Han's question, politely conclude the conversation.
            """

            run = client.beta.threads.runs.create(
                thread_id = thread.id,
                assistant_id = assistant.id,
                instructions = instructions
            )

            wait_for_run_completion(client, thread.id, run.id)

            messages = client.beta.threads.messages.list(
                thread_id=thread.id
            )
            last_message = messages.data[0]
            text_response = last_message.content[0].text.value
            print(text_response)

            if "Here is a recipe that I found!" in text_response:
                recipe_info.append(text_response)

            if "a delightful visual preview of the recipe" in text_response:
                for i in len(recipe_info):
                    prompt =f"Help me generate a visual representation of the food described in this recipe: '{recipe_info[i]}'."
                    image_gen = client.images.generate(
                        model="dall-e-3",
                        prompt=prompt,
                        size="1024x1024",
                        quality="standard",
                        n=1,
                    )
                    image_url = image_gen.data[0].url
                    image_name = "image"+"_"+str(i)+"_"+".png"
                    urllib.request.urlretrieve(image_url, image_name) 
                    img = Image.open(image_name) 
                    img.show()

            speech_file_name = "tts_response_" + str(i)+".mp3"
            i = i + 1

            speech_file_path = Path(__file__).parent / speech_file_name
            print()
            print("wait for tts to complete ...")
            audio_response = client.audio.speech.create(
                model="tts-1",
                voice="alloy",
                input=text_response,
            )
            audio_response.stream_to_file(speech_file_path)
            print()
            print("start tts playback ...")
            play_mp3(speech_file_name)

        except KeyboardInterrupt:  # Ctrl + C - will exit program immediately if not caught
            break
        print()
        print("Program Exit")


