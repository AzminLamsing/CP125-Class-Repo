def withdraw(accounts, card_number, amount):
    for card_number,balance in (accounts) :
        if card_number in accounts[item] :
            total_balance = accounts[balance] - amount 
            
            if total_balance > 0 :
                return total_balance
            else : 
                return f"Insufficient Funds"
            
        else :
            return f"Card Not Found"





accounts = {
    "4111-1111": 500.00,
    "4222-2222": 80.00,
}
print(withdraw(accounts, "4111-1111", 200.00))
print(withdraw(accounts, "4222-2222", 100.00))
print(withdraw(accounts, "9999-0000", 50.00))
