# -*- coding: utf-8 -*-
import base64


def safe_base64_decode(s):
    l= 4 - (len(s)%4)
    if isinstance(s,bytes):
        s = s + b"="*l
    else:
        s = s + "="*l
    return base64.b64decode(s)

    
 
# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')