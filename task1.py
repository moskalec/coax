# There is string s = "Python Bootcamp". Write the code that hashes string.
import hashlib

s = "Python Bootcamp"


def hash_string(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    print(hash_string(s))
