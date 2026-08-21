# src/pdf_maker/gems.py

import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv

# 클라이언트 초기화
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_data_by_API(input_text):
    system_instruction = """
    1. 사용자는 글귀의 {title}(제목), "제 {study_no} 회", 그리고 8개 내외의 일본어 가사, 독음, 번역의 뭉치를 제공함.

    2. 이를 가공해 다음과 같은 구조의 json 형식으로 응답해야 함.
    ---
    {
        "title": "수평선",
        "study_no": 1,
        "lyrics": [
            {
                "jp": "水平線が光る朝に",
                "pron": "스이헤이센가 히카루 아사니",
                "kr": "수평선이 빛나는 아침에"
            },
            {
                "jp": "あなたの希望が崩れ落ちて",
                "pron": "아나타노 키보-가 쿠즈레 오치테",
                "kr": "당신의 희망이 무너져 내려버려서"
            }
        ],
        "vocabs": [
            {
                "term": "水平線 (すいへいせん)",
                "def": "수평선"
            },
            {
                "term": "光る (ひかる)",
                "def": "빛나다"
            },
            {
                "term": "朝 (あさ)",
                "def": "아침"
            }
        ]
    }
    ---

    3. vocabs의 경우 해당 가사의 주요 단어 12개를 정리해 제공함.
    """

    print("데이터를 요청하는 중...")

    response = client.models.generate_content(
        model='gemini-3.6-flash',  
        contents=input_text,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            response_mime_type="application/json",
        )
    )

    # 응답받은 텍스트(JSON 문자열)를 파이썬 딕셔너리로 변환해 리턴
    return json.loads(response.text)
