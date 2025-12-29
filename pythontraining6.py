#exception handeling
try:
    x=50
    print(x)
except:
    print("except")
else:
    print("jhf")
finally:
    print("it will always execute")

#insufficient balance create 
"""try:
    x=1234
    c=50000
    y=int(input("Enter the pin: "))
    a=int(input("Enter the amount: "))
    if c>a: print(a)
except:
    print("ATM is under maintainance")
else:
    print("remove the card")
finally:
    print("thank you") """

correct_pin = 1190
balance = 2000
attempts = 3

while attempts > 0:
    try:
        entered_pin = int(input("Enter your PIN: "))

        if entered_pin == correct_pin:
            print("PIN verified")

            while True:
                print("\n1. Withdraw")
                print("2. Check Balance")
                print("3. Exit")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    amount = int(input("Enter amount to withdraw: "))

                    if amount <= 0:
                        print("Invalid amount")

                    elif amount > balance:
                        print("Insufficient balance")

                    else:
                        balance -= amount
                        print("Please collect your cash")
                        print("Remaining balance:", balance)

                elif choice == 2:
                    print("Your balance is:", balance)

                elif choice == 3:
                    print("Remove your card")
                    break

                else:
                    print("Invalid choice")

            break  # Exit after successful ATM session

        else:
            attempts -= 1
            print("Wrong PIN. Attempts left:", attempts)

    except ValueError:
        print("Invalid input. Enter numbers only")

else:
    print("ATM machine is blocked due to multiple wrong attempts")

print("Thank you for using our ATM")
