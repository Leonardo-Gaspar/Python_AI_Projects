from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(os.getenv('OPENAI_API_KEY'))

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "List only the products names, without descriptions"
        },
        {
            "role": "user",
            "content": "List 3 sustainable products"
        }
        
    ],
    model="gpt-3.5"
)

print(response.choises[0].message.content)