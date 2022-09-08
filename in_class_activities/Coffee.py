class drink:

    def __init__(self, name, calories, caffeine):
        self.name = name
        self.calories = calories
        self.caffiene = caffeine

    def get_name(self):
        print(self.name)

    def get_calories(self):
        print(self.calories)

    def get_caffiene(self):
        print(self.caffiene)

    def set_calories(self, calories):
        self.calories = calories

    def set_caffiene(self, caffiene):
        self.caffiene = caffiene

    def set_name(self, name):
        self.name = name

class coffee(drink):

    def __init__(self, name, calories, caffeine, lactose):
        super().__init__(name, calories, caffeine)
        self.lactose = lactose

class condiments:

    def __init__(self, name):
        self.name = name

def main():

    brewing = 'yes'
    drink = drink()
    coffee = coffee()
    
    while brewing == 'yes':
        drink_pref = input("What would you like to drink? (press n to stop")
        if drink_pref == 'n':
            brewing = 'no'
            break
        elif drink_pref.lower() == 'espresso':





main()

