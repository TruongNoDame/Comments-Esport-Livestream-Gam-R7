from dotenv import load_dotenv, dotenv_values
import openai
import time
import pandas as pd

load_dotenv()
config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

file_writer = open("chatgpt_results.txt.txt", "a", encoding="utf-8")


INDEX = 1

# Chia nhóm câu thành các nhóm nhỏ
def chunk_list(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

# Hàm gửi yêu cầu API cho một nhóm câu
def process_group(group):
    global INDEX
    resilts = []

    prompt = "bình luận toxic hoặc không toxic. Gán nhãn cho từng bình luận sau (trả lời ngắn gọn cho từng câu):\n"

    for sentence in group:
      prompt += f'{INDEX}. "{sentence}"\n'
      INDEX += 1
    print(prompt)

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": prompt }
      ],
      temperature=0.7,
      max_tokens=2000
    )

    result = response.choices[0].message.content
    print("---------------------------result:")
    print(result)
    results = result.split("\n")

    # print(response.usage)
    return results

df = pd.read_excel('DataCrawl.xlsx')
sentences = df['Content'].to_list()

chunk_size = 50  # Kích thước mỗi nhóm
sentences_groups = list(chunk_list(sentences, chunk_size))

total = []

for i, group in enumerate(sentences_groups):
    log_1 = f"----------------------------group: {i}"
    print(log_1)
    file_writer.write(f"{log_1}\n")

    log_4 = f"----------------num sentences to request: {len(group)}"
    print(log_4)
    file_writer.write(f"{log_4}\n")

    results = process_group(group)
    total += results
    for result in results:
      file_writer.write(f"{result}\n")

    log_2 = f"------------------current len of total results: {len(total)}"
    print(log_2)
    file_writer.write(f"{log_2}\n")

    log_3 = "----------------------------------------------------------"
    print(log_3)
    file_writer.write(f"{log_3}\n")

    time.sleep(20)

# print(results)
