from cardholder import cardholder

def print_menu():
    print('Please choose an option...')
    print('1.Deposit')
    print('2.Withdraw')
    print('3.Show Balance')
    print('4.Transaction History')
    print('5.Exit')

def deposit(cardholder):
    try:
        deposit=float(input('How much money do you want to deposit ?'))
        cardholder.set_balance(cardholder.get_balance()+deposit)
        print('Thank you for your money. Your new balance is:',str(cardholder.get_balance()))
    except:
        print('Invalid input')
    #current_user.transaction_history.append(deposit)

def withdraw(cardholder):
    try:
        withdraw=float(input('How much money do you want to withdraw ?'))
        if (cardholder.get_balance()) < withdraw:
            print('Sorry, Insufficient balance.')
        else:
            cardholder.set_balance(cardholder.get_balance()-(withdraw))
            print('Thank you. Your new balance is:',str(cardholder.get_balance()))
    except:
        print('Invalid input')

    #current_user.transaction_history.append(withdraw)

def show_balance(cardholder):
    print('Your current balance is:',cardholder.get_balance())


if __name__=='__main__':
    current_user=cardholder('','','','','')

    ###creation of a repository of cardholders
    #DATABASE
    list_of_cardholders=[]
    list_of_cardholders.append(cardholder('3874627902872987',4567,'Sam','Smith',100000))
    list_of_cardholders.append(cardholder('1234567891011121',1234,'Bob','Marley',200000))
    list_of_cardholders.append(cardholder('1234432112344321',1234,'Harley','Quinn',9000000))
    list_of_cardholders.append(cardholder('8888777766665555',4321,'Raisa','Jahan',100000))
    list_of_cardholders.append(cardholder('9999888877776666',1234,'Ahmed','Sakib',100000))
                               
                               
    debitCardNum=''
    while True:
        try:
            debitCardNum=input('Please enter your debit card number :')
            #check against the repository
            crosscheck=[holder for holder in list_of_cardholders if holder.cardnumber==debitCardNum]
            if len(crosscheck)>0:
                current_user=crosscheck[0]
                break
            else:
                print('Card number not recognized please try again')
        except:
            print('Card number  not recognized please try again')


    #PIN PROMPT
    while True:
        try:
            upin=int(input('Please enter PIN:').strip())
            if current_user.get_pin()==upin:
                break
            else:
                print('Invalid choice try again...')

        except:
            print('Invalid choice,try again...')


##print options
    print('Welcome',current_user.get_firstname(),':)')
    option=0
    while True:
        print_menu()
        try:
            option=int(input())
        except:
            print('Invalid choice,please try again...')

        if option==1:
            deposit(current_user)
        elif option==2:
            withdraw(current_user)
        elif option==3:
            show_balance(current_user)
        elif option==4:
            for i in current_user.transaction_history():
                print(i)
        else:
            break
    print('THANK YOU! COME AGAIN')



