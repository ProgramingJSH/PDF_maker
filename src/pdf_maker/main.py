# src/pdf_maker/main.py

import json
import weasyprint
from jinja2 import Template
from pdf_maker.config import INPUT_FILE, TEMPLATE_FILE, OUTPUT
from pdf_maker.gems import get_data_by_API

def main():
    try: 
        # 텍스트 파일에서 가사 데이터 읽어오기
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            input_text = f.read()

        # API로 데이터 생성 후 저장
        data = get_data_by_API(input_text)

        # Jinja2 HTML 템플릿을 불러오기
        with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
            template_str = f.read()

        # 데이터 주입 
        template = Template(template_str)
        html_content = template.render(data)

        # PDF 생성
        OUTPUT.mkdir(exist_ok=True)
        output_name = OUTPUT / f"{data['study_no']}. {data['title']}.pdf"
        weasyprint.HTML(string=html_content).write_pdf(output_name)

        print(f"{data["title"]} pdf 출력을 완료했습니다")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    main()