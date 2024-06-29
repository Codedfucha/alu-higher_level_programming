#!/usr/bin/python3
import os

def check_readme():
    if os.path.exists("README.md"):
        if os.path.getsize("README.md") > 0:
            return "README.md exists and is not empty"
        else:
            return "README.md exists but is empty"
    else:
        return "README.md does not exist"

if __name__ == "__main__":
    from add_0 import add

    # Check if README.md exists and is not empty
    readme_status = check_readme()

    # Addition operation
    a = 1
    b = 2
    addition_result = "{} + {} = {}".format(a, b, add(a, b))

    # Combined print statement
    print("{}\n{}".format(readme_status, addition_result))
