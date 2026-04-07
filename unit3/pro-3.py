class Example:

    count = 0

    def __init__(self):
        Example.count += 1

    def instance_method(self):
        print("Instance Method Called")

    @classmethod
    def class_method(cls):
        print("Total Objects:", cls.count)

obj1 = Example()
obj2 = Example()

obj1.instance_method()
Example.class_method()
