# first OOPs project
# bike rentel service using OOPs concept 


class bike(): #defining a class name bike
    def __init__(self, bikename, com_name):
        self.bike = bikename
        self.name = com_name
        self.test = {}

    # def __str__(self):
    #     return f"This is name and its connected to class"

    def display(self):
        '''use this method to display your bikes name''' #this is doc string
        models = len(self.bike)
        print(f'we have only {models} models available for now')
        id = 1
        for bikes in self.bike:
            print(id, bikes)
            id += 1

    def test_ride(self, bikename, user):
        '''take 3 parameter 2 are additioal and 1 is automatic 
           take username and bikename'''

        if bike not in self.test.keys():
            self.test.update({bike: user})
            print("your bike has been booked for test ride.")
            del self.bike[userbike-1]

        elif user in self.test.values():
            print(
                f"sir that is not available for now ")

        else:
            print(
                f"sorry sir !! this bike is already booked by {self.test[bike]}")

if __name__ == '__main__':

    kawasaki_bikes = ["z900", "z650", "zx10r", "z800", "z6r"]
    hayabusa_bikes = ["hayabusa", "gz100", "katana1000", "hayabusa turbo", ]

    brand1 = bike(kawasaki_bikes, "kawasaki motors")
    brand2 = bike(hayabusa_bikes, "hayabusa motors")

    # print(brand1)

    print("which showroom do you want to go")
    print("1.kawasaki")
    print("2.hayabusa")
    userchoice = int(input("enter :"))

    if userchoice == 1:
        com1 = brand1
        lst = kawasaki_bikes

    else:
        com1 = brand2
        lst = hayabusa_bikes

    # com1.test_ride("z900","vishal")
    # com1.test_ride("z900","yadav")

    while True:
        print(f"\t\t\t\t\twelcome to {com1.name}")
        print("1. display bikes")
        print("2. book test ride")
        print("3. exit ")
        # print(len(lst)) for testing something

        try:
            ipt = int(input("enter your choice : "))

            if ipt == 1:
                print(f"you selected option {ipt} to display bikes")
                com1.display()

            elif ipt == 2:
                print(f"you selected option {ipt} to book test rides")
                com1.display()
                userbike = int(input("select your bike:"))
                if userbike >= len(lst):
                    print("enter valid option")
                else:
                    userself = input("enter your name:")
                    com1.test_ride(userbike, userself)

            elif ipt == 3:
                print("Thank you, program is terminated ")
                exit()

            else:
                print("enter a valid option")

        except Exception as e:
            print("error enter a number between 1 to 3 as instruction")
