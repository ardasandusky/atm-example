user1acc = {
    'name': 'Arda Erdoğan',
    'accNo': '18500',
    'balance': 4000,
    'addBalance': 2500
}

user2acc = {
    'name': 'Tuba Saridji',
    'accNo': '9000',
    'balance': 3000,
    'addBalance': 160
}


def withdrawal(account, balance):
    print(f"Hello, {account['name']}")

    if account['balance'] >= balance:
        account['balance'] -= balance
        print("You can take your money.")
    else:
        total = account['balance'] + account['addBalance']

        if total >= balance:
            addBalanceUsage = input("Do you want to use additional accounts?(y/n)")

            if addBalanceUsage == "e":

                amountSpent = account - balance
                account['balance'] = 0
                hesap['addBalance'] -= amountSpent
                print("You can take your money.")
            else:
                print(f"{account['balance']} balance in your account numbered {account['accNo']}.")
        else:
            print("Sorry, transaction denied.")


withdrawal(user2acc, 300)
