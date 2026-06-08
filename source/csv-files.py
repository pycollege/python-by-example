import csv


with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "city"])
    writer.writerows([
        ["Alice", 30, "New York"],
        ["Bob", 25, "London"],
        ["Carol", 35, "Tokyo"],
    ])


with open("people.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# DictReader maps each row to a dict using the header
with open("people.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])
