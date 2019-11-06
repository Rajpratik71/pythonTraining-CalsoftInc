def image_res(imgname):
    with open(imgname, "rb") as img_file:
        img_file.seek(163)

        a = img_file.read(2)

        height = ()
