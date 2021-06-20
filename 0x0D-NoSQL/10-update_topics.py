#!/usr/bin/env python3
""" 10-Change school topics  """


def update_topics(mongo_collection, name, topics):
    """Function: changes all topics of a school document
    based on the name"""
    myquery = {'name': name}
    newvalues = {'$set': {'topics': topics}}
    mongo_collection.update_many(myquery, newvalues)
