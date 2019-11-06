import os
import shutil

if os.path.exists("testfile"):
    src = os.path.realpath("testfile")
    os.rename("testfile", "new_test")
    root_dir, tail = os.path.split(src)
    shutil.make_archive("test_archive", "zip", root_dir)

    with zip.Zipfile("test.zip", "w") as newzip:
        newzip.write("testfile")
        newzip.write("new_test")
