#!/usr/bin/env python3
"""
changes all topics of a document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """function that changes all topics"""
    topic = mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
