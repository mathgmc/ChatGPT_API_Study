# ChatGPT API Study

Repository dedicated to study how to use ChatGPT API. This repository is made of small functionalities using ChatGPT API in Python.

## Set Up

1. Add an env `OPENAI_API_KEY` that contains your openAI token.
2. Install requirements: `pip install -r requirements.txt`
3. Run the scrips: `python <script_file_name>`

## Scripts

### list_countries.py

Script that list countries from a selected continent.

### classifier.py

Script that classifies some product in one of the predefined categories and describe the category, generating 3 responses. On this code we play with a dynamic prompt and some OpenAI parameters like temperature, max_tokens and n. 

### count_tokens.py

Script that uses tiktokens lib to count tokens used and calculate how much this token costs on two different models.

### client_classifier.py

Script to classify the purchasing profile for each client in a csv file with a list of client's purchases. On this script we will use a dynamic model selection based on the number of tokens to be processed. If the number of tokens is greater than 2048, we will use the model "gpt-4-1106-preview", otherwise we will use the model "gpt-4".
