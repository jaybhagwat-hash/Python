import test.maths as maths

def main() :
    val1 = int(input("enter first value"))
    val2 = int(input("enter second value"))
    print()
    operation = input("Type on of the following:  \n\t\t add\n\t\t sub\n\t\t mult\n\t\t div\n")
    operation_value = {
        'add' : maths.add,
        'sub' : maths.sub,
        'mult' : maths.mult,
        'div' : maths.div
     }
    
    function_to_call = operation_value[operation]

    print("The output of " + operation + " " + str(function_to_call(val1, val2)))

if __name__ == '__main__' :
    main()