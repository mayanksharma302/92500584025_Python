class Temperature:
    def convertFarenheit(self, c):
        f = (c * 9/5) + 32
        print("Fahrenheit:", f)
    def convertCelsius(self, f):
        c = (f - 32) * 5/9
        print("Celsius:", c)
t = Temperature()
t.convertFarenheit(30)
t.convertCelsius(86)
