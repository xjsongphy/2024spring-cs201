homework = input("请输入作业编号：")
name = "宋昕杰"
college = "物理学院"
system_environment = "Windows 11 22H2"
python_environment = "PyCharm 2023.2 (Community Edition)"
c_environment = "g++ (x86_64-win32-seh-rev0, Built by MinGW-W64 project) 8.1.0"  #若有C/C++环境请改为具体想要填充的字符串，不要改为True

homework = "assignment" + homework + "\\" + "assignment" + homework + ".md"
context = ""
with open(homework, encoding="utf-8") as h:
    context = h.read()
output = context.replace("Hongfei Yan==同学的姓名、院系==", "Xinjie Song, Phy") \
    .replace("macOS Ventura 13.4.1 (c)", system_environment) \
    .replace("Spyder IDE 5.2.2, PyCharm 2023.1.4 (Professional Edition)", python_environment) \
    .replace("【张概论，中国语言文学系，2023年秋】 ==（请改为同学的姓名、院系）==", f"【{name}，{college}，2023年秋】") \
    .replace("==（请改为同学的思路和代码）==", "") \
    .replace("# 请改为同学的代码", "") \
    .replace("==（请替换为同学的AC代码截图，至少包含有\"Accepted\"的截图）==", "") \
    .replace("==（AC代码截图，至少包含有\"Accepted\"）==", "") \
    .replace("==（至少包含有\"Accepted\"）==", "") \
    .replace("==（请改为同学的操作系统、编程环境等）==\n", "") \
    .replace("\nC/C++编程环境：Mac terminal vi (version 9.0.1424), g++/gcc (Apple clang version 14.0.3, clang-1403.0.22.14.1)", \
             f"\nC/C++编程环境：{c_environment}" if c_environment else "")
newfile = homework.replace(".md", "_sxj.md")
with open(newfile, "x", encoding="utf-8") as f:
    f.write(output)
    print(f"文件已填充完成，请打开{newfile}查看")