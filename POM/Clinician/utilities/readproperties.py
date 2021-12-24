import configparser

config = configparser.RawConfigParser()
configFilePath = r'C:\Users\oviya\Software\Python\Lib\__pycache__\configparser.cpython-310.pyc'
config.read("POM/Clinician/Configuration/config.ini")

class Readconfig:
    @staticmethod
    def getURL():
        url = config.get('common info', 'URL')
        return url
    @staticmethod
    def getemail():
        email = config.get('common info', 'email')
        print(email)
        return email


    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password
