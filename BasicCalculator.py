#Basic Calculator In Python..
print('===== Operation To Use =====')
print(' [1] ADDITION ')
print(' [2] SUBTRACTION')
print(' [3] DIVISION ')
print(' [4] MULTIPLICATION ')
print(' [0] EXIT THE APPLICATION')

print('_______________________________')

OperationChoice = input(' Operation Choice: ')
print('_______________________________')
    
if  OperationChoice == '1':# addition
     print('======= ADDITION =======')
     FirstNum =  int(input(' Enter First Number: '))
     SecondNum = int(input(' Enter Second Number: '))
     Sum = (FirstNum + SecondNum)
     print(' The Sum Of', FirstNum ,'&', SecondNum,'is',Sum)
     print('_______________________________')
     print()
     
elif OperationChoice == '2': #division
     print('======= SUBTRACTION =======')
     FirstNum =  int(input(' Enter First Number: '))
     SecondNum = int(input(' Enter Second Number: '))
     Difference = (FirstNum - SecondNum)
     print(' The Difference Of', FirstNum ,'&', SecondNum,'is', Difference)
     print('_______________________________')
     print()
     
elif OperationChoice == '3':#Subtraction
    print('======= DIVISION =======')
    FirstNum =  int(input(' Enter First Number: '))
    SecondNum = int(input(' Enter Second Number: '))
    Quotient = (FirstNum / SecondNum)
    print(' The Quotient Of', FirstNum ,'&', SecondNum,'is', Quotient)
    print('_______________________________')
    print()
     
elif OperationChoice == '4':#multiplication
     print('======= MULTIPLICATION =======')
     FirstNum =  int(input(' Enter First Number: '))
     SecondNum = int(input(' Enter Second Number: '))
     Product = (FirstNum * SecondNum)
     print(' The Product Of', FirstNum ,'&', SecondNum,'is', Product)
     print('_______________________________')
     print()
     
elif OperationChoice == '0':#exiting the application.
     print('Exiting application..')
     print('Done..')

else:
      print('invalid')


