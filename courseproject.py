print("===== HOTEL MANAGEMENT SYSTEM =====")

print("1. Book Room")
print("2. Check Room Price")
print("3. Check Out")
print("4. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    name = input("Enter customer name: ")
    days = int(input("Enter number of days: "))
    room_price = 1500
    total = days * room_price

    print("\nRoom booked successfully!")
    print("Customer Name:", name)
    print("Number of Days:", days)
    print("Room Price per Day: ₹", room_price)
    print("Total Bill: ₹", total)

elif choice == 2:
    print("Room Price per Day: ₹1500")

elif choice == 3:
    name = input("Enter customer name: ")
    print("Checkout completed successfully!")
    print("Thank you for staying with us,", name)

elif choice == 4:
    print("Thank you! Visit again.")

else:
    print("Invalid choice!")