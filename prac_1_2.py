import os
from dotenv import load_dotenv
from openai import OpenAI

# 환경 변수 로드
load_dotenv()


# 요약을 위한 프롬프트
prompt="""
Describe the floowing movie using emojis.

{movie}: """

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

#퓨샷 예시
examples=[
    {"input": "Titanic", "output": "🚢🌊💑🎵🎶🔥📚💔😢😭"},
    {"input": "The Matrix", "output": "😎🕶️💥🤖😵🔌📱🔄🔐💊"}
]

movie = "Toy Story"
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt.format(movie=examples[0]["input"])},
        {"role": "assistant", "content": examples[0]["output"]},
        {"role": "user", "content": prompt.format(movie=examples[1]["input"])},
        {"role": "assistant", "content": examples[1]["output"]},
        {"role": "user", "content": prompt.format(movie=movie)},
    ]
)

print(response.choices[0].message.content)