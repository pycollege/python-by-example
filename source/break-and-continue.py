# break: exit loop when condition is met
for i in range(5):
    if i == 3:
        break
    print(i)
print("done with break")

# continue: skip current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)
print("done with continue")
