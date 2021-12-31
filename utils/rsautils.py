import base64

import rsa


class HandleSign(object):
    # 定义服务器公钥, 往往可以存放在公钥文件中
    server_pub = """
        -----BEGIN PUBLIC KEY-----
        MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCsDrk3UmWEes2z2Es/ZoW7BLmGNQb/KV8cVzun7UuJCP8fQiYJD+URNnl+mhzOVDhWo8MHuETX+9FuhuqNXQXx0f+5UyyTUlA19ZBJJh4J45ZD0/mVcBLq4AcIe3rAvpHv1GKXNclvdZMBmhcTzUCqb+IxAjG3ANsjnLZijAiS0wIDAQAB
        -----END PUBLIC KEY-----
        """

    @classmethod
    def to_encrypt(cls, msg, pub_key=None):
        """
        非对称加密
        :param msg: 待加密字符串或者字节
        :param pub_key: 公钥
        :return: base64密文字符串
        """
        if isinstance(msg, str):            # 如果msg为字符串, 则转化为字节类型
            msg = msg.encode('utf-8')
        elif isinstance(msg, bytes):        # 如果msg为字节类型, 则无需处理
            pass
        else:                               # 否则抛出异常
            raise TypeError('msg必须为字符串或者字节类型!')

        if not pub_key:                     # 如果pub_key为空, 则使用全局公钥
            pub_key = cls.server_pub.encode("utf-8")
        elif isinstance(pub_key, str):      # 如果pub_key为字符串, 则转化为字节类型
            pub_key = pub_key.encode('utf-8')
        elif isinstance(pub_key, bytes):    # 如果msg为字节类型, 则无需处理
            pass
        else:                               # 否则抛出异常
            raise TypeError('pub_key必须为None、字符串或者字节类型!')

        public_key_obj = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key)  # 创建 PublicKey 对象

        cryto_msg = rsa.encrypt(msg, public_key_obj)  # 生成加密文本
        cipher_base64 = base64.b64encode(cryto_msg)   # 将加密文本转化为 base64 编码

        return cipher_base64.decode()   # 将字节类型的 base64 编码转化为字符串类型

if __name__ == '__main__':
    print(HandleSign.to_encrypt("dai@1234"))