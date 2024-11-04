from openai import OpenAI
from dotenv import load_dotenv
import openai
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-4"

def load_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except IOError as e:
        print(f"Error reading the file: {e}")
        return None
    
def write_file(file_path, content):
    try:
        with open(file_path, "w") as file:
            file.write(content)
    except IOError as e:
        print(f"Error writing the file: {e}")
        return None
    
def classify_sentiment(product):
    sys_prompt = """
        You are a sentiment analyzer of products reviews.
        Write a paragraph with 50 words maximum resuming the sentiment
        of the product reviews and then classify the overall sentiment of
        the product as positive or negative or neutral.Identify as well 3 
        positive and 3 negative aspects of the product though the reviews.

        The output format should be:

        Product name: product name
        Reviews resume: paragraph with 50 words maximum
        Overall sentiment: positive/negative/neutral
        Positive aspects: bullet list of 3 positive aspects
        Negative aspects: bullet list of 3 negative aspects
    """

    user_prompt = load_file(f"data/review_{product}.txt")
    print(f"Starting sentiment analysis for product {product}")

    messages_list = [
        {
            "role": "system", 
            "content": sys_prompt
        },
        {
            "role": "user", 
            "content": user_prompt
        },
    ]

    response = client.chat.completions.create(
        messages=messages_list,
        model=model,
    )

    try:
        response_content = response.choices[0].message.content
        write_file(f"output/sentiment_{product}.txt", response_content)
        print(f"Sentiment analysis for product {product} completed")
    except openai.AuthenticationError as e:
        print(f"Error OpenAI authentication: {e}")
    except openai.APIError as e:
        print(f"Error OpenAI API: {e}")


classify_sentiment("mineral_makeup")
classify_sentiment("organic_cotton_tshirt")
classify_sentiment("recycled_jeans")