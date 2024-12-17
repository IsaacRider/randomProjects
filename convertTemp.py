class Convert:
    def __init__(self):
        self.temp = 0
        self.type = ""
    def reset(self):
        self.temp = self.getTemp()
        self.type = self.getType()
    def branch(self):
        if self.type == "C" or self.type == "c":
            print("Temperature in Celsius: ")
            return self.ftoc(self.temp)
        elif self.type == "F" or self.type == "f":
            print("Temperature in Fahrenheit: ")
            return self.ctof(self.temp)
        else:
            print("Error: Invalid input!")
            return None
    def getTemp(self):
        while True:
            try:
                return float(input("Enter the temperature: "))
            except ValueError:
                print("Invalid Input")
    def getType(self):
        while True:
            type_input = input("Would you like that in F or C: ")
            if type_input.lower() in ['f', 'F', 'c', 'C']:
                return type_input
            else:
                print("Invalid Input")
    def ctof(self, tempInC):
        return round((tempInC * (9/5)) + 32, 2)
    def ftoc(self, tempInF):
        return round((tempInF - 32) * (5/9), 2)
    
def main():
    exit = "0"
    test = Convert()
    while(exit != "Q" and exit != "q"):
        test.reset()
        result = test.branch()
        if result is not None:
            print(result)
        exit = input("Type q to quit: ")

if __name__ == "__main__":
    main()