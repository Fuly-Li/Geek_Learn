'''
请你编写自定义异常类，
如果读取的文件小于 10 个字符，抛出文件过小的自定义异常，
如果读取的文件大于等于 10 个字符，则正常输出该文件内容
'''


class NumError(Exception):
    def __init__(self, filename, num):
        self.filename = filename
        self.num = num

    @property
    def msn(self):
        return f"文件{self.filename}中的字符数为:{self.num},小于 10 个字符限制"


file = "userData.txt"
with open(file, 'r') as f:
    file_read = f.read()
    # 获取文件中字符数量
    file_len = len(file_read)
    try:
        if file_len >= 10:
            print(file_read)
        else:
            raise NumError(file, file_len)
    except NumError as e:
        print(e.msn)
