def shopchange():
    price=float(input("Hello! Please enter price:"))
    tender=float(input("Hello! Please enter amount tendered:"))
    print(round(tender-price*1.07,2))
    end=input('Thank you!\n type "exit" to quit, or press enter to continue')
    if end.lower() == "exit":
        exit()

def main():
    while True:
        shopchange()

main()
