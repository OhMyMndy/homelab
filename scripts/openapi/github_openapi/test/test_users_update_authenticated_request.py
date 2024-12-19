# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.users_update_authenticated_request import UsersUpdateAuthenticatedRequest

class TestUsersUpdateAuthenticatedRequest(unittest.TestCase):
    """UsersUpdateAuthenticatedRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsersUpdateAuthenticatedRequest:
        """Test UsersUpdateAuthenticatedRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsersUpdateAuthenticatedRequest`
        """
        model = UsersUpdateAuthenticatedRequest()
        if include_optional:
            return UsersUpdateAuthenticatedRequest(
                name = 'Omar Jahandar',
                email = 'omar@example.com',
                blog = 'blog.example.com',
                twitter_username = 'therealomarj',
                company = 'Acme corporation',
                location = 'Berlin, Germany',
                hireable = True,
                bio = ''
            )
        else:
            return UsersUpdateAuthenticatedRequest(
        )
        """

    def testUsersUpdateAuthenticatedRequest(self):
        """Test UsersUpdateAuthenticatedRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
