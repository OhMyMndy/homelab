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

from authentik_openapi.models.token_request import TokenRequest

class TestTokenRequest(unittest.TestCase):
    """TokenRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenRequest:
        """Test TokenRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenRequest`
        """
        model = TokenRequest()
        if include_optional:
            return TokenRequest(
                managed = '0',
                identifier = 'z0',
                intent = 'verification',
                user = 56,
                description = '',
                expires = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expiring = True
            )
        else:
            return TokenRequest(
                identifier = 'z0',
        )
        """

    def testTokenRequest(self):
        """Test TokenRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
