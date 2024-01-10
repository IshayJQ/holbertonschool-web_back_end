#!/usr/bin/env python3
"""
Return a list with all documments in a collection
"""


def list_all(mongo_collection):
    """
    function that lists all documents in a collection
    """
    elements = mongo_collection.find()
    documents = list(elements)
    return documents
