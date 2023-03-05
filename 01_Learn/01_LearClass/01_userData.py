'''
@property 装饰器可以将一个方法转化为属性，使得在访问这个属性时可以像访问普通属性一样，而不需要通过调用方法来获取属性值。

在这个例子中，@property 装饰器将方法 func 转化为属性 func，当访问该属性时，会调用 func 方法，返回实例的私有变量 __varName。

@property 装饰器还定义了一个与该属性关联的 setter 方法，它使用 @func.setter 装饰器来实现。setter 方法接受一个参数 varValue，将它赋值给实例的私有变量 __varName。

在这段代码中，我们创建了一个 Klass3 类的实例 obj，并将属性 func 的值设置为 '123'。这会调用 func.setter 方法，将 '123' 赋值给 __varName。

最后，我们打印了 obj.func 属性的值，这会调用 func 方法，返回 __varName 的值，也就是 '123'。
'''


class Klass3:
    @property
    def func(self):
        return self.__varName
    
    @func.setter
    def func(self, varValue):
        self.__varName = varValue


obj = Klass3()
obj.func = '123'
print(obj.func)
