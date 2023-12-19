#!/usr/bin/env python3
""" Script that lists all docs in a collection """


def list_all(mongo_collection):
    """ Lists all documents in collection """

    if mongo_collection is None:
        return []

    return mongo_collection.find()
