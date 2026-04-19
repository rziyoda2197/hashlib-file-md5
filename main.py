import hashlib

def fayl_md5(hash_fayl):
    md5 = hashlib.md5()
    with open(hash_fayl, 'rb') as f:
        for b in iter(lambda: f.read(4096), b''):
            md5.update(b)
    return md5.hexdigest()

print(fayl_md5('fayl.txt'))
