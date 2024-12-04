from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(os.getenv('OPENAI_API_KEY'))

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": """
            Classify the product below in one of the following categories: 
            Personal, Home, Fashion, Hygiene and give a short description of the category.
            """
        },
        {
            "role": "user",
            "content": """
            Bamboo toothbrush 
            """
        }
        
    ],
    model="gpt-3.5",
    temperature=0.5,
    max_tokens=200,
    n=3
)

for counter in range(0,3):
    print(response.choises[counter].message.content)
    