
input_str=input("输入学生成绩格式如下：学生姓名,高数成绩,英语成绩,大物成绩\n")
str_list=input_str.split(";")
print(str_list)
#将字符串转换为一个列表，每个元素是一个字符串
next_list= [item.split(",") for item in str_list]
#3.	将列表中的每个元素再转换为一个列表，每个元素是一个字符串
nest_list_raw = [item.split(",") for item in str_list]
print("输出列表")
print(next_list)
#步骤3：
print(nest_list_raw)
#将列表元素转换为字典，名字作为key
head=nest_list_raw[0]
body=nest_list_raw[1:]
dict_list=[]
print(f"表头: {head}")
print(f"第一行数据示例: {body[0]}")
for item in body:
    # 1. 先配对生成字典
    temp_dict = dict(zip(head, item))

    # 2. 遍历字典，转换成绩
    for key in temp_dict:
        if key != "学生姓名":
            val = temp_dict[key]

            # 如果是列表，取第一个元素
            if isinstance(val, list):
                val = val[0]

            # 转换为整数并更新回字典
            temp_dict[key] = int(val)

    # 3. 【重要】等这个学生的所有成绩都处理完后，再把整个字典加入大列表
    # 这一步必须和内部的 for 循环对齐，不能在 if 里面！
    dict_list.append(temp_dict)

print(dict_list)




#学生姓名,高数成绩,英语成绩,大物成绩;SanZhang,70,
#80,61;SiLi,86,77,81;WuWang,88,90,
#77;MingLi,60,77,81;MiWang,71,70,60;HaiLi,
#88,78,89;HeWang,70,90,80;LiWang,67,71,70
