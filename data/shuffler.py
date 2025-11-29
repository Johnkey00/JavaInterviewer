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


# 示例
if __name__ == "__main__":
    input_file = "java_interview.jsonl"
    output_file = "java_interview_shuffled.jsonl"

    shuffle_jsonl(input_file, output_file)