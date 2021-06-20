#!/usr/bin/env python3
""" 9-insert school """


def insert_school(mongo_collection, **kwargs):
    """Function: Insert a document in Python"""
    x = mongo_collection.insert_one(kwargs)
    return x.inserted_id
