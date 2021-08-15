import csv
from models import *


"""
id, title = categories
id, title, price, description, picture, category_id = meals
"""


with open('categories.csv', encoding="UTF8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', )
    next(csv_reader) #skip first row with header
    for row in csv_reader:
        # print(row[0], row[1])
        category = Category(
            title = row[1]
        )
        db.session.add(category)
    db.session.commit()    


with open('meals.csv', encoding="UTF8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', )
    next(csv_reader) #skip first row with header
    for row in csv_reader:
        print(row[0], row[1], row[2], row[3], row[4], row[5])
        dish = Dish(
            title = row[1],
            price = row[1],
            description = row[1],
            picture = row[1],
        )
        db.session.add(dish)
    db.session.commit()   