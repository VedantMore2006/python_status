import csv

data = [
    ['Name', 'Age', 'Country'],
    ['Vedant', '19', 'India'],
    ['Nakul', '20', 'India']
]

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)