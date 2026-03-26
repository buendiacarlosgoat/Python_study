# Python_study

记录我的Python学习之路

## 项目说明

本仓库包含Python学习过程中的作业和练习代码。
以下为项目说明，真正的readme
## 项目说明

本仓库包含Python学习过程中的作业和练习代码。

### 文件说明

| 文件 | 说明 |
|------|------|
| `hw1_1.py` | 学生成绩管理系统 - 支持成绩录入、字典转换、排序等功能 |
| `hw2.py` | 考场管理系统 - 支持学生信息管理、随机点名、考场安排、准考证生成 |

 注意：运行前请确保桌面存在 `人工智能编程语言学生名单.txt` 数据文件，格式为制表符分隔的文本文件（第一行为表头）。


---

# 李云迪-24345033-第二次人工智能编程作业

## 1. 任务拆解与 AI 协作策略

我在编写代码前，阅读完作业要求，将完整的考场管理系统任务拆解为四个层次，并按照顺序让 AI 逐步完成：

**步骤1：文件的读取和搭建基础信息框架**
首先要求 AI 创建一个包含 `Student` 类和 `ExamSystem` 类的 Python 程序框架，仅实现数据加载功能。目的是验证 AI 是否理解面向对象编程的基本结构。通过代码将桌面上的txt文档内容写入"Student"类中。

**步骤2：具体功能的实现**
让 AI 为 ExamSystem 类添加三个用户交互功能，完成作业要求：
- 按学号查找学生（功能1）
- 随机点名（功能2）
- 生成考场安排表，存储到桌面（功能3）


**步骤3：生成准考证，格式化输出**
在确认前三个功能运行正常后，再要求 AI 添加第四个功能：生成准考证文件（功能4），并确保该功能能与考场安排表联动。

**步骤4：异常处理**
最后让 AI 为所有可能出错的地方添加异常捕获和处理，包括：文件不存在、用户输入非法值、数据格式错误等。

## 2. 核心 Prompt 迭代记录

**初代 Prompt（3月24日）**
“帮我补全 Python 考场管理系统，实现随机点名、考场安排和准考证生成功能。”
“帮我打印考场安排表”

**AI 生成的问题/缺陷：**
1. AI 使用了过于复杂的逻辑：在考场分配时试图根据班级和学院分组，违背了随机分配的原则。
2. AI 遗漏了准考证号生成规则：没有实现“考场号3位 + 座位号3位”的准考证号生成逻辑。
3. 异常处理不完整：仅在文件加载时处理了错误，用户输入无效数据时程序会崩溃。
4. 考场安排表的表头与内容错位

**优化后的 Prompt（追问）**
“请修改代码，要求：
- 考场安排必须完全随机分配（不考虑班级/学院）
- 准考证号格式：考场号（3位）+座位号（3位），例如考场1座位30为 '001030'
- 所有用户输入（点名人数、考场容量）都必须进行类型检查和异常捕获
- 如果用户选择生成准考证时考场尚未分配，自动调用考场生成功能（默认30人）
- 最终生成的文件保存在桌面”

- 我需要表头与内容对照，用更加易于编辑的函数方法打印表格

**迭代效果：**
AI 将 `generate_seat` 方法中的排序逻辑替换为 `random.shuffle` 实现真正的随机分配；在 `generate_admission_tickets` 中添加了自动调用考场分配的逻辑；并在所有用户交互处添加了 try/except 捕获异常。

移除 \t：在 generate_seat 函数中，不再使用 f.write(...\t...)。
引入格式化字符串：定义了 header_fmt 和 row_fmt。使用了 {: <宽度} 语法。例如 {: <10} 表示该字段内容左对齐，并且强制占用 10 个字符的宽度。如果内容不足 10 个字，会自动补空格；如果超过，则显示全部内容（这可能会稍微挤到下一列，但在中文环境下通常足够）

## 3. Debug 与异常处理记录

**报错类型/漏洞现象**
运行程序时发现 FileNotFoundError，并发现 `load_student` 方法中的 `parts[3]` 索引错误。

**解决过程**
1. 将报错信息喂给 AI：`"出错了: IndexError: list index out of range"`
2. AI 检查后指出 `parts` 列表中班级信息在第3列（原始数据为序号、姓名、性别、班级、学号、学院），而代码误用了性别信息。
3. AI 修改为：
```python
new_student = Student(
    num=parts[0],       # 序号在第1列
    name=parts[1],      # 姓名在第2列
    gender=parts[2],    # 性别在第3列
    class_num=parts[3], # 班级在第4列
    id=parts[4],        # 学号在第5列
    college=parts[5]    # 学院在第6列
)
```

## 4. 人工代码审查 

以下是 AI 生成的 `generate_seat` 方法的核心逻辑代码


  # def generate_seat(self, capacity_input="30"):
             """功能3：生成考场安排表，并保存到桌面"""
    try:
        capacity = int(capacity_input)  # 将输入的字符串转换为整数
        if capacity <= 0:               # 检查考场容量是否合法
            print("⚠️ 每考场人数必须大于0！")
            return

        # 打乱顺序，随机分配考场
        shuffled = self.students[:]     # 复制一份学生列表
        random.shuffle(shuffled)        # 随机重新排列学生顺序

        room_num = 1                    # 初始化考场号为1
        seat_num = 1                    # 初始化座位号为1
        for s in shuffled:              # 遍历每一个被随机分配的学生
            s.exam_room = room_num      # 为该学生分配考场号
            s.seat_num = seat_num       # 为该学生分配座位号
            # 生成准考证号：考场号(3位) + 座位号(3位)
            s.admission_no = f"{room_num:03d}{seat_num:03d}"
            seat_num += 1               # 座位号递增
            if seat_num > capacity:     # 如果当前考场满员
                seat_num = 1            # 重置座位号为1
                room_num += 1           # 开启下一个考场

        # 保存到桌面
        desk_path = os.path.join(os.path.expanduser("~"), "Desktop")
        out_path = os.path.join(desk_path, "考场安排表.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("考场号\t座位号\t姓名\t学号\t性别\t班级\t学院\n")
            for s in sorted(shuffled, key=lambda x: (x.exam_room, x.seat_num)):
                f.write(f"{s.exam_room}\t{s.seat_num}\t{s.name}\t"
                        f"{s.id}\t{s.gender}\t{s.class_num}\t{s.college}\n")

        total_rooms = shuffled[-1].exam_room if shuffled else 0
        print(f"✅ 考场安排完成！共 {total_rooms} 个考场，已保存到桌面：考场安排表.txt")

    except Exception as e:  # 捕获所有可能的异常
        print(f"生成考场安排表出错: {e}")
```

**人工注释总结：**
1. `capacity = int(capacity_input)` 将字符串转为数字，如果用户输入非数字会抛出异常被捕获。
2. `random.shuffle(shuffled)` 是实现随机分配的关键，完全打乱顺序避免人为偏见。
3. `room_num` 和 `seat_num` 的递增逻辑模拟了真实的考场分配流程。
4. `f"{room_num:03d}{seat_num:03d}"` 用格式化字符串确保准考证号始终为6位数字。
5. `sorted(shuffled, key=lambda x: (x.exam_room, x.seat_num))` 按考场号和座位号排序后写入文件，确保输出文件有清晰的顺序。

以下为项目说明，真正的readme
## 项目说明

本仓库包含Python学习过程中的作业和练习代码。

### 文件说明

| 文件 | 说明 |
|------|------|
| `hw1_1.py` | 学生成绩管理系统 - 支持成绩录入、字典转换、排序等功能 |
| `hw2.py` | 考场管理系统 - 支持学生信息管理、随机点名、考场安排、准考证生成 |

 注意：运行前请确保桌面存在 `人工智能编程语言学生名单.txt` 数据文件，格式为制表符分隔的文本文件（第一行为表头）。
