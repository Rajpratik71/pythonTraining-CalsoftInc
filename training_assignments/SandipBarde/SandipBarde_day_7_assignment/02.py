import os
import requests
from threading import Thread, current_thread, Lock
from concurrent.futures.thread import ThreadPoolExecutor
import time

inputs = [
    "https://files.pythonhosted.org/packages/ab/6f/b5dd831c5655d06504c0740f415a52246c7223163208141c617dae7a1b3b/intel_scipy-1.1.0-cp36-cp36m-manylinux1_x86_64.whl",
    "http://google.com/favicon.ico",
    "https://youtu.be/PJ4t2U15ACo",
    "https://www.w3schools.com/python/python_intro.asp",
    "https://www.google.com",
    "https://yahoo.com",
    "https://www.linkedin.com",
    "https://www.tutorialspoint.com/index.htm",
    "https://docs.python.org/3/",
    "https://www.bing.com"]

def save_url_ata(url,count):
    path = os.getcwd()
    path += "\\multithreading\\"
    filePath = path
    filePath += current_thread().getName()
    filePath += "_"
    filePath += str(count)
    try:
        print(filePath)
        r = requests.get(url, allow_redirects=True)
        fp = open(filePath, "wb")
        fp.write(r.content)
        fp.close()
    except Exception as e:
        print(e)


def SeprateStringUsingDelimeter(s):
    s = s[0].split('.')
    return (s[len(s)-1])


if __name__ == "__main__":
    start = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        count = 0
        for arg in inputs:
            count = count + 1
            executor.submit(save_url_ata, arg, count)
    print('All tasks has been finished in time ', time.time() - start )
