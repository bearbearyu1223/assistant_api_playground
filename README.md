# Craft Your Own Kitchen Companion: Leveraging OpenAI Assistant, Image Generation, and Text-to-Speech for a Revolutionary Cooking Experience 
 <img src="assets/cropped_image.png"  width="80%" height="20%">  

## TL;DR
 OpenAI unveiled its [Assistant API](https://platform.openai.com/docs/assistants/overview) during its very first developer conference-[OpenAI DevDay](https://devday.openai.com/). This marked a significant addition to the suite of tools and models available for building conversational AI, a domain in which I've been actively engaged. 
 
 Although I have used other frameworks, tools and models to build customized Assistant in the past (check out my previous posts  [Food QnA Chatbot : Help Answer Food Related Questions from Your Own Cookbook](https://bearbearyu1223.github.io/chatbot/2023/07/31/food-qna-on-server-llm.html) and [Build On-Device QnA with LangChain and Llama2](https://bearbearyu1223.github.io/chatbot/2023/08/14/food-qna-on-device-llm.html)), intrigued by the new capabilities of the Assistant API, I decided to integrate it into a new project. This sample project is a refreshed demonstration of a simple Cooking Assistant, leveraging not only the Assistant API but also incorporating additional functionalities such as [Text-to-Speech](https://platform.openai.com/docs/guides/text-to-speech) and [Image Generation](https://platform.openai.com/docs/guides/images?context=node), showcasing a holistic approach to building conversational AI systems with only a few lines of code. 
 
Get inspired by the latest from Open AI DevDay with my project on [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/bearbearyu1223/assistant_api_playground)? Ready to unleash your creativity? Start building your own generative AI-powered experience today, join the forefront of AI innovation, and let us make AI for everyone! 

## Set Up the Dev Enviroment 
* Step 1: Git clone the sample project from [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/bearbearyu1223/assistant_api_playground). 
* Step 2: Create a venv
```
python3 -m venv cooking_assistant
```
* Step 3: Under the project root, active the venv you have just created,
```
source cooking_assistant/bin/activate
```
* Step 4: Installed the required libaries in the venv 
```
pip3 install -r requirements.txt
```
* Step 5: create an `.env` file under your project root and add your Open AI API Key as following: 
```
OPENAI_API_KEY=<Your API KEY>
```

## Run the Application 
You can play with the project in an interactive mode by entering a query related to food preparation and cooking via:
```
python main.py
```
and simply press `Ctrl + C` to exit the program. See a sample converstation created from this application below. 
| Turn ID | User Query | Assistant Response | TTS Playback |
|---------|------------|--------------------|--------------|
| 0       | 👩🏻‍🍳: Hi there, Thanksgiving is coming! I would like to have some ideas for cooking! | 🔮: Thanksgiving is a great occasion to prepare a feast. Here are some main dish ideas inspired by the contents of the "Deliciously Healthy Dinners" cookbook that could suit a Thanksgiving dinner: [Main dishes listed] | <video src="https://github.com/bearbearyu1223/assistant_api_playground/assets/7468124/06aaa9e8-9833-48a9-950e-95b8f9494c90" controls="control"></video> |
| 1       | 👩🏻‍🍳: How to make Cornbread-Crusted Turkey? | 🔮: Here's a recipe I found for Cornbread-Crusted Turkey from your cookbook: [Recipe details] | <video src="https://github.com/bearbearyu1223/assistant_api_playground/assets/7468124/cb672f77-e66d-46cd-bcff-7a8abb1a834c" controls="control"></video> |
| 2       | 👩🏻‍🍳: Thanks, what kind of salad will pair nicely with it? | 🔮: An Autumn Salad would pair nicely with Cornbread-Crusted Turkey. Here's the recipe from your cookbook: [Recipe details] | <video src="https://github.com/bearbearyu1223/assistant_api_playground/assets/7468124/cc4b66e0-b158-419e-bd5d-98946fe21404" controls="control"></video> |
| 3       | 👩🏻‍🍳: Can I see a visual of the autumn salad with the cornbread crusted turkey? | 🔮: Absolutely! Prepare for a delightful visual preview of the recipe, coming up shortly. Please hold on! | <video src="https://github.com/bearbearyu1223/assistant_api_playground/assets/7468124/1f1765bc-206f-4eed-afa6-d860965ad25c" controls="control"></video> |
|         |            | ![recipe_image](assets/recipe_image.png) |              |
| 4       | 👩🏻‍🍳: Oh that is very nice. How many calories per serving, including the autumn salad and the cornbread crusted turkey? | 🔮: The combined total calories per serving for the Autumn Salad and the Cornbread-Crusted Turkey is 395 calories. | <video src="https://github.com/bearbearyu1223/assistant_api_playground/assets/7468124/b87b3eea-786b-4557-b216-66d3acc42d9e" controls="control"></video> |
| 5       | 👩🏻‍🍳: Can you give me a breakdown of how the total calories per serving is calculated? | 🔮: Certainly! Here's the breakdown of how the total calories per serving is calculated for the combination of Autumn Salad and Cornbread-Crusted Turkey: [Calorie breakdown] | <video src="https://github.com/bearbearyu1223/assistant_api_playground/assets/7468124/03bad1bd-e575-4ba2-8958-460298c24993" controls="control"></video> |
| 6       | 👩🏻‍🍳: Nice. Can you help me create a grocery list for making the autumn salad and the cornbread crusted turkey? | 🔮: Absolutely, here's your grocery list for making the Autumn Salad and the Cornbread-Crusted Turkey: [Grocery list details] | <video src="https://github.com/bearbearyu1223/assistant_api_playground/assets/7468124/9b6b07a1-4fc0-4608-9cdb-150b87a0f387" controls="control"></video> |
| 7       | 👩🏻‍🍳: Thank you! Happy Thanksgiving! | 🔮: You're welcome! If you need any more help in the future, feel free to reach out. Have a wonderful Thanksgiving and enjoy your delicious meal! | <video src="https://github.com/bearbearyu1223/assistant_api_playground/assets/7468124/ed240241-2220-4d36-9516-60b5104e1db1" controls="control"></video> |




