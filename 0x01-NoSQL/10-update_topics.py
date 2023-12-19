#!/usr/bin/env python3
""" Script that changes topics based on school name """


def update_topics(mongo_collection, name, topics):
    """ Update topis """

    if mongo_collection is None:
        return []

    return mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}})
