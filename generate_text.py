#Author: spasemax0
#calls the OpenAI api and chooses specifications
import openai
import os

openai.api_key = "INSERT API KEY HERE"


def generate_text(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = response.choices[0].text.strip()
    return message
