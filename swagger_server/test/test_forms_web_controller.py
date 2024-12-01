# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.form import Form  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFormsWebController(BaseTestCase):
    """FormsWebController integration test stubs"""

    def test_forms_get(self):
        """Test case for forms_get

        Muestra la lista de formularios.
        """
        response = self.client.open(
            '/forms',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_new_get(self):
        """Test case for new_get

        Muestra la página para crear nuevos formularios.
        """
        response = self.client.open(
            '/new',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
