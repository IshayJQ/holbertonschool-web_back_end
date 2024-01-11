#!/usr/bin/env python3
"""
changes all topics of a document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """function that changes all topics"""
    topic = mongo_collection.update_one(
        {'name': name},
        {'$set': {'topics': topics}}
    )

    if topic.modified_count > 0:
        return True
    else:
        return False
