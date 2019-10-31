import hashlib


def sha1_hash(filename):
    sha1_hash_obj = hashlib.sha1()

    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)

            sha1_hash_obj.update(chunk)

    return sha1_hash_obj.hexdigest()


digest = sha1_hash("testfile")

print(digest)
