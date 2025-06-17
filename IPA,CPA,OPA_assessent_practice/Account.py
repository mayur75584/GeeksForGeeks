'''
For question go to folder of 
IPA sample questions - Question 3



Sample Input1-
120
Rajesh
1500

1200
2000

Sample Output1-
2700
Insufficient balance for withdrawal

Sample Input2-
150
Mayur
3000

1200
800

Sample Output2-
4200
Balance after withdrawl : 3400
'''
class Account:

    def __init__(self,account_no,account_name,account_balance):
        self.account_no = account_no
        self.account_name = account_name
        self.account_balance = account_balance

    def depositAmnt(self,depamnt):
        self.account_balance+=depamnt

    def withdrawAmnt(self,withamnt):
        if(self.account_balance-withamnt<1000):
            return False
        else:
            self.account_balance-=withamnt

        return True





if __name__ == '__main__':
    # list_obj=[] #Here no need to create list for objects as single objects are used
    account_no = int(input())
    account_name = input()
    account_balance = int(input())

    # list_obj.append(Account(account_no,account_name,account_balance))
    depamnt=int(input())
    withamnt=int(input())

    obj=Account(account_no,account_name,account_balance)
    obj.depositAmnt(depamnt)
    print(obj.account_balance)

    res=obj.withdrawAmnt(withamnt)
    if res==True:
        print("Balance after withdrawl :",obj.account_balance)
    else:
        print("Insufficient balance for withdrawal")




