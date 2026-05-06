from datetime import datetime
import json
import os


class Student:
    """学生类"""

    def __init__(self, sid, name, age, gender):
        self.sid = sid
        self.name = name
        self.age = age
        self.gender = gender
        self.scores = {}  # 科目:分数

    def add_score(self, subject, score):
        """添加/修改成绩"""
        if not isinstance(score, (int, float)):
            raise TypeError("成绩必须是数字")
        if score < 0 or score > 100:
            raise ValueError("成绩必须在0-100之间")
        self.scores[subject] = score

    def get_average(self):
        """计算平均分"""
        if not self.scores:
            return 0
        return sum(self.scores.values()) / len(self.scores)

    def get_grade(self):
        """根据平均分返回等级"""
        avg = self.get_average()
        if avg >= 90:
            return "优秀"
        elif avg >= 80:
            return "良好"
        elif avg >= 70:
            return "中等"
        elif avg >= 60:
            return "及格"
        else:
            return "不及格"


    def __str__(self):
        return f"{self.sid}\t{self.name}\t{self.age}\t{self.gender}"

    def get_total(self):
        return sum(self.scores.values())


class StudentManager:
    """学生管理类"""

    def __init__(self):
        self.students = {}  # 学号:学生对象

    def add_student(self, student):
        """添加学生"""
        if student.sid in self.students:
            raise Exception("学号已存在：" + student.sid)
        self.students[student.sid] = student

    def remove_student(self, sid):
        """删除学生"""
        if sid not in self.students:
            raise Exception("学号不存在：" + sid)
        name = self.students[sid].name
        del self.students[sid]

    def find_student(self, sid):
        """查找学生"""
        if sid not in self.students:
            raise Exception("未找到该学号：" + sid)
        return self.students[sid]

    def find_student_by_name(self, name):
        """根据姓名查找"""
        results = []
        for student in self.students.values():
            if student.name == name:
                results.append(student)
        return results

    def update_score(self, sid, subject, score):
        """更新成绩"""
        student = self.find_student(sid)


        student.add_score(subject, score)

    def show_all_students(self):
        """显示所有学生"""
        if not self.students:
            print("\n暂无学生数据！")
            return
        print("\n" + "=" * 80)
        print(f"{'学号':<12}{'姓名':<10}{'年龄':<6}{'性别':<6}{'平均分':<10}{'等级':<10}")
        print("=" * 80)
        for student in self.students.values():
            avg = student.get_average()
            grade = student.get_grade()
            print(f"{student.sid:<12}{student.name:<10}{student.age:<6}{student.gender:<6}{avg:<10.2f}{grade:<10}")
        print("=" * 80)
        print(f"共 {len(self.students)} 名学生")

    def show_student_detail(self, sid):
        """显示详情"""
        try:
            student = self.find_student(sid)
            print("\n" + "=" * 60)
            print(f"学生详细信息 - {student.name}")
            print("=" * 60)
            print(f"学号：{student.sid}")
            print(f"姓名：{student.name}")
            print(f"年龄：{student.age}")
            print(f"性别：{student.gender}")
            if student.scores:
                print("\n成绩单：")
                print("-" * 40)
                print(f"{'科目':<12}{'成绩':<8}{'等级':<10}")
                print("-" * 40)
                for subject, score in student.scores.items():
                    grade = student.get_grade()
                    print(f"{subject:<12}{score:<8}{grade:<10}")
                print("-" * 40)
                print(f"总分：{student.get_total():.2f}")
                print(f"平均分：{student.get_average():.2f}")
                print(f"总评等级：{student.get_grade()}")
            else:
                print("\n暂无成绩记录")
            print("=" * 60)
        except Exception as e:
            print(f"错误：{e}")

    def show_class_statistics(self):
        """班级统计"""
        if not self.students:
            print("\n暂无学生数据")
            return
        grade_count = {"优秀": 0, "良好": 0, "中等": 0, "及格": 0, "不及格": 0}
        total_score = 0
        highest_student = None
        lowest_student = None
        highest_avg = -1
        lowest_avg = 101

        for student in self.students.values():
            avg = student.get_average()
            grade = student.get_grade()
            grade_count[grade] += 1
            total_score += avg
            if avg > highest_avg:
                highest_avg = avg
                highest_student = student
            if avg < lowest_avg:
                lowest_avg = avg
                lowest_student = student

        class_avg = total_score / len(self.students)
        print("\n" + "=" * 60)
        print("班级统计信息")
        print("=" * 60)
        print(f"班级总人数：{len(self.students)}人")
        print(f"班级平均分：{class_avg:.2f}分")
        if highest_student:
            print(f"最高分：{highest_student.name} ({highest_avg:.2f})")
        if lowest_student:
            print(f"最低分：{lowest_student.name} ({lowest_avg:.2f})")
        print("\n等级分布：")
        print("-" * 40)
        for g, c in grade_count.items():
            p = (c / len(self.students)) * 100
            bar = "█" * int(p // 2)
            print(f"{g:<8}{c:>3}人 ({p:>5.1f}%) {bar}")
        print("=" * 60)

    def save_to_txt(self, filename):
        """保存文件"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("=" * 80 + "\n")
                f.write("学生成绩管理系统数据\n")
                f.write(f"导出时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 80 + "\n\n")
                for s in self.students.values():
                    f.write(f"【学生信息】\n")
                    f.write(f"学号：{s.sid}\n姓名：{s.name}\n年龄：{s.age}\n性别：{s.gender}\n")
                    if s.scores:
                        f.write("成绩：\n")
                        for sub, sc in s.scores.items():
                            g = s.get_grade()
                            f.write(f"  {sub}：{sc}分 ({g})\n")
                        f.write(f"平均分：{s.get_average():.2f}\n总评：{s.get_grade()}\n")
                    else:
                        f.write("成绩：暂无\n")
                    f.write("\n" + "-" * 40 + "\n\n")
            print(f"✓ 已保存到 {filename}")
        except Exception as e:
            print(f"✗ 保存失败：{e}")


def main():
    manager = StudentManager()
    try:
        demo = [
            Student("2024001", "张三", 20, "男"),
            Student("2024002", "李四", 19, "女"),
            Student("2024003", "王五", 21, "男"),
            Student("2024004", "赵六", 20, "女"),
            Student("2024005", "小明", 19, "男")
        ]
        for s in demo:
            manager.add_student(s)





        manager.update_score("2024001", "数学", 92)
        manager.update_score("2024001", "语文", 85)
        manager.update_score("2024001", "英语", 88)
        manager.update_score("2024002", "数学", 95)
        manager.update_score("2024002", "语文", 90)
        manager.update_score("2024002", "英语", 91)
        manager.update_score("2024003", "数学", 78)
        manager.update_score("2024003", "语文", 82)
        manager.update_score("2024003", "英语", 75)
        manager.update_score("2024004", "数学", 88)
        manager.update_score("2024004", "语文", 92)
        manager.update_score("2024004", "英语", 86)
        manager.update_score("2024005", "数学", 65)
        manager.update_score("2024005", "语文", 70)
        manager.update_score("2024005", "英语", 68)
    except Exception as e:
        print(f"初始化出错：{e}")

    while True:
        print("\n" + "=" * 70)
        print("========== 智能学生成绩管理系统 ==========")
        print("1. 添加学生")
        print("2. 删除学生")
        print("3. 查找学生")
        print("4. 添加/修改成绩")
        print("5. 查看学生成绩单")
        print("6. 显示所有学生")
        print("7. 班级统计信息")
        print("8. 导出成绩报告（TXT）")
        print("0. 退出系统")
        print("=" * 70)
        choice = input("请选择操作：")

        try:
            if choice == "1":
                print("\n--- 添加学生 ---")
                sid = input("学号：")
                name = input("姓名：")
                age = int(input("年龄："))
                gender = input("性别（男/女）：")
                student = Student(sid, name, age, gender)
                manager.add_student(student)
                print("✓ 添加成功")
            elif choice == "2":
                sid = input("输入要删除的学号：")
                manager.remove_student(sid)
                print("✓ 删除成功")
            elif choice == "3":
                t = input("按1.学号 2.姓名查找：")
                if t == "1":
                    sid = input("学号：")
                    manager.show_student_detail(sid)
                elif t == "2":
                    name = input("姓名：")
                    res = manager.find_student_by_name(name)
                    if res:
                        for s in res:
                            print(f"{s.sid} - {s.name}")
                    else:
                        print("未找到")
            elif choice == "4":
                sid = input("学号：")
                sub = input("科目：")
                sc = float(input("成绩："))
                manager.update_score(sid, sub, sc)
                print("✓ 成绩更新成功")
            elif choice == "5":
                sid = input("学号：")
                manager.show_student_detail(sid)
            elif choice == "6":
                manager.show_all_students()
            elif choice == "7":
                manager.show_class_statistics()
            elif choice == "8":
                manager.save_to_txt("成绩报告.txt")
            elif choice == "0":
                print("\n再见！")
                break
            else:
                print("输入无效")
        except ValueError:
            print("✗ 输入格式错误")
        except Exception as e:
            print(f"✗ 错误：{e}")


if __name__ == "__main__":
    main()
    # help(StudentManager)