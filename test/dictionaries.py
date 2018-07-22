ages = {"Alice": 22, "Bob": 27}
ages["Charlie"] = 30 +1
ages["Alice"] += 2

print(ages)

for key in ages:
    print(f"{key} is {ages[key]} years old.")
