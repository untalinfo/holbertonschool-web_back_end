#!/usr/bin/env python3
""" 12 - Log Stats """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    print(str(logs_collection.count_documents({})) + ' logs')
    print('Methods:')
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for met in method:
        print('\tmethod ' + met + ': ' +
              str(logs_collection.count_documents({'method': met})))
    print(str(logs_collection.count_documents(
          {'method': 'GET', 'path': '/status'})) + ' status check')
