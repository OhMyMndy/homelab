# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.label1 import Label1

class TestLabel1(unittest.TestCase):
    """Label1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Label1:
        """Test Label1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Label1`
        """
        model = Label1()
        if include_optional:
            return Label1(
                color = '',
                default = True,
                description = '',
                id = 56,
                name = '',
                node_id = '',
                url = ''
            )
        else:
            return Label1(
                color = '',
                default = True,
                description = '',
                id = 56,
                name = '',
                node_id = '',
                url = '',
        )
        """

    def testLabel1(self):
        """Test Label1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
