my_purchase = {
    "R1_Pizza": {"count": 1, "cost": 1000},
    "R2_Pizza": {"count": 2, "cost": 2000},
}
amount =0

for key in my_purchase:
    count = my_purchase[key]['count']
    cost = my_purchase[key]['cost']
    amount+=count*cost
print(amount)