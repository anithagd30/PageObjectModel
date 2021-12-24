import configparser

config = configparser.RawConfigParser()
configFilePath = r'C:\Users\oviya\Software\Python\Lib\__pycache__\configparser.cpython-310.pyc'
config.read("https://github.com/anithagd30/PageObjectModel/blob/97e6313b5c2592fcc5abbfc12eb6a8965abe9941/POM/Clinician/Configuration/config.ini")

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
