import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("API_KEY")

api_response: dict = openai.ChatCompletion.create(  # type: ignore
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Who won the world series in 2020?"},
    ],
)

message = api_response["choices"][0]["message"]["content"]

print(message)
