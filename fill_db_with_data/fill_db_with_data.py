"""Use this file to first fill database with prepared data from csv files."""

import sys
import os
import csv


#to import module "models.py" from parent dir
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
if parent not in sys.path:
    sys.path.append(parent)


from models import *
from app import *


with app.app_context():
    categories = db.session.query(Category).all()
    if categories is None:
        categories_data_path = os.path.join(current, "categories.csv")
        with open(categories_data_path, encoding="UTF8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            next(csv_reader) #skip first row with header

            for row in csv_reader:
                print(row[1])
                new_category = Category(title=row[1])
                db.session.add(new_category)
            db.session.commit()    

            print(">>>Categories -----> done")
    else:
        print("Category table is not empty")

    categories = db.session.query(Category).all()
    if categories is None:
        dishes_data_path = os.path.join(current, "meals.csv")
        with open(dishes_data_path, encoding="UTF8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', )

            next(csv_reader) #skip first row with header

            for row in csv_reader:

                dish = Dish(
                    title = row[1],
                    price = row[2],
                    description = row[3],
                    picture = row[4],
                    category_id = row[5]
                )
                db.session.add(dish)
            db.session.commit()   

            print(">>>Dishes -----> done")
    else:
        print("Dish table is not empty")