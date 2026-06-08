# Python by Example: CSV Files

CSV (comma-separated values) is a plain-text format for tabular data. Python's `csv` module handles quoting and escaping automatically. Use `csv.writer` and `csv.reader` for row-based access; use `csv.DictReader` when you want named fields.

**What you'll learn:**
- Writing rows with `csv.writer`
- Reading rows with `csv.reader`
- Named-field access with `csv.DictReader`

```python
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
```

Pass `newline=""` when opening for writing—the `csv` module handles its own line endings. All values come back as strings when reading; convert them explicitly if you need numbers.

To run this program:

```bash
$ python source/csv-files.py
['name', 'age', 'city']
['Alice', '30', 'New York']
['Bob', '25', 'London']
['Carol', '35', 'Tokyo']
Alice 30
Bob 25
Carol 35
```

**Tip:** For tab-separated files, pass `delimiter="\t"` to `csv.writer` and `csv.reader`.

**Try it:** Read the CSV back and print only the people older than 28.

Source: [csv-files.py](../source/csv-files.py)

Next: [Time](time.md)
