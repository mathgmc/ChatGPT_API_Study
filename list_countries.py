import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

selected_continent = None
continents = {
    "1": "Africa",
    "2": "America",
    "3": "Asia",
    "4": "Europe",
    "5": "Oceania"
}

selected_continent = input("""
Possible continents:
    1. Africa
    2. America
    3. Asia
    4. Europe
    5. Oceania
Select the number of the continent:""")
while selected_continent not in continents:
    selected_continent = input("Invalid option. Select the number of the continent as shown above:")

response = client.chat.completions.create(
    messages=[
        {
            "role": "system", 
            "content": "Answer the question always in alphabetical order, writing only the name of the countries, on the same line separated by a comma and thanking the user at the end in a separated line."
        },
        {
            "role": "user", 
            "content": f"List all the countries in the {continents[selected_continent]} continent"
        },
    ],
    model="gpt-3.5-turbo-1106",
)

print(response.choices[0].message.content)

"""
Input:
    Select the number of the continent: 2

Output: 

    Argentina, Belize, Bolivia, Brazil, Canada, Chile, Colombia, Costa Rica, Cuba, Dominica, Dominican Republic, Ecuador, El Salvador, Grenada, Guatemala, Guyana, Haiti, Honduras, Jamaica, Mexico, Nicaragua, Panama, Paraguay, Peru, Saint Kitts and Nevis, Saint Lucia, Saint Vincent and the Grenadines, Suriname, Trinidad and Tobago, United States of America, Uruguay, Venezuela.
    Thank you.

"""