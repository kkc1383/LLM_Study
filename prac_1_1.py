import os
from dotenv import load_dotenv
from openai import OpenAI

# 환경 변수 로드
load_dotenv()

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

english_text = "Hello, How are you?"

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": english_text},
    ],
)
print(response.choices[0].message.content)