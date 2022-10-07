# fisrty we need to import math as adressed
import math

# user should be allowed to choose which calculation they want to do by using print out the options from the menu
print("Choose either 'investment' or 'bond' from the menu below to proceed: ")
print("investment - to calculate the amount of interest you'll earn on interest. ")
print("bond       - to calculate amount you have to pay on a home loan: ")

# variable choice is declared for the user to choose between bond and investment
choice = input()

# then a condition is created using an if statement if investment is chosen
# the below calculations will take place using the given equations
#User is required to input their choice
if choice.lower() == 'investment':
    p = float(input("Enter the amount of money you want to deposit : "))
    i = float(input("Enter the interest rate (do not add % symbol) : "))
    t = int(input("number of years money is being invested for: "))
    r = i/100

    # witthin the same if statement two more options are introduced to the
    # first main condition user needs to choose between simple or compound
    interest = input("Enter 'simple' or 'compound' interest : ")
    if interest.lower() == "simple":
        A = p*(1 + r * t)
        print(A, "is the amount: ")
    elif interest.lower() == "compound":
        A = p * math.pow((1 + r), t)
        print(A, "is the amount: ")
    else:
        print("Dear user, please kindly select the valid interest type")

# else if the user choses bond the calculation below will be excuted using equation provided 
# and the user is requeated to enter prensent value of the house,interest and number of mounths he/she plan to repay the bond
elif choice.lower() == 'bond':
    p = float(input("Enter the present value of the house: "))
    i = float(input("Enter The interest rate: "))
    n = float(input("Enter the number of months you plan to repay the bond: "))
    i = i/100
    i = i/12
    x = (i*p)/(1-(1+i)**(-n))
    print(f"You have to repay {round(x, 2)} each month")

# else if non of the above conditions are meet the statement below will be printed
else:
    print(f"choose only between investment and bond.")