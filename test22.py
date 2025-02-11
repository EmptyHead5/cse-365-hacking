import re
import subprocess

levels = {
    "TS": 4,  # 最高安全级别
    "S": 3,
    "C": 2,
    "UC": 1  # 最低安全级别
}

process = subprocess.Popen(
    "/challenge/run",
    stdin=subprocess.PIPE,  # 允许向进程写入答案
    stdout=subprocess.PIPE,  # 读取进程输出
    stderr=subprocess.PIPE,  # 捕获错误
    encoding="utf-8" # 立即处理 I/O，减少延迟
)

question = re.compile(
    r"Q \d+\. Can a Subject with level ([A-Z]+) and categories \{(.*?)\} (read|write) an Object with level ([A-Z]+) and categories \{(.*?)\}\?"
)
question_count = 0
max_questions = 20

while question_count < max_questions:
    line = process.stdout.readline().strip()
    
    if not line:
        continue  # 避免空行导致错误

    if not line.startswith("Q "):  # 只处理问题行
        continue

    match = question.match(line)
    if not match:
            print("Error parsing question:", line)
            continue

        
    sub_name,sub_cat,operation,obj_name,obj_cat=match.groups()

    sub_categories =set(sub_cat.split(", ")) if sub_cat else set()
    obj_categories =set(obj_cat.split(", ")) if obj_cat else set()

    sub_level=levels[sub_name]
    obj_level=levels[obj_name]

    if operation=="read":
        allowed=sub_level>=obj_level and obj_categories.issubset(sub_categories)
    elif operation =="write":
        allowed=sub_level<=obj_level and sub_categories.issubset(obj_categories)
    else:
        allowed=False  
    question_count += 1

    answer= "yes" if allowed else "no"
    process.stdin.write(answer+"\n")
    process.stdin.flush()


process.stdin.close()
process.wait()

final_output = process.stdout.read().strip()
print(final_output)

