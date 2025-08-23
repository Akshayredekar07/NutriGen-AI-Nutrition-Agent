import chainlit as cl
import requests

API_URL = "http://localhost:8000/chat/"

@cl.on_message
async def main(message: str):
    response = requests.post(API_URL, params={"query": message})
    await cl.Message(content=response.json()["response"]).send()
