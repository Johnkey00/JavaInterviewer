import json
import random

def shuffle_jsonl(input_path, output_path):
    # 1. 读取全部数据行
    data = []
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():  # 过滤空行
                data.append(json.loads(line))

    print(f"Loaded {len(data)} records.")

    # 2. 随机打乱
    random.shuffle(data)
    print("Shuffled the dataset.")

    # 3. 写入新的 jsonl 文件
    with open(output_path, "w", encoding="utf-8") as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"Saved shuffled dataset to {output_path}")

def shuffle_txt(input_path, output_path):
    # 1. 读取全部行
    with open(input_path, "r", encoding="utf-8") as f:
        lines = [line for line in f if line.strip()]   # 保留非空行

    print(f"Loaded {len(lines)} lines.")

    # 2. 打乱顺序
    random.shuffle(lines)
    print("Shuffled the lines.")

    # 3. 写入新的 txt 文件
    with open(output_path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line.rstrip("\n") + "\n")  # 确保格式干净

    print(f"Saved shuffled txt to {output_path}")

# 示例
if __name__ == "__main__":
    input_file = "java_interview_shuffled.jsonl"
    output_file = "java_interview_shuffled_new.jsonl"

    shuffle_jsonl(input_file, output_file)
    # input_file = "test_questions.txt"
    # output_file = "test_questions_shuffled.txt"
    # shuffle_txt(input_file, output_file)