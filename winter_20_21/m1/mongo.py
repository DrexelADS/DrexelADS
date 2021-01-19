# Adapted from tutorial at
#    https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb

from pymongo import MongoClient
from pprint import pprint

# connect to mongodb server
client = MongoClient("127.0.0.1")
# make a new database called "drexelads"
db = client.drexelads

# creating some example entries for the "members" table
members = [
    {
        "name": "Adam Bengis",
        "position": "president",
        "position_year": 2018,
    },
    {
        "name": "Vivek Khimani",
        "position": "vice president",
        "position_year": 2018,
    },
    {
        "name": "Ibrahim Elsaid",
        "position": "treasurer",
        "position_year": 2018,
    },
    {
        "name": "Tim Egenton",
        "position": "event coordinator",
        "position_year": 2020,
    },
    {
        "name": "Mat Nguyen",
        "position": "content curator",
        "position_year": 2020,
    },
    {
        "name": "Himani Hisani",
        "position": "marketing and media",
        "position_year": 2020,
    },
]

# insert entries into the members table
db.members.insert_many(members)

# lookup all members who got their position in 2020
members_2018 = db.members.find({"position_year": 2020})
pprint(list(members_2018))

# delete the member whose name is "Tim Egenton"
db.members.delete_one({"name": "Tim Egenton"})

# lookup all members who got their position in 2020 again
members_2018 = db.members.find({"position_year": 2020})
pprint(list(members_2018))
