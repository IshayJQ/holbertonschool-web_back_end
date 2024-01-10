#!/usr/bin/env python3
"""
Return the id for the new document
"""


def insert_school(mongo_collection, **kwargs):
    """
    Function that inserts a new document in a collection
    """
    document = mongo_collection.insert_one(kwargs)
    return document.inserted_id
