# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.student import Student  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_add_student(self):
        """Test case for add_student

        Add a new student
        """
        body = Student()
        response = self.client.open(
            '/Irakliy/tutorial/1.0.0/student',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_student(self):
        """Test case for delete_student

        deletes a student
        """
        response = self.client.open(
            '/Irakliy/tutorial/1.0.0/student/{student_id}'.format(student_id=1.2),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_student_by_id(self):
        """Test case for get_student_by_id

        gets student
        """
        response = self.client.open(
            '/Irakliy/tutorial/1.0.0/student/{student_id}'.format(student_id=1.2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
