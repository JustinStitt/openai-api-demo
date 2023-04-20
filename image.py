import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("API_KEY")

EXTRA = " wearing a pirate hat"


def generate_image_url(description: str) -> bytes:
    description = description + EXTRA
    response = openai.Image.create(prompt=description, n=1, size="512x512")
    image_url = response["data"][0]["url"]  # type: ignore
    return image_url


while True:
    user_input = input("Describe an image:\n> ")
    image_url = generate_image_url(user_input)
    print("Your Image: ", image_url)
