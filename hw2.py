import os
import string
import random

def main():                                                #use for communicate with user and 调用其余函数

    desk_path=os.path.join(os.path.expanduser("~"),"Desktop")
    file_name="人工智能编程语言学生名单.txt"
    file_path=os.path.join(desk_path,file_name)
    print(f"正在读取文件{file_path}")
    system=ExamSystem(file_path)

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


class Student:
  def __init__(self,name,num,id,college,gender):
    self.college=college
    self.name=name
    self.num=num
    self.id=id
    self.gender=gender
  def __str__(self):
      print(f"{self.name} {self.id} {self.college} {self.gender}")

class ExamSystem:

    def __init__(self,file_path):
       self.student_list=[]
       self.load_student(file_path)

    @staticmethod    #静态方法，检查输入是否为空，拦截空输入，不用self
    def check_path_valid(path):
       if not path:
           return False
       return True

    def load_student(self,file_path):
        try:
            if not os.path.exists(file_path):
               print("error path，please confirm the path")
               return
            with (open(file_path,"r",encoding="utf-8") as f):
             lines=f.readlines()
             for line in lines[1:]:
                line = line.strip()  # 去掉每行末尾的换行符和空格
                if not line:  # 如果是空行，就跳过
                    continue
                parts = line.split("\t")

                new_student=Student(
                    id=parts[4],  # 学号在第5列
                    name=parts[1],  # 姓名在第2列
                    gender=parts[2],  # 性别在第3列
                    class_num=parts[3],  # 班级在第4列
                    college=parts[5]
                )
                self.students.append(new_student)
                print("succed")
        except Exception as e:
                print(f"出错了{e}")

#根据id查找学生功能
        def find_student(self,target_id):
            found = False                              #旗帜作用
            for s in self.students:
                if s.id == target_id:
                    found = True
                    print(f"找到学生\n{s}")
                    break
                if not found:                           #if not Ture
                    print(f"未找到学号为{target_id}的学生")

        def











