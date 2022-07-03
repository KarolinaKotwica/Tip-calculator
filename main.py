print('Welcome to tip calculator')
bill = input('What was the total bill? $')
tip = input('What percentage tip would you like to give? 10? 12? or 15? ')
people = input('What many people to split the bill? ')

bill = float(bill)
tip = int(tip)
people = int(people)

tips = (tip / 100) + 1

result = (bill / people) * tips
final_amount = round(result, 2)

print(f"Each person should pay: ${final_amount}")