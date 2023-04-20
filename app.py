import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("API_KEY")

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
]


def send_message_to_ai(my_message: str) -> str:
    user_message = {"role": "user", "content": my_message}
    messages.append(user_message)

    api_response: dict = openai.ChatCompletion.create(  # type: ignore
        model="gpt-3.5-turbo",
        messages=messages,
    )

    message = api_response["choices"][0]["message"]
    messages.append(message)

    return message["content"]  # user only cares about content


print(send_message_to_ai("Who won the 2016 NBA Finals?"))
