#!/usr/bin/env python
import pymongo

# no need to import sys

# establish a connection to the database
# TODO specify appropriate connection string
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
# TODO specify correct db / collection names
db = connection.db
collection_1 = db.collection_1
collection_2 = db.collection_2


def find():
    query = {}
    collection_1_count = collection_1.find(query).count()
    print str(collection_1_count) + ' count of items in collection 1'
    collection_2_count = collection_2.find(query).count()
    print str(collection_2_count) + ' count of items in collection 2'


find()

print 'Done'
