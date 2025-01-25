import subprocess
import re

# 定义安全级别和类别
levels = {
    "TS": 4,
    "S": 3,
    "C": 2,
    "UC": 1
}

categories = {
    "NUC": 1,
    "NATO": 2,
    "ACE": 3,
    "UFO": 4
}

# 启动挑战进程
process = subprocess.Popen(
    "/challenge/run",
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    encoding="utf-8"
)

question_count = 0  # 追踪问题数量
max_questions = 20  # 题目总数

with open("answers.txt", "w") as f:
    while question_count < max_questions:
        line = process.stdout.readline().strip()
        if not line.startswith("Q "):  # 过滤掉非问题行
            continue

    # 解析问题
    match = re.match(
        r"Q (\d+). Can a Subject with level ([A-Z]+) and categories \{([A-Z, ]*)\} (read|write) an Object with level ([A-Z]+) and categories \{([A-Z, ]*)\}\?",
        line.strip()
    )

    if not match:
        print("Error parsing question:", line)
        continue

    question, subj_level, subj_cats, operation, obj_level, obj_cats = match.groups()

    # 处理类别字符串
    subject_categories = set(subj_cats.split(", ")) if subj_cats else set()
    object_categories = set(obj_cats.split(", ")) if obj_cats else set()

    # 获取安全级别
    subject_security_level = levels[subj_level]
    object_security_level = levels[obj_level]

    # 访问控制规则
    if operation == "read":
        allowed = subject_security_level >= object_security_level and object_categories.issubset(subject_categories)
    elif operation == "write":
        allowed = subject_security_level <= object_security_level and subject_categories.issubset(object_categories)
    else:
        allowed = False

    # 发送答案
    answer = "yes" if allowed else "no"
    process.stdin.write(answer + "\n")
    process.stdin.flush()

    print(f"Processing：{line} -> {answer}")
    question_count += 1  # 增加问题计数


# 确保所有问题已完成，发送退出信号
process.stdin.close()
process.wait()

print("All questions answered. Exiting.")
