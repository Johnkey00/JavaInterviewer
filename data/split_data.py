import json
import random

def sample_jsonl(input_path, test_output, train_output, test_size=50):
    # 1. 读入全部 JSONL 数据
    data = []
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))

    print(f"总数据量: {len(data)}")

    # 2. 随机抽取 test_size 条
    test_data = random.sample(data, test_size)

    # 3. 剩下的就是训练集
    train_data = [item for item in data if item not in test_data]

    # 4. 写入 test.jsonl
    with open(test_output, "w", encoding="utf-8") as f:
        for item in test_data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    # 5. 写入 train.jsonl
    with open(train_output, "w", encoding="utf-8") as f:
        for item in train_data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"测试集: {len(test_data)} 条 → {test_output}")
    print(f"训练集: {len(train_data)} 条 → {train_output}")


if __name__ == "__main__":
    input_file = "java_interview_shuffled.jsonl"                # 578 条总数据
    test_file = "java_interview_test.jsonl"             # 抽出的测试集
    train_file = "java_interview_train.jsonl"         # 剩余训练数据
    sample_jsonl(input_file, test_file, train_file)
