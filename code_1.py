import subprocess
import re

# 定义安全级别
levels = {
    "TS": 4,  # 最高安全级别
    "S": 3,
    "C": 2,
    "UC": 1  # 最低安全级别
}

# 启动挑战进程
process = subprocess.Popen(
    "/challenge/run",
    stdin=subprocess.PIPE,  # 允许向进程写入答案
    stdout=subprocess.PIPE,  # 读取进程输出
    stderr=subprocess.PIPE,  # 捕获错误
    encoding="utf-8",
    bufsize=1  # 立即处理 I/O，减少延迟
)

# 解析并回答问题
question_count = 0
max_questions = 20

# 正则表达式解析问题
question_pattern = re.compile(
    r"Q \d+\. Can a Subject with level ([A-Z]+) and categories \{(.*?)\} (read|write) an Object with level ([A-Z]+) and categories \{(.*?)\}\?"
)


while question_count < max_questions:
    line = process.stdout.readline().strip()
    
    if not line:
        continue  # 避免空行导致错误

    if line.startswith("Q "):  # 只处理问题行
        print(f"Processing: {line}")

        match = question_pattern.match(line)
        if not match:
            print("Error parsing question:", line)
            continue

        subj_level, subj_cats, operation, obj_level, obj_cats = match.groups()

        # 解析类别
        subj_categories = set(subj_cats.split(", ")) if subj_cats else set()
        obj_categories = set(obj_cats.split(", ")) if obj_cats else set()

        # 获取安全级别
        subj_level_value = levels[subj_level]
        obj_level_value = levels[obj_level]

        # 访问控制规则
        if operation == "read":
            allowed = subj_level_value >= obj_level_value and obj_categories.issubset(subj_categories)
        elif operation == "write":
            allowed = subj_level_value <= obj_level_value and subj_categories.issubset(obj_categories)
        else:
            allowed = False

        # 发送答案到 /challenge/run
        answer = "yes" if allowed else "no"
        process.stdin.write(answer + "\n")
        process.stdin.flush()

        # 打印答案
        print(f"Answering: {answer}")

        question_count += 1

# 关闭输入流并等待挑战完成
process.stdin.close()
process.wait()

# 读取最终输出（如果有 flag）
final_output = process.stdout.read()
print(final_output)

print("All questions answered. Exiting.")
