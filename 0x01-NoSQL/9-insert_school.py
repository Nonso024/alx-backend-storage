#!/usr/bin/env python3
""" Script that inserts new doc into collection """


def insert_school(mongo_collection, **kwargs):
    """ Inserts school document into collection """

    if mongo_collection is None:
        return []

    return mongo_collection.insert_one(kwargs).inserted_id
