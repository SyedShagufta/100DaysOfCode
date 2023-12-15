# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# If we want to pay 12% as the tip, it means  we're paying 0.12*(bill amount) more
#
# So it effectively means, what you're paying is bill amount + 0.12*(bill amount)
#
# Taking bill amount common (in mathematical terms, which you do in high school), your  total pay = (bill amount) * (
# 1 + 0.12) = (bill amount)*1.12
#
#
# Now this total pay is to be divided amongst the people in the party
#
# So if there were 5 people, bill amount was 150.00, 12% tip
#
# we'll split the total pay, which is 150.00*1.12, amongst 5, = 150.00*1.12/5

# Write your code below this line 👇

# print the greetings
print("Welcome to the Tip Calculator.")

# take the inputs
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))


# define the function
def calculate_tip(total_bill, percentage, no_of_people):
    tip = (total_bill / no_of_people) * (1 + percentage / 100)
    return tip


# from math import pi  # pi ~ 3.141592653589793
# >>> '{0:.2f}'.format(pi)
# '3.14'
result = "{0:.2f}".format(calculate_tip(total_bill, percentage, no_of_people))
# print result
print(f"Each person should pay: ${result}")
