import os
import time
import logging
from datetime import datetime 
from pathlib import Path
import openai
from openai import OpenAI
from openai import OpenAI
from dotenv import load_dotenv
import pygame

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
        tools=[{"type": "retrieval"}], 
        model="gpt-4-1106-preview", 
        file_ids=file_ids,           
    )

    thread = client.beta.threads.create()
    message = "Give me some ideas to make beef dish with Lantin American flavors with detailed steps, also if there are sides dessert, or salards that can pair with it nicely, find the recipe information and summarize how to make them as well."

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=message
    )

    run = client.beta.threads.runs.create(
        thread_id = thread.id,
        assistant_id = assistant.id,
        instructions = "Please address the user as Han, and only generate response using the cookbooks she shared with you. If you cannot help answer the questions, just politely end the conversation."
    )

    wait_for_run_completion(client, thread.id, run.id)

    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    last_message = messages.data[0]
    response = last_message.content[0].text.value
    print(response)

    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=response,
    )

    response.stream_to_file(speech_file_path)
    play_mp3("speech.mp3")





    




    


