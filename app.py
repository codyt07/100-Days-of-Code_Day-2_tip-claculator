# Dr. Yu's 100 days of Code Project 2, a tip calculator! 

print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? $"))
percentage_tip = float(input('''How much percentage tip you want to give? 10%, 12%, or 15%? '''))
split = float(input("How many people to split the bill? "))

# Final calculation
final_answer = ((total_bill * (percentage_tip / 100) + total_bill) / split)
answer = "{:.2f}".format(final_answer)
print(f'''Each person should pay: ${answer}''')
