#!/usr/bin/python3
import os

def check_readme():
    if os.path.exists("README.md"):
        if os.path.getsize("README.md") > 0:
            print("README.md exists and is not empty")
        else:
            print("README.md exists but is empty")
    else:
        print("README.md does not exist")

if __name__ == "__main__":
    from add_0 import add

    # Check if README.md exists and is not empty
    check_readme()

    # Addition operation
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
