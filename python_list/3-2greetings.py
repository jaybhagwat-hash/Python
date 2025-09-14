""" Start with the list you used in Exercise 3-1, but instead of just 
printing each person’s name, print a message to them . The text of each mes
sage should be the same, but each message should be personalized with the 
person’s name """

if __name__ == "__main__":
    names = ["Alice", "Bob", "Charlie", "Diana"]
    for name in names:
        print(f"Hello {name}, hope you're having a great day!") 