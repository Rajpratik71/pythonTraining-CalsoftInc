def OpenAndWriteIntoFile():
    with open("fileDemo.txt", "r") as f:
        content = f.read()
        print(content)
    with open("fileDemo.txt", "a") as f:
        f.writelines("\n")
        f.writelines("First new Added line\n")
        f.writelines("Second new Added line\n")
    with open("fileDemo.txt", "r") as f:
        content = f.read()
        print(content)

OpenAndWriteIntoFile()