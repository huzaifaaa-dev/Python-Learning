amountdue = 50
while amountdue > 0:
    insertcoin = int(input("Insert Coin: "))
    if insertcoin == 10 or insertcoin == 25 or insertcoin == 50:
        amountdue = amountdue - insertcoin
        print("Amount Due: ", amountdue)
if amountdue < 0:
    print("Change due: ", amountdue * -1)