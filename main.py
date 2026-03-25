expense_list = []

print("====== WELCOME TO EXPENSE TRACKER ======")

while True:
    print("\n===== MENU =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Total Expense")
    print("4. Exit")

    # Safe input
    try:
        choice = int(input("\nEnter your choice: "))
    except:
        print(" Invalid input! Please enter a number.")
        continue

    # 1. Add Expense
    if choice == 1:
        date = input("Enter date: ")
        category = input("Enter category: ")
        description = input("Enter description: ")

        try:
            amount = float(input("Enter amount: "))
        except:
            print(" Invalid amount!")
            continue

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expense_list.append(expense)
        print("✅ Expense added successfully!")

    # 2. View Expenses
    elif choice == 2:
        if len(expense_list) == 0:
            print("⚠️ No expenses found!")
        else:
            print("\n====== EXPENSE LIST ======")
            count = 1
            for x in expense_list:
                print(f"{count}. {x['date']} | {x['category']} | {x['description']} | ₹{x['amount']}")
                count += 1

    # 3. Total Expense
    elif choice == 3:
        if len(expense_list) == 0:
            print("⚠️ No expenses to calculate!")
        else:
            total = 0
            for x in expense_list:
                total += x["amount"]

            print(f"\n Total Expense = ₹{total}")

    # 4. Exit
    elif choice == 4:
        print("\n Thank you for using Expense Tracker!")
        break

    else:
        print(" Enter a valid choice!")