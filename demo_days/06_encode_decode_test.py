#!/usr/local/bin/python3
import base64

mystr = 'O João mordeu o cão!'

mystr_encoded = base64.b64encode(mystr.encode('utf-8'))
# b'TyBKb8OjbyBtb3JkZXUgbyBjw6NvIQ=='
print(mystr_encoded)
# Decode
mystr_encoded = base64.b64decode(mystr_encoded).decode('utf-8')
print(mystr_encoded)
# 'O João mordeu o cão!'
