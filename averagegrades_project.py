# pedro bakare, average grades project
period_1 = input("enter grade for programming: " )
period_2 = input("enter grade for biology: ")
period_3 = input("enter grade for geography: ")
period_4 = input("enter grade for advisory: ")
period_5 = input("enter grade for english: ")
period_6 = input("enter grade for drawing: ")
period_7 = input("enter grade for math: ")

total= period_1 + period_2 + period_3 + period_4 + period_5 + period_6 + period_7
average = total / 7

print(f"your average grade for all 7 periods is {average:.2f}")