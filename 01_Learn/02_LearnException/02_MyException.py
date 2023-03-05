class NameError(Exception):
    def __init__(self, message):
        self.message = message

    @property
    def msn(self):
        return f"名字中不能有{self.message}"


name = 'Tom'
try:
    if name == 'Tom':
        raise NameError(name)
except NameError as ne:
    print(ne.msn)
