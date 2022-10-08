def main():
    choice = int(input('''
1 - String to Ascii
2 - Ascii to String

9 - Quit

Choice: '''))

    if choice == 1:
        ToAscii()
    elif choice == 2:
        FromAscii()
    elif choice == 9:
        exit()
    else:
        print("That is not an option, please try again")
        main()

def ToAscii():
    string = input("String: ")
    asciistring = ""

    for letter in string:
        asciistring = asciistring + str(ord(letter)) + " "

    print(asciistring)
    main()

def FromAscii():
    cont = 1
    string = ""
    while cont == 1:
        x = int(input("Ascii Value (0 to stop): "))
        if x == 0:
            cont = 0
        else:
            string = string + str(chr(x))

    print(string)
    main()

main()
