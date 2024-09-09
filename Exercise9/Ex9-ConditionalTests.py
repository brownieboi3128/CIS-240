#Christian Brown

def printApplePrices():
    # Open the text file
    with open("Apples.txt", "r") as apples:
        #create a for loop to read over each line and remove the newline character
        for line in apples:
            line = line.strip()
            if line == "Honeycrisp" or line == "Empire" or line == "Fuji":
                price = "$2.00"
            else:
                price = "$1.00"
            print(line, price)

#call the function  
printApplePrices()