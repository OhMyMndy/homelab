# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_openapi.models.access_token import AccessToken

class TestAccessToken(unittest.TestCase):
    """AccessToken unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessToken:
        """Test AccessToken
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessToken`
        """
        model = AccessToken()
        if include_optional:
            return AccessToken(
                id = 56,
                name = '',
                scopes = [
                    ''
                    ],
                sha1 = '',
                token_last_eight = ''
            )
        else:
            return AccessToken(
        )
        """

    def testAccessToken(self):
        """Test AccessToken"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()