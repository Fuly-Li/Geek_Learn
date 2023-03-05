"""
定义一个类，类中的属性 userData 可以将属性的值保存到文件中，该属性的行为如下：
1.对属性赋值时，该值自动保存到文件 userData.txt 中。
2.读取属性值时，如果该属性为空，那么就从文件 userData 中读取并在终端显示该属性值
"""
class UserData:
    def __init__(self):
        self.__userData = None

    @property
    def userData(self):
        if self.__userData is None:
            self.__userData = self.__loadData()
        return self.__userData

    @userData.setter
    def userData(self, value):
        self.__userData = value
        self.__saveData()

    def __loadData(self):
        try:
            with open('userData.txt', 'r') as f:
                return f.read()
        except FileNotFoundError:
            return ''

    def __saveData(self):
        with open("userData.txt", 'w') as f:
            f.write(self.__userData)


user_data = UserData()

print(user_data.userData)# 从文件中读取数据并显示

user_data.userData='你好'# 保存到文件中
print(user_data.userData)# 从文件中读取数据并显示
