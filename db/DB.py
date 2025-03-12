import pymongo

myclient = pymongo.MongoClient("mongodb+srv://gowsalya:SRINUVASAN22@gowsalya.yz0c6.mongodb.net/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = [
{'_id': 1, 'name': 'John', 'address': 'Highway37'},
{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'},
{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'},
{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'},
{'_id': 5, 'name': 'Michael', 'address': 'Valley 345'},
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'},
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'},
{'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'},
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'},
{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'},
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'},
{'_id': 12, 'name': 'William', 'address': 'Central st 954'},
{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'},
{'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}
]
# x = mycol.insert_many(mydict)                       insert value



# myquery = { "address": "Valley 345" }
# newvalues = { "$set": { "address": "Canyon 123" } }
# mycol.update_one(myquery, newvalues)                    update value
# for x in mycol.find():
#   print(x)

# myquery = { "address": { "$regex": "^S" } }
# newvalues = { "$set": { "name": "Minnie" } }             documents update
# x = mycol.update_many(myquery, newvalues)
# print(x.modified_count, "documents updated.")

# myquery = { "address": "Mountain 21" }
# mycol.delete_one(myquery)                               delete value


# mydoc = mycol.find().sort("name")                             sort name
# for x in mydoc:
#   print(x)


# mydoc = mycol.find().sort("_id",-1)                               id and descending
# for x in mydoc:
#   print(x)


# myquery = { "address": "Park Lane 38" }
# mydoc = mycol.find(myquery)
# for x in mydoc:                                                   find values
#   print(x)


# myquery = { "address": { "$gt": "S" } }
# mydoc = mycol.find(myquery)
# for x in mydoc:                                             find methods Recursi
#   print(x)


