#!/usr/bin/env python3
"""
Returns the list having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    function that returns the list of school having a specific topic
    """
    top = mongo_collection.find({'topics': topic})

    schools = list(top)

    return schools
