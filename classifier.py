import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_product(product, categories):
    prompt = f"""
        Classify the product '{product}' into one of the following categories: {categories}.

        Follow this response example:
            Category: Hygiene
            Description: Hygiene products are items used for personal care and cleanliness. This category includes products such as toothpaste, soap, shampoo, and personal grooming items. Hygiene products are essential for maintaining good health and personal well-being.
    """

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system", 
                "content": prompt
            },
            {
                "role": "user", 
                "content": product
            },
        ],
        model="gpt-3.5-turbo-1106",
        temperature=1, # Controls the randomness of the response. Lower values make the model more deterministic
        max_tokens=100, # Maximum number of tokens to generate
        n=3 # Number of responses to generate
    )

    for choice in response.choices:
        print(choice.message.content)
        print("\n")


categories = input("Enter the categories separated by a comma: ")
product = input("Enter the product: ")

classify_product(product, categories)

"""
EXAMPLE:

    Input: 
        hygiene, food, electronics, clothing, household
        Toothpaste made of bamboo.

    Output:

        Category: Hygiene
        Description: Hygiene products are items used for personal care and cleanliness. This category includes products such as toothpaste, soap, shampoo, and personal grooming items. Hygiene products are essential for maintaining good health and personal well-being.


        Category: Hygiene
        Description: Hygiene products are designed to promote cleanliness and personal care. They include items such as toothpaste, soap, shampoo, and deodorant. Hygiene products are essential for maintaining personal cleanliness and overall health.


        Category: Hygiene
        Description: This category includes products related to personal care and cleanliness, such as dental hygiene products, soaps, shampoos, and skincare items. These products are essential for maintaining cleanliness and overall health.
"""