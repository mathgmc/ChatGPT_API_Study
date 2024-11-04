# ChatGPT API Study

Repository dedicated to study OpenAI API integrations. This repository is made of many small scripts using ChatGPT API in Python.

## Set Up

1. Add an env `OPENAI_API_KEY` that contains your openAI token.
2. Install requirements: `pip install -r requirements.txt`
3. Run the scrips: `python <script_file_name>`

## Scripts

### List Countries

**Script Path:** `/list_countries.py`

**Descriptions:** Script that uses the OpenAI API to list countries from a selected continent in alphabetical order.

### Product Classifier

**Script Path:** `/product_classifier.py`

**Descriptions:** Script that classifies some product in one of the predefined categories and describe the category, generating 3 responses. On this code we play with a dynamic prompt and some OpenAI parameters like `temperature`, `max_tokens` and `n`. 

### Count Tokens and Cost

**Script Path:** `/count_tokens.py`

**Descriptions:** Script that uses `tiktokens` lib to count tokens used and calculate how much this token costs on two different models.

### Client Classifier Script

**Script Path:** `/client_classifier.py`

**Descriptions:** Script to classify the purchasing profile for each client in a csv file with a list of client's purchases. On this script we will use a dynamic model selection based on the number of tokens to be processed. If the number of tokens is greater than `2048`, we will use the model `gpt-4-1106-preview`, otherwise we will use the model `gpt-4`.

### Sentiment Analyzer Script 

**Script Path:** `/sentiment_analyzer.py`

**Descriptions:** Script that uses the OpenAI API to classify the sentiment of product reviews. The script reads the product reviews from a file, then uses the OpenAI API to classify the overall sentiment of the reviews as positive, negative, or neutral. It also identifies 3 positive and 3 negative aspects of the product based on the reviews. On this script we are using for the first time the OpenAI Exception handling. You can check the output examples of this script at `output/sentiment_{product}.txt`.