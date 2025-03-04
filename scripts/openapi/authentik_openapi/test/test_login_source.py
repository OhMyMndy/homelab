# coding: utf-8

"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2024.6.4
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from authentik_openapi.models.login_source import LoginSource

class TestLoginSource(unittest.TestCase):
    """LoginSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LoginSource:
        """Test LoginSource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LoginSource`
        """
        model = LoginSource()
        if include_optional:
            return LoginSource(
                name = '',
                icon_url = '',
                challenge = None
            )
        else:
            return LoginSource(
                name = '',
                challenge = None,
        )
        """

    def testLoginSource(self):
        """Test LoginSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
