sql--是一种用于管理数据或者图表的语言
    SELECT payload FROM entries 
        --简单的查询语句，从entries表中选择payload列
    SELECT payload FROM entries WHERE flag_tag=1337 AND substr(payload,1,3)='pwn'
        --查询entries表中flag_tag为1337且payload的前三个字符为pwn的数据,这个语句会返回包含pwn的整行数据
    SELECT content FROM notes WHERE substr(content, 1, 3) = 'pwn' LIMIT 1;
        --查询notes表中content的前三个字符为pwn的数据，这个语句会返回第一行数据,这个语句会返回包含pwn的整行数据
            --由于增加LIMIT 1，所以只会返回第一行数据
    SELECT name FROM sqlite_master WHERE type='table';
        --查询sqlite_master表中type为table的数据，这个语句会返回所有表的名字, sqlite_master是sqlite数据库中的一个系统表，用于存储数据库的元数据
    SELECT record FROM logs WHERE record LIKE 'pwn%';
        --字符串查找，查询logs表中record列中包含pwn的数据，这个语句会返回包含pwn的整行数据

table_name = "".join(random.sample(string.ascii_letters, 8))
    --额外内容 python使用, 生成一个8位的随机字符串
        --random.sample() 随机抽取不重复元素
        --string.ascii_letters 包含所有字母的字符串
        --"".join() 将列表中的元素连接成字符串
