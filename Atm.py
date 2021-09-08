class ATM: 
    def _init_(self,cardnumber,pin)
        self.cardnumber = number
        self.pin = pin

    def check_balance(self):
         print("Your Balance Is 1,000,000")
     
    def withdrawl(self,amount):
         new_amount = 1,000,000 - amount
         print("you have withdrawn amount"+str(amount)+". Your Remaining Balance is "+ str (new_amount))
        
        
def main():
            Card_number = input("insert your card number:- ")
            pin_number = input("insert your card number:-")

            new_user = Atm(Card_number,pin_number)

            print("Choose your Activity")
            print("1.Balance Enquiry  2.withdrawal")
            activity = int(input("enter activity number:-"))

            if (activity == 1):
                new_user.check_balance()
                elif (activity ==2):
                    amount=int(input("enter the amount:-"))
                    new_user.withdrawal(amount)
                    else:
                        print("enter a valid number")



if_name_ == "_main_":
    main()            

  