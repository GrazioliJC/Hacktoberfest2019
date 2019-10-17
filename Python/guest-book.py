filename = 'guests.txt'

with open(filename, 'w') as f:
    f.write("Guest List:")
    while True:
        n = input("Insert your name (quit for exit): ")
        if n == "quit":
            f.close()
            break
        f.write("\n" + n)
        print("Hello " + n + ", you have been added!")
