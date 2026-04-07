class Outer:
    class Inner:
        def show(self):
            print("Inner class method")
o = Outer()
i = o.Inner()
i.show()
