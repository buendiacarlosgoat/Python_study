import os
import random


def main():  # use for communicate with user and 调用其余函数

    desk_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_name = "人工智能编程语言学生名单.txt"
    file_path = os.path.join(desk_path, file_name)
    print(f"正在读取文件{file_path}")
    system = ExamSystem(file_path)

    if len(system.students) == 0:
        print("⚠️ 由于没有加载到学生数据，程序将退出。请检查文件是否存在。")
        return

    while True:
        print("\n--- 请选择功能 ---")
        print("1. 查询学生信息 (输入学号)")
        print("2. 随机点名")
        print("3. 生成考场安排表")
        print("4. 生成准考证文件")
        print("5. 退出系统")

        choice = input("请输入选项 (1-5): ")

        if choice == '1':
            sid = input("请输入要查询的学号: ")
            system.find_student(sid)

        elif choice == '2':
            count_input = input("请输入随机点名人数: ")
            system.roll_call(count_input)

        elif choice == '3':
            capacity_input = input("请输入每个考场容纳人数（默认30）: ") or "30"
            system.generate_seat(capacity_input)

        elif choice == '4':
            system.generate_admission_tickets()

        elif choice == '5':
            print("已退出系统，再见！")
            break

        else:
            print("⚠️ 无效选项，请输入 1-5。")


class Student:
    def __init__(self, name, num, id, college, gender, class_num=""):
        self.college = college
        self.name = name
        self.num = num      # 序号
        self.id = id        # 学号
        self.gender = gender
        self.class_num = class_num
        self.exam_room = None   # 考场号（生成后赋值）
        self.seat_num = None    # 座位号（生成后赋值）
        self.admission_no = None  # 准考证号（生成后赋值）

    def __str__(self):
        return (f"姓名: {self.name} | 学号: {self.id} | "
                f"学院: {self.college} | 性别: {self.gender} | 班级: {self.class_num}")


class ExamSystem:

    def __init__(self, file_path):
        self.students = []
        self.load_student(file_path)

    @staticmethod  # 静态方法，检查输入是否为空，拦截空输入，不用self
    def check_path_valid(path):
        if not path:
            return False
        return True

    def load_student(self, file_path):
        try:
            if not os.path.exists(file_path):
                print("error path，please confirm the path")
                return
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines[1:]:
                    line = line.strip()  # 去掉每行末尾的换行符和空格
                    if not line:         # 如果是空行，就跳过
                        continue
                    parts = line.split("\t")
                    if len(parts) < 6:
                        continue  # 数据列不足，跳过

                    new_student = Student(
                        num=parts[0],       # 序号在第1列
                        name=parts[1],      # 姓名在第2列
                        gender=parts[2],    # 性别在第3列
                        class_num=parts[3], # 班级在第4列
                        id=parts[4],        # 学号在第5列
                        college=parts[5]    # 学院在第6列
                    )
                    self.students.append(new_student)
            print(f"✅ 成功加载 {len(self.students)} 名学生数据。")
        except Exception as e:
            print(f"出错了: {e}")

    # 根据学号查找学生功能
    def find_student(self, target_id):
        found = False  # 旗帜作用
        for s in self.students:
            if s.id == target_id:
                found = True
                print(f"找到学生：\n{s}")
                break
        if not found:  # if not True
            print(f"未找到学号为 {target_id} 的学生")

    # 随机点名
    def roll_call(self, count_input):
        """功能2：随机点名"""
        try:
            count = int(count_input)
            if count <= 0:
                print("⚠️ 点名人数必须大于0！")
                return
            if count > len(self.students):
                print(f"⚠️ 班里一共只有 {len(self.students)} 人，你不能点 {count} 个！")
                return
            chosen = random.sample(self.students, count)
            print(f"\n随机点名结果（共 {count} 人）：")
            for i, s in enumerate(chosen, start=1):
                print(f"{i}. {s.name}  学号: {s.id}")
            print("--------------------------")
        except Exception as e:
            print(f"发生以下错误: {e}")

    # 生成考场安排表
    def generate_seat(self, capacity_input="30"):
        """功能3：生成考场安排表，并保存到桌面"""
        try:
            capacity = int(capacity_input)
            if capacity <= 0:
                print("⚠️ 每考场人数必须大于0！")
                return

            # 打乱顺序，随机分配考场
            shuffled = self.students[:]
            random.shuffle(shuffled)

            room_num = 1
            seat_num = 1
            for s in shuffled:
                s.exam_room = room_num
                s.seat_num = seat_num
                # 生成准考证号：考场号(3位) + 座位号(3位)
                s.admission_no = f"{room_num:03d}{seat_num:03d}"
                seat_num += 1
                if seat_num > capacity:
                    seat_num = 1
                    room_num += 1

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

        except Exception as e:
            print(f"生成考场安排表出错: {e}")

    # 生成准考证文件
    def generate_admission_tickets(self):
        """功能4：生成准考证文件，每位学生一张，保存到桌面"""
        try:
            # 如果还没分配考场，先自动分配
            if not self.students[0].exam_room:
                print("⚠️ 尚未生成考场安排，正在自动生成（默认每场30人）...")
                self.generate_seat("30")

            desk_path = os.path.join(os.path.expanduser("~"), "Desktop")
            out_path = os.path.join(desk_path, "准考证.txt")

            with open(out_path, "w", encoding="utf-8") as f:
                for s in self.students:
                    f.write("=" * 40 + "\n")
                    f.write("           准  考  证\n")
                    f.write("=" * 40 + "\n")
                    f.write(f"  姓    名：{s.name}\n")
                    f.write(f"  学    号：{s.id}\n")
                    f.write(f"  性    别：{s.gender}\n")
                    f.write(f"  班    级：{s.class_num}\n")
                    f.write(f"  学    院：{s.college}\n")
                    f.write(f"  准考证号：{s.admission_no}\n")
                    f.write(f"  考    场：第 {s.exam_room} 考场\n")
                    f.write(f"  座    位：第 {s.seat_num} 号\n")
                    f.write("=" * 40 + "\n\n")

            print(f"✅ 准考证生成完成！共 {len(self.students)} 张，已保存到桌面：准考证.txt")

        except Exception as e:
            print(f"生成准考证出错: {e}")


if __name__ == "__main__":
    main()
