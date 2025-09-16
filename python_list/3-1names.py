"""Store the names of a few of your friends in a list called names . Print 
each person’s name by accessing each element in the list, one at a time """

if __name__ == "__main__":
    names = ["Alice", 3.021, "Charlie", 2]
    names[2] = "Jay"
    names.append("Json")
    print(names.count("Alice"))
    #names.clear()
    print('names are: ' + str(names))
    names.insert(0, "Veer")
    print(names)
    del names[-1]
    print(names)