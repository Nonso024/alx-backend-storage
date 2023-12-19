#!/usr/bin/env python3
""" Script that logs stats about an nginx collection """


if __name__ == '__main__':
    """ Import MongoClient """
    from pymongo import MongoClient

    client = MongoClient()
    db = client.logs

    print("{} logs".format(db.nginx.count_documents({})))
    print("Methods:")

    for method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
        count = db.nginx.count_documents({'method': method})
        print("\tmethod {}: {}".format(method, count))

    count = db.nginx.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{count} status check")
    client.close()
