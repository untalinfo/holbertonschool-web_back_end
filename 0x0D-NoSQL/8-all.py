#!/usr/bin/env python3
"""Module: Python MongoDB"""


def list_all(mongo_collection):
    """Function: List all documents in Python"""
    cursor = mongo_collection.find({})
    return cursor
