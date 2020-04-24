import hashlib, base64
class UserService():
    @staticmethod
    def generatePwd(pwd,salt):
        m = hashlib.md5()
        str = "%s-%s"%(base64.encodebytes(pwd.encode('utf-8')))
        m.update(str.encode('utf-8'))
        return m.hexdigest()