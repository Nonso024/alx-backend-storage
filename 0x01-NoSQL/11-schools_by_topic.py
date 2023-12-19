#!/usr/bin/env python3
""" Script return a list of schools having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """ Returns list of school per specifc topic """

    if mongo_collection is None:
        return None
    return mongo_collection.find({"topics": topic})
