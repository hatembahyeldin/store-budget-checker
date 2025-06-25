item1_price = 25.0
item2_price = 40.0
item3_price = 15.0

budget = 100.0

total_cost = item1_price + item2_price + item3_price

if total_cost <= budget:
    money_left = budget - total_cost
    print(f"Total cost is ${total_cost:.2f}. You are within budget. Money left: ${money_left:.2f}.")
else:
    money_needed = total_cost - budget
    print(f"Total cost is ${total_cost:.2f}. You are over budget. You need ${money_needed:.2f} more.")