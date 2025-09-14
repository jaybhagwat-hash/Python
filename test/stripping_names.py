"""Store a person’s name, and include some whitespace 
characters at the beginning and end of the name . Make sure you use each 
character combination, "\t" and "\n", at least once .
 Print the name once, so the whitespace around the name is displayed . 
Then print the name using each of the three stripping functions, lstrip(), 
rstrip(), and strip()"""

def main():
    # Your code goes here
    name = '  John Doe  '
    print("Original String: '" + name + "'")
    print("After strip(): '" + name.strip() + "'")
    print("After lstrip(): '" + name.lstrip() + "'")
    print("After rstrip(): '" + name.rstrip() + "'")

if __name__ == "__main__":
    main()
