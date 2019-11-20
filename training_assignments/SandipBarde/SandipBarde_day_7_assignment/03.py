import os
import requests
import asyncio
import time

inputs = [
    ("https://files.pythonhosted.org/packages/ab/6f/b5dd831c5655d06504c0740f415a52246c7223163208141c617dae7a1b3b/intel_scipy-1.1.0-cp36-cp36m-manylinux1_x86_64.whl", 2, 1),
    ("http://google.com/favicon.ico", 10, 0.5),
    ("https://youtu.be/PJ4t2U15ACo", 3, 2),
    ("https://www.w3schools.com/python/python_intro.asp", 20, 1)]

async def save_url_ata(url, attempt, extension):
    path = os.getcwd()
    path += "\\asyncio\\"
    filePath = path
    filePath += str(attempt)
    if(len(extension) == 3):
        filePath += "."
        filePath += extension
    try:
        print(filePath)
        r = requests.get(url[0], allow_redirects=True)
        fp = open(filePath, "wb")
        fp.write(r.content)
        fp.close()
    except Exception as e:
        print(e)


def SeprateStringUsingDelimeter(s):
    s = s[0].split('.')
    return (s[len(s)-1])


async def main():
    count1 = inputs[0][1]
    count2 = inputs[1][1]
    count3 = inputs[2][1]
    count4 = inputs[3][1]
    while(count1 > 0 or count2 > 0 or count3 > 0 or count4 > 0):
        if (count1 > 0):
            await save_url_ata(inputs[0], count1, SeprateStringUsingDelimeter(inputs[0]))
            count1 = count1 - 1
        if (count2 > 0):
            await save_url_ata(inputs[1], count2, SeprateStringUsingDelimeter(inputs[1]))
            count2 = count2 -1
        if (count3 > 0):
            await save_url_ata(inputs[2], count3, SeprateStringUsingDelimeter(inputs[2]))
            count3 = count3 -1
        if (count4 > 0):
            await save_url_ata(inputs[3], count4, SeprateStringUsingDelimeter(inputs[3]))
            count4 = count4 - 1

asyncio.run(main())