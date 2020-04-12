import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mongowarehouse"]
col_account = db["account"]
col_item = db["item"]
col_transaction = db["transaction"]

dataaccount = [
    {"username":"Admin","password":"12345","name":"Admin1","role":"Admin"},
    {"username":"PengurusGudang","password":"12345","name":"Pengurus Gudang1","role":"Pengurus Gudang"},
    {"username":"Kasir","password":"12345","name":"Kasir1","role":"Kasir"},
]

dataitem = [
    {"itemname": "Samsung Galaxy S20 Ultra","price": "1200","amountitem": "20"},
    {"itemname": "Samsung Galaxy S20+", "price": "899", "amountitem": "25"},
    {"itemname": "Samsung Galaxy S20", "price": "749", "amountitem": "19"},
    {"itemname": "Apple Iphone X","price": "999", "amountitem": "9"},
    {"itemname": "Apple Iphone 11 Pro Max", "price": "1500", "amountitem": "18"},
    {"itemname": "Asus ROG Phone 2", "price": "799", "amountitem": "26"},
    {"itemname": "Xiaomi Redmi Note 10 Pro", "price": "599", "amountitem": "35"}
]

transaction = [
    {"cashiername":"Kasir1","itemname": "Samsung Galaxy S20 Ultra","price":"1200","amountitem":"2","totalprice":"2400"},
    {"cashiername":"Kasir1","itemname":"Apple Iphone X","price": "999","amountitem": "1","totalprice": "999"},
    {"cashiername":"Kasir1","itemname": "Apple Iphone 11 Pro Max","price": "1500","amountitem": "3","totalprice": "4500"}
]

col_account.insert_many(dataaccount)
col_item.insert_many(dataitem)
col_transaction.insert_many(transaction)
