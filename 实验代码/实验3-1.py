"""
任务一：成绩计算工具（文件读取版）
功能：从文件读取成绩列表，计算统计信息，显示等级分布
"""

import sys
import os

def read_scores_from_file(filename):
    """
    从文件读取成绩（一行一个分数）
    处理文件不存在、格式错误等异常
    """
    scores = []

    try:
        # 检查文件是否存在


        # 打开文件读取
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            # 处理空文件
            if not lines:
                print(f"⚠️ 警告：文件 '{filename}' 为空")
                return scores

            # 逐行处理
            for line_num, line in enumerate(lines, 1):
                # 去除前后空白字符（包括换行符）
                score_str = line.strip()

                # 跳过空行
                if not score_str:
                    continue

                try:
                    # 转换为浮点数
                    score = float(score_str)

                    # 验证成绩范围
                    if score < 0 or score > 100:
                        print(f"⚠️ 警告：第{line_num}行成绩 {score} 超出范围（0-100），已跳过")
                        continue

                    scores.append(score)

                except ValueError:
                    print(f"⚠️ 警告：第{line_num}行 '{score_str}' 不是有效的数字，已跳过")
                    continue

        if scores:
            print(f"✓ 成功从文件 '{filename}' 读取 {len(scores)} 个有效成绩")
        else:
            print(f"⚠️ 文件中没有找到有效的成绩")
        
        return scores
    
    except FileNotFoundError as e:
        print(f"❌ 错误：{e}")
        return None
    except PermissionError:
        print(f"❌ 错误：没有权限读取文件 '{filename}'")
        return None
    except Exception as e:
        print(f"❌ 读取文件时发生未知错误：{e}")
        return None


def calculate_average(scores):
    """
    计算平均分
    处理空列表情况
    """
    try:
        average = sum(scores) / len(scores)
        return average
    except ZeroDivisionError:
        print("⚠️ 警告：成绩列表为空，无法计算平均分！")
        return 0
    except Exception as e:
        print(f"⚠️ 计算平均分时发生错误：{e}")
        return 0


def calculate_grade(score):
    """
    根据分数返回等级
    处理分数超出0-100范围的情况
    """
    try:
        if not isinstance(score, (int, float)):
            raise TypeError(f"分数必须是数字类型，当前类型：{type(score)}")
        
        if score < 0 or score > 100:
            raise ValueError(f"分数 {score} 超出范围（0-100）")
        
        if score >= 90:
            return "优秀"
        elif score >= 80:
            return "良好"
        elif score >= 70:
            return "中等"
        elif score >= 60:
            return "及格"
        else:
            return "不及格"
    
    except TypeError as e:
        print(f"❌ 等级计算错误：{e}")
        return "未知"
    except ValueError as e:
        print(f"❌ 等级计算错误：{e}")
        return "未知"


def show_statistics(scores):
    """
    显示统计信息
    最高分、最低分、平均分
    各等级人数分布
    使用表格形式输出
    """
    if not scores:
        print("\n⚠️ 没有有效的成绩数据，无法统计！")
        return
    
    print("\n" + "=" * 60)
    print("成绩统计结果")
    print("=" * 60)
    
    # 基础统计
    print(f"\n原始成绩：{', '.join([str(s) for s in scores])}")
    print(f"最高分：{max(scores):.2f}")
    print(f"最低分：{min(scores):.2f}")
    
    # 计算平均分（使用try-except-else-finally）
    average = 0
    try:
        average = calculate_average(scores)
        print(f"平均分：{average:.2f}")
    except Exception as e:

        print(f"计算平均分时出错：{e}")


    
    # 等级分布统计
    grade_count = {
        "优秀": 0,
        "良好": 0,
        "中等": 0,
        "及格": 0,
        "不及格": 0
    }
    
    # 统计各等级人数
    for score in scores:
        grade = calculate_grade(score)
        if grade in grade_count:
            grade_count[grade] += 1
    
    # 显示等级分布表格
    print("\n" + "-" * 60)
    print("等级分布")
    print("-" * 60)
    print(f"{'等级':<12}{'人数':<8}{'占比':<10}")
    print("-" * 60)
    
    total = len(scores)
    for grade in ["优秀", "良好", "中等", "及格", "不及格"]:
        count = grade_count[grade]
        percentage = (count / total) * 100 if total > 0 else 0
        print(f"{grade:<12}{count:<8}{percentage:>6.1f}%")
    
    print("-" * 60)
    
    # 详细成绩单
    print("\n" + "-" * 60)
    print("详细成绩单")
    print("-" * 60)
    print(f"{'序号':<8}{'成绩':<10}{'等级':<10}")
    print("-" * 60)
    
    for i, score in enumerate(scores, 1):
        grade = calculate_grade(score)
        print(f"{i:<8}{score:<10.2f}{grade:<10}")
    
    print("-" * 60)
    
    # 额外统计信息
    print("\n" + "-" * 60)
    print("额外统计")
    print("-" * 60)
    
    # 计算标准差
    try:
        if len(scores) > 1:
            mean = sum(scores) / len(scores)
            variance = sum((x - mean) ** 2 for x in scores) / len(scores)
            std_dev = variance ** 0.5
            print(f"标准差：{std_dev:.2f}")
            
            # 成绩分布区间
            print(f"\n成绩分布区间：")
            print(f"  优秀（90-100）：{grade_count['优秀']}人")
            print(f"  良好（80-89）：{grade_count['良好']}人")
            print(f"  中等（70-79）：{grade_count['中等']}人")
            print(f"  及格（60-69）：{grade_count['及格']}人")
            print(f"  不及格（0-59）：{grade_count['不及格']}人")
    except Exception as e:
        print(f"计算额外统计时出错：{e}")
    
    print("=" * 60)


def main():
    """
    主函数
    使用 try-except-else-finally 结构
    """
    print("=" * 60)
    print("欢迎使用成绩计算工具")
    print("=" * 60)
    
    # 检查命令行参数  需要   import sys
    if len(sys.argv) < 2:
        print("\n使用方法：python main.py <成绩文件>")
        print("示例：python main.py scores.txt")
        print("\n或者输入文件名：")
        filename = input("请输入成绩文件名：").strip()
        if not filename:
            print("❌ 未输入文件名，程序退出")
            return
    else:
        filename = sys.argv[1]
    
    print(f"\n正在读取文件：{filename}")
    
    scores = None
    
    try:
        # 从文件读取成绩
        scores = read_scores_from_file(filename)
        
        # 检查是否成功读取数据
        if scores is None:
            print("❌ 无法读取文件数据")
            return
        
        # 显示统计信息
        if scores:
            show_statistics(scores)

            print("\n✅ 成绩分析完成！")

            # 给出建议
            avg = calculate_average(scores)
            if avg >= 90:
                print("🎉 表现优异！继续保持！")
            elif avg >= 80:
                print("👍 表现良好！还可以更好！")
            elif avg >= 70:
                print("📚 表现中等，继续努力！")
            elif avg >= 60:
                print("💪 刚好及格，需要加油！")
            else:
                print("⚠️ 需要加倍努力！")
        else:
            print("⚠️ 没有有效的成绩数据可以统计")
    
    except KeyboardInterrupt:
        print("\n\n⚠️ 用户中断操作")
    
    except Exception as e:
        print(f"\n❌ 程序运行出错：{e}")
    

    finally:
        # 无论是否有异常都执行
        print("\n感谢使用成绩计算工具，再见！")


if __name__ == "__main__":
    main()