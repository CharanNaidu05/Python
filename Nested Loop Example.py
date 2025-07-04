rows = int(input("Enter the Number Of rows: "))
columns = int(input("Enter the Number Of columns: "))
symbol = input("Enter a Symbol to Use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()    