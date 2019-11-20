import os
import requests
from threading import Thread, current_thread

inputs = [
    ("https://files.pythonhosted.org/packages/ab/6f/b5dd831c5655d06504c0740f415a52246c7223163208141c617dae7a1b3b/intel_scipy-1.1.0-cp36-cp36m-manylinux1_x86_64.whl", 2, 1),
    ("http://google.com/favicon.ico", 10, 0.5),
    ("https://youtu.be/PJ4t2U15ACo", 3, 2),
    ("https://www.w3schools.com/python/python_intro.asp", 20, 1)]

def save_url_ata(url, attempt, extension):
    path = os.getcwd()
    path += "\\multithreading\\"
    filePath = path
    filePath += current_thread().getName()
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


if __name__ == "__main__":
    count1 = inputs[0][1]
    count2 = inputs[1][1]
    count3 = inputs[2][1]
    count4 = inputs[3][1]
    while(count1 > 0 or count2 > 0 or count3 > 0 or count4 > 0):
        if (count1 > 0):
            t1 = Thread(target=save_url_ata, args=(inputs[0], count1, SeprateStringUsingDelimeter(inputs[0])))
        if (count2 > 0):
            t2 = Thread(target=save_url_ata, args=(inputs[1], count2, SeprateStringUsingDelimeter(inputs[1])))
        if (count3 > 0):
            t3 = Thread(target=save_url_ata, args=(inputs[2], count3, SeprateStringUsingDelimeter(inputs[2])))
        if (count4 > 0):
            t4 = Thread(target=save_url_ata, args=(inputs[3], count4, SeprateStringUsingDelimeter(inputs[3])))
        if(count1 > 0):
            t1.start()
            count1 = count1 - 1
            t1.join(inputs[0][2])

        if(count2 > 0):
            t2.start()
            count2 = count2 - 1
            t2.join(inputs[1][2])
        if(count3 > 0):
            t3.start()
            count3 = count3-1
            t3.join(inputs[2][2])

        if(count4 > 0):
            t4.start()
            count4 = count4 - 1
            t4.join(inputs[3][2])
