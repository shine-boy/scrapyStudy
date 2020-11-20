from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import base64,codecs

# 如果text不足16位的倍数就用空格补足为16位
def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')


# 加密函数
def encrypt(text):
    key = '0CoJUm6Qyw8W8jud'.encode('utf-8')
    mode = AES.MODE_CBC
    iv = b'0102030405060708'
    text = add_to_16(text)
    cryptos = AES.new(key, mode, iv)
    cipher_text = cryptos.encrypt(text)
    # 因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为16进制字符串
    return b2a_hex(cipher_text)


# 解密后，去掉补足的空格用strip() 去掉
def decrypt(text):
    key = '0CoJUm6Qyw8W8jud'.encode('utf-8')
    iv = b'0102030405060708'
    mode = AES.MODE_CBC
    print(text.__len__())
    print(text.__len__()%16
          )
    cryptos = AES.new(key, mode, iv)
    plain_text = cryptos.decrypt(a2b_hex(text))
    return bytes.decode(plain_text).rstrip('\0')


if __name__ == '__main__':
    re= "XAwiglTqS3SiXNOBoHkXbti1rsv/zuW5pZEKhi7Jv4EXJnqIwC2C7Rpi8NagIBLJScidbQ5/220bVp5GqAMp0tQu/tyKwIk7wbkMMcDSxwbtxhHpFxrjF1kHBpt/j9wBaMV+LkEoUvIxlD/EBGFijNOX0nbkmB7/JOaA4ZQzKqvpc2IdTJMuCGAXg8MyOynWwZVos7rQSNlhCeRoIYArpHE6CMCdjwZ09IKlesyGiEDd1XNymwXLXuWtiqCqt6BwJoFLk6oyLduQfJOnUKsR4v8yiGyAFTyi7y+nHxDgEHQ=".encode().hex()
    print(re.__len__()%16)
    e = encrypt("hello world")  # 加密
    d = decrypt(e)  # 解密
    print("加密:", e)
    ba=str(base64.encodebytes(e), encoding='utf-8')
    print(ba)
    print(base64.b64decode(re).hex().__len__()%16)
    print(base64.b64decode(re).hex().encode().__len__()%16)
    print(base64.b64decode(re).__len__()%16)
    print(add_to_16(str(base64.b64decode(re).hex())).__len__()%16)
    print(base64.b64decode(re).hex().encode()[:-4].__len__()%16)
    print(re.__len__())
    print("解密:", d)