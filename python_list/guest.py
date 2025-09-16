if __name__ == "__main__" :
    guests = ["Saurabh", "Anuli", "Swati"]
    print( "Hi " + str(guests) + " welcome to dinner\n" )
    print('Due to unexpected reasons ' + str(guests[0]) + ' can not make it to dinner\n')
    pop_guest = guests.pop(0)
    guests.insert(0, "Veer")
    print('Now instead of ' + pop_guest + ' we have ' + guests[0])
    print( "Hi " + str(guests) + " welcome to dinner\n" )
    print("We found a bigger dinner table\n")
    guests.insert(0, "Prajwal")
    guests.insert(2, "Achyut")
    guests.append("Shambhavi")
    print( "Hi " + str(guests) + " welcome to dinner\n" )
    print("Sorry we can only invite 4 people for dinner\n")
    pop_guest = guests.pop()
    print("Sorry " + pop_guest + " we can't invite you to dinner")
    pop_guest = guests.pop(0)
    print("Sorry " + pop_guest + " we can't invite you to dinner")
    print("Hi " + str(guests) + " you are still invited")
    del guests[0]
    del guests[0]
    del guests[0]
    del guests[0]
    print(guests)
