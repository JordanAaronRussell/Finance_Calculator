import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

choice = (input("Enter either 'investment' or 'bond' from the menu above to proceed: ")).lower()

if choice == "investment": 

    money_invested = float(input("Enter how much money you want to invest: "))
    interest_rate = float(input("Enter the interest rate as a percent out of 100: "))
    years = float(input("Enter how many years you will invest: "))

    interest_type = (input("Please choose either 'simple' or 'compound' interest: ")).lower()

    if interest_type == "simple":
        total_amount = money_invested * (1 + (interest_rate/100) * years)
        print(f"The total amount returned is {total_amount}.")
    elif interest_type == "compound":
        total_amount = money_invested * math.pow((1 + interest_rate/100), years)
        print(f"The total amount returned is {total_amount}.")
    else:
        print("Not a valid option. Please try again.")

elif choice == "bond":

    house_value = float(input("Enter the value of the house: "))
    annual_interest_rate = float(input("Enter the annual interest rate as a percent out of 100: "))
    months = float(input("Enter how many months you intend to take to pay the bond: "))

    monthly_repayment = (annual_interest_rate/100/12 * house_value)/(1 - (1 + annual_interest_rate/100/12)**(-months))
    print(f"The monthly repayment amount is {monthly_repayment}")

else: 
    print("That's not a valid option. Please try again.")




