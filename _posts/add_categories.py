import os
from glob import glob


def show():
    # exit()
    # os.chdir("_posts/C_C++")
    print(os.getcwd())
    # exit()
    fs = glob("*.md")
    for i in fs:
        with open(i, "a+") as f:
            f.seek(0)
            f.seek(4)
            # print(f.tell())
            content = f.read()
            f.seek(0)
            f.seek(4)
            # print(content)
            f.truncate()
            f.write("categories: [Linux-Shell]")
            f.write("\n")
            # print(content)
            f.write(content)
        # exit()
        print(i, "ok")


if __name__ == "__main__":
    show()
