from openai import OpenAI
from dotenv import load_dotenv
import os
import tiktoken

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-4"

codifier = tiktoken.encoding_for_model(model)

def load_csv_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except IOError as e:
        print(f"Error reading the file: {e}")
        return None
    
sys_prompt = """
Identify the purchasing profile for each client below.

The output format should be:

client - describe the client profile in 3 words 
"""

client_prompt = load_csv_file("data/purchase_list.csv")

token_list = codifier.encode(sys_prompt + client_prompt)
number_of_tokens = len(token_list)

print(f"Total tokens: {number_of_tokens}")
expected_output_size = 2048

if number_of_tokens >= expected_output_size:
    model = "gpt-4-1106-preview"

print(f"Model selected: {model}")

response = client.chat.completions.create(
    messages=[
        {
            "role": "system", 
            "content": sys_prompt
        },
        {
            "role": "user", 
            "content": client_prompt
        },
    ],
    model=model,
)

print(response.choices[0].message.content)

"""
Output:
    Total tokens: 2447
    Model selected: gpt-4-1106-preview
    client0 - Eco-conscious, Diverse, Sustainable
    client1 - Eco-friendly, Health-oriented, Energy-saving
    client2 - Solar-focused, Recycled-fashion
    client3 - Sustainable, Organic-consumer, Eco-friendly
    client4 - Natural, Versatile, Eco-conscious
    client5 - Eco-camping, Skin-health, Reusable
    client6 - Organic-personal-care, Audio-tech
    client7 - Sustainable, Educated, Nature-focused
    client8 - Artisanal, Vegan-fashion
    client9 - Eco-lifestyle, Dental-care, Vegan-accessories
    client10 - Recycled-clothing, Solar-tech, Eco-friendly
    client11 - Low-energy, Skin-care, Tech-savvy
    client12 - Green-cleaning, Sustainable-fashion, Eco-aware
    client13 - Fair-trade, Sustainable-living, Eco-furniture
    client14 - Recycled-products, Adventure, Eco-conscious
    client15 - Organic-clothing, Eco-cleaning
    client16 - Energy-efficient, Skin-care, Tech-savvy
    client17 - Recycled-fashion, Artisanal, Eco-cleaning
    client18 - Educational, Eco-products, Illumination
    client19 - Sustainable-guides, Personal-care, Outdoor-gear
    client20 - Renewable-tech, Swimwear, Organic-clothing
    client21 - Artisanal, Fair-trade, Non-toxic
    client22 - Hygiene, Reusable, Hair-care
    client23 - Camping, Recycled-products, Organic-eater
    client24 - Educational, Eco-tech, Documentary-viewer
    client25 - Solar-tech, Outdoor-adventure
    client26 - Audio-tech, Non-toxic, Lighting
    client27 - Swimwear, Illumination
    client28 - Organic-fabric, Eco-clothing
    client29 - Green-energy, Cleaning-supplies, Lighting
    client30 - Outdoor-apparel, Eco-lighting, Climbing-equipment
    client31 - Sustainable-furniture, Eco-media, Cleaning-products
    client32 - Swimwear, Documentaries, Skin-care
    client33 - Beauty-focus, Artisanal, Recycled-products
    client34 - Lifestyle-guides, Health-snacks, Solar-energy
    client35 - Eco-camping, Recycled-swimwear
    client36 - Healthy-eating, Renewable-lighting, Tech-users
    client37 - Efficiency-guide, Documentary-viewer, Tech-consumer
    client38 - Kitchenware, Hair-care, Hygiene
    client39 - Eco-cleaning, Non-toxic, Dental-care
    client40 - Organic-eater, Hair-care
    client41 - Hair-care, Dental-hygiene
    client42 - Green-cleaning, Outdoor-apparel, Mindful-consumer
    client43 - Beauty, Eco-fashion, Daylight-bulbs
    client44 - Vegan-accessories, Camping, Sustainable-apparel
    client45 - Renewable-energy, Durable-gear, Camping-enthusiast
    client46 - Organic-produce, Hair-care, Eco-conscious
    client47 - Recycled-denim, Eco-tech, Soap-maker
    client48 - Eco-furnishings, Eco-calendar, Low-energy-lighting
    client49 - Education-focus, Documentaries, Farm-produce
    client50 - LED-lighting, Recycled-swimwear, Eco-guides
    client51 - Books, Tents, Lanterns
    client52 - Mobile-charging, Stainless-steel
    client53 - Sustainable, Diverse, Eco-friendly
    client54 - Non-toxic, Acoustic, Clean-tech
    client55 - Reusable, Camping-essentials
    client56 - Vegan-fashion, Solar-tech, Hydration
    client57 - Recycled-backpacks, Swimwear, Climbing
    client58 - Fair-trade, Eco-clothing
    client59 - Portable-lighting, Outdoor-gear, Health-snacks
    client60 - Locally-sourced, Denim, Eco-calendars
    client61 - Organic-beauty, Comfort-wear, Health-snacks
    client62 - Natural-soap, Dining-ware, Cleaning-agent
    client63 - Local-products, Audio, Garment
    client64 - Organic-foods, Hygiene, Vegetarian
    client65 - Solar-home, Water-bottles
    client66 - Organic-produce, Recycled-fashion, Solar-power
    client67 - Vegan-bags, Educational, Eco-friendly
    client68 - Non-toxic, Natural-products, Organic-clothing
    client69 - Tech-savvy, Safe-cookware
    client70 - Healthy-eating, Charging-devices, Kitchenware
    client71 - Solar-tech, Swimwear
    client72 - Non-toxic, Dental-hygiene, Solar-power
    client73 - Solar-tech, Organic-produce, Eco-calendars
    client74 - Sustainable-media, Hydration
    client75 - Eco-furnishing, Sustainable-wear
    client76 - Non-toxic, Eco-living
    client77 - Illumination, Conservation, Non-toxic
    client78 - Camping-supplies, Artisanal-soaps
    client79 - Organic-produce, Hair-care
    client80 - Swimwear, Denim, Craftsmanship
    client81 - Office-products, Outdoor-gear
    client82 - Electric-power, Organic-fabric
    client83 - Reusable, Non-toxic
    client84 - Reading, Sustainability, Farm-products
    client85 - Tech-user, Craftsmanship
    client86 - Lighting, Solar-technology
    client87 - Kitchenware, Organic-consumer, Hair-care
    client88 - Audio-enthusiast, Non-toxic, Nutritious-snacks
    client89 - Oral-care, Health-foods
    cliente90 - Eco-fashion, Solar-lighting
    cliente91 - Climbing-gear, Eco-reading, Audio-tech
    cliente92 - Swimwear, Hair-care, Outdoor-living
    cliente93 - Camping, Grooming-tools
    cliente94 - Organic-foods, Cleaning-products, Protective-gear
    cliente95 - Solar-energy, Dining-ware, Backpacks
    cliente96 - Lighting, Backpacks, Solar-equipment
    cliente97 - Personal-care, Bamboo-products, Illumination
    cliente98 - Reading-materials, Swimwear, Grooming
    cliente99 - Camping-gear, Beauty, Sustainable-fashion
"""
