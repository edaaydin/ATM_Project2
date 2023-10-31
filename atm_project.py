import time
balanceOfAhmet = 0
balanceOfZeynep = 0
usernameOfAhmet = "Ahmet"
usernameOfZeynep = "Zeynep"
passwordOfAhmet = "1234"
passwordOfZeynep = "4321"
username = ""
password = None

def checkUsernameAndPassword (username, password): # kullanici adi ve sifreyi sorgulama
    if(str(username) == usernameOfAhmet):
        if(password == passwordOfAhmet):
            return usernameOfAhmet
        else:
            print("Wrong credentials!!!!")
            return False
    elif(str(username) == usernameOfZeynep):
        if(password == passwordOfZeynep):
            return usernameOfZeynep
        else:
            print("Wrong credentials!!!!")
            return False
    else:
        print("Wrong credentials!!!!")
        return False

def userMenu(username):
    return input \
        ("Welcome " + username + "!\nPlease enter the number of the service:\n1. Withdraw Money\n2. Deposit Money\n3. Transfer Money\n4. My Account Information\n5. Logout")
        # yapacaginiz islemleri seciniz.
def withdrawMoney(username, withdraw):
    global balanceOfAhmet
    global balanceOfZeynep
    if(str(username) == usernameOfAhmet):
        if(balanceOfAhmet < int(withdraw)):
            print("You don't have " + withdraw + " TL in your account\nGoing back to main menu...")
        else:
            balanceOfAhmet = balanceOfAhmet - int(withdraw)
            print(withdraw + " TL withdrawn from your account\nGoing back to main menu...")
    elif(str(username) == usernameOfZeynep):
        if(balanceOfZeynep < int(withdraw)):
            print("You don't have " + withdraw + " TL in your account\nGoing back to main menu...")
        else:
            balanceOfZeynep = balanceOfZeynep - int(withdraw)
            print(withdraw + " TL withdrawn from your account\nGoing back to main menu...")

def depositMoney(username, withdraw):
    global balanceOfAhmet
    global balanceOfZeynep
    if(username == usernameOfAhmet):
        balanceOfAhmet = balanceOfAhmet + int(withdraw)
        print(withdraw + " TL added to your account\nGoing back to main menu...")
    elif(username == usernameOfZeynep):
        balanceOfZeynep = balanceOfZeynep + int(withdraw)
        print(withdraw + " TL added to your account\nGoing back to main menu...")

def transferMoney(username, transfer):
    global balanceOfAhmet
    global balanceOfZeynep
    if(username == usernameOfAhmet):
        if(balanceOfAhmet < int(transfer)):
            return input \
                ("Sorry! You don't have enough money to complete this transaction\n1. Going back to main menu...\n2. Transfer again")
        else:
            balanceOfZeynep = balanceOfZeynep + int(transfer)
            balanceOfAhmet = balanceOfAhmet - int(transfer)
            return input \
                (transfer + " TL transffered from your account\n\n1. Going back to main menu...\n2. Transfer again")
    elif(username == usernameOfZeynep):
        if(balanceOfZeynep < int(transfer)):
            return input \
                ("Sorry! You don't have enough money to complete this transaction\n1. Going back to main menu...\n2. Transfer again")
        else:
            print(balanceOfZeynep)
            balanceOfAhmet = balanceOfAhmet + int(transfer)
            balanceOfZeynep = balanceOfZeynep - int(transfer)
            print(balanceOfZeynep)
            return input \
                (transfer + " TL transffered frodddm your account\n\n1. Going back to main menu...\n2. Transfer again")

def userMenuSelection(userIslem, username, password):
    if(userIslem == "1"):
        withdraw = input("Please enter the amount you want to withdraw:")
        withdrawMoney(username, withdraw)
    if(userIslem == "2"):
        deposit = input("Please enter the amount you want to drop:")
        depositMoney(username, deposit)
    if(userIslem == "3"):
        while True:
            transfer = input("Please enter the amount you want to transfer:")
            if(transferMoney(username, transfer) == "1"):
                break
    if(userIslem == "4"):
        t = time.localtime()
        print("--İSTİNYE Bank--\n--" + time.asctime
            (t) + "--\n" + "Your Name: " + username + "\nYour Password: " + password)
        if(username == usernameOfAhmet):
            print("Your Amount(TL): " + str(balanceOfAhmet))
        else:
            print("Your Amount(TL): " + str(balanceOfZeynep))

while True:
    print("— Welcome to İSTİNYE Bank —\n1. Login\n2. Exit") #istinye banka girmek icin 1 e cikis yapmak icin 2 ye basinşiz
    islem = input()
    if(islem == "2"):
        break
    if(islem == "1"):
        username = input("User Name:")
        password = input("Password:")
        checkUser = checkUsernameAndPassword(username, password)
        if(checkUser) != False:
            if(checkUser) == usernameOfAhmet:
                while True:
                    userIslem = userMenu(username)
                    if(userIslem == "5"):
                        break
                    userMenuSelection(userIslem, username, password)

            elif(str(checkUser) == usernameOfZeynep):
                while True:
                    userIslem = userMenu(username)
                    if(userIslem == "5"):
                        break
                    userMenuSelection(userIslem, username, password)
