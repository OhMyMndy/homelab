# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.simple_classroom_user import SimpleClassroomUser

class TestSimpleClassroomUser(unittest.TestCase):
    """SimpleClassroomUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SimpleClassroomUser:
        """Test SimpleClassroomUser
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SimpleClassroomUser`
        """
        model = SimpleClassroomUser()
        if include_optional:
            return SimpleClassroomUser(
                id = 1,
                login = 'octocat',
                avatar_url = 'https://github.com/images/error/octocat_happy.gif',
                html_url = 'https://github.com/octocat'
            )
        else:
            return SimpleClassroomUser(
                id = 1,
                login = 'octocat',
                avatar_url = 'https://github.com/images/error/octocat_happy.gif',
                html_url = 'https://github.com/octocat',
        )
        """

    def testSimpleClassroomUser(self):
        """Test SimpleClassroomUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()