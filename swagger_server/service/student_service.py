import os
import tempfile
from functools import reduce

from tinydb import TinyDB, Query
# from pymongo import MongoClient

db_dir_path = tempfile.gettempdir()
db_file_path = os.path.join(db_dir_path, "students.json")
student_db = TinyDB(db_file_path)

# student_db.truncate()
####
# my_student_db = MongoClient('mongodb://localhost:27017/')

##
# def get_db():
#     client = MongoClient('mongodb://localhost:27017/')
#     return client.student_db
#

def add(student=None):
    queries = []
    query = Query()
    queries.append(query.first_name == student.first_name)
    queries.append(query.last_name == student.last_name)
    query = reduce(lambda a, b: a & b, queries)
    res = student_db.search(query)
    if res:
        return 'already exists', 409

    doc_id = student_db.insert(student.to_dict())
    student.student_id = doc_id
    return student.student_id, 200


# def get_by_id(student_id=None, subject=None):
#     # student = student_db.get(doc_id=int(student_id))
#     Student = Query()
#     student = student_db.search(Student.student_id == int(student_id))
#
#     if not student:
#         return 'not found', 404
#     return student, 200


# def delete(student_id=None):
#     Student = Query()
#     search_result = student_db.search(Student.student_id == int(student_id))
#
#     if not search_result:
#         return 'not found', 404
#
#     # Remove documents matching the student_id
#     student_db.remove(Student.student_id == int(student_id))
#     return 'Successfully removed Student ID ' + str(student_id), 200


#On my machine, originally provided GET and DELETE with more than 2 digit IDs do no work
#However, it works on github.
#While my code works PERFECTLY on my machine, while it doesn't work in GitHub.
#This doesn't make any sense.


def get_by_id(student_id=None, subject=None):
    student = student_db.get(doc_id=int(student_id))
    if not student:
        return 'not found', 404
    student['student_id'] = student_id
    print(student)
    return student


def delete(student_id=None):
    student = student_db.get(doc_id=int(student_id))
    if not student:
        return 'not found', 404
    student_db.remove(doc_ids=[int(student_id)])
    return student_id