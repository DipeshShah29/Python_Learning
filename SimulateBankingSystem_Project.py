from random import randint
import pandas as pd


class bank:
    # accountDetails_dict = {}
    accountDetails_df = pd.DataFrame(
        columns=["Cust_Acc_Number", "Cust_Name", "Cust_Balance"]
    )

    def __init__(self):
        # self.accountDetails_dict={}
        pass

    def generateAccountNumber(self):
        return randint((10 ** 4), ((10 ** 5) - 1))

    def showBalance(self, accountNumber):
        # balance = self.accountDetails_df['Cust_Balance'].where(self.accountDetails_df['Cust_Acc_Number'] == accountNumber)
        balance = self.accountDetails_df.loc[
            self.accountDetails_df["Cust_Acc_Number"] == accountNumber, "Cust_Balance"
        ]

        return balance

    def createAccount(self):
        print("Please enter your name you want to open your saving account with")
        name = input()
        if len(name) == 0:
            print("Please enter valid name")
        else:
            accountNumber = bank.generateAccountNumber()
            print("Welcome", name, "!")
            print("Your account number is", accountNumber)
            print("Please deposit some amount in your account")
            amount = int(input())
            if type(amount) == int:
                self.accountDetails_df = self.accountDetails_df.append(
                    {
                        "Cust_Acc_Number": accountNumber,
                        "Cust_Name": name,
                        "Cust_Balance": amount,
                    },
                    ignore_index=True,
                )
                print(self.accountDetails_df)
                print(type(self.accountDetails_df))
            else:
                print("Please enter valid amount")

    def aunthenticateUser(self):

        print("Welcome to 2 way Authentication")
        inputName = input("Verify your name")

        if len(inputName) == 0:
            print("Please enter valid name")
        else:
            inputNumber = int(input("Verify your account number"))
            Name = self.accountDetails_df.loc[
                self.accountDetails_df["Cust_Name"] == inputName, "Cust_Name"
            ]
            Number = self.accountDetails_df.loc[
                self.accountDetails_df["Cust_Acc_Number"] == inputNumber,
                "Cust_Acc_Number",
            ]

            # cust_Name = Name[0]
            # cust_Acc_Number = Number[0]

            if len(Name) != 0 and len(Number) != 0:
                print("You have succesully logged in to your account")
                print("Press 1 to withdraw money")
                print("Press 2 to deposit money")
                print("Press 3 to check your balance")
                print("Press 0 to exit")
                optionSelected = int(input())
                if optionSelected == 1:
                    bank.withdrawMoney(inputNumber)
                elif optionSelected == 2:
                    bank.depositMoney(inputNumber)
                elif optionSelected == 3:
                    balance = self.showBalance(inputNumber)
                    print("Your balance is", balance[0])
                elif optionSelected == 0:
                    quit()

            else:
                print("Sorry, invalid aunthentication. Please try again.")

    def withdrawMoney(self, accountNumber):
        print("Enter the amount you want to withdraw")
        amount = int(input())

        if type(amount) == int:
            try:
                self.accountDetails_df["Cust_Balance"] = (
                    self.accountDetails_df["Cust_Balance"].where(
                        self.accountDetails_df["Cust_Acc_Number"] == accountNumber
                    )
                    - amount
                )
                print(
                    "The amount {0} is successully whithdrawn and your balance is {1}".format(
                        amount, self.showBalance(accountNumber)
                    )
                )
            except:
                print("Sorry, error occured in the operation. Please try again")

                # bank.showBalance(accountNumber)

        else:
            print("Please enter valid amount")

    def depositMoney(self, accountNumber):
        print("Enter the amount you want to deposit")
        inputAmount = int(input())

        if type(inputAmount) == int:
            try:
                self.accountDetails_df["Cust_Balance"] = (
                    self.accountDetails_df["Cust_Balance"].where(
                        self.accountDetails_df["Cust_Acc_Number"] == accountNumber
                    )
                    + inputAmount
                )
                print(
                    "The amount {0} is successfully deposited in your account {1} and your balance is {2}".format(
                        inputAmount, accountNumber, self.showBalance(accountNumber)
                    )
                )

            finally:
                pass
            # except Exception as e:
            #   print(e.__class__)

        else:
            print("Please enter the valid amount")

    def get_user(self):
        pass

    def set_user(self):
        pass


bank = bank()

while True:

    print("Welcome to ABC Bank")
    print("Select option to continue your operation with the bank")
    print("------------------------------------------------------")
    print("Press 1 open a saving account")
    print("Press 2 to access your existing saving account")
    print("Press 0 to exit")
    optionSelected = int(input())
    if optionSelected == 1:
        bank.createAccount()
    elif optionSelected == 2:
        bank.aunthenticateUser()
    elif optionSelected == 0:
        quit()
