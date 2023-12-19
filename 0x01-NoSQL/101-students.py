#!/usr/bin/env python3
""" returns students by average """


def top_students(mongo_collection):
    """ returns students sorted the average scores """

    if mongo_collection is None:
        return []

    return mongo_collection.aggregate([
        {'$project': {
            'name': '$name',
            'averageScore': {'&avg': '$topics.score'}
        }}
        {'$sort': {'averageScore': -1}}
    ])
