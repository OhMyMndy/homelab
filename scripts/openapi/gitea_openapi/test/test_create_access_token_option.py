# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_openapi.models.create_access_token_option import CreateAccessTokenOption

class TestCreateAccessTokenOption(unittest.TestCase):
    """CreateAccessTokenOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateAccessTokenOption:
        """Test CreateAccessTokenOption
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateAccessTokenOption`
        """
        model = CreateAccessTokenOption()
        if include_optional:
            return CreateAccessTokenOption(
                name = '',
                scopes = [
                    ''
                    ]
            )
        else:
            return CreateAccessTokenOption(
                name = '',
        )
        """

    def testCreateAccessTokenOption(self):
        """Test CreateAccessTokenOption"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()