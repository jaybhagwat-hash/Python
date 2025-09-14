def main() :
    name = input("Please enter your name.\n")
    print()
    print("In capital: " + str.upper(name))
    print("In Small: "+ str.lower(name))
    print("In TitleCase: " + str.title(name))

if __name__ == "__main__" :
    main()