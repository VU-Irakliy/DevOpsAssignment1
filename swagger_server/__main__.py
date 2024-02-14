#!/usr/bin/env python3

import connexion

from swagger_server import encoder

# from pymongo import MongoClient
#
#
# mongo_client = MongoClient('mongodb://localhost:27017/')
# mongo_db = mongo_client['student_db']

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder

    # app.app.config["mongo_db"] = mongo_db

    app.add_api('swagger.yaml', arguments={'title': 'Simple Inventory API'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
