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

from authentik_openapi.models.outpost_request import OutpostRequest

class TestOutpostRequest(unittest.TestCase):
    """OutpostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OutpostRequest:
        """Test OutpostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OutpostRequest`
        """
        model = OutpostRequest()
        if include_optional:
            return OutpostRequest(
                name = '0',
                type = 'proxy',
                providers = [
                    56
                    ],
                service_connection = '',
                config = {
                    'key' : null
                    },
                managed = '0'
            )
        else:
            return OutpostRequest(
                name = '0',
                type = 'proxy',
                providers = [
                    56
                    ],
                config = {
                    'key' : null
                    },
        )
        """

    def testOutpostRequest(self):
        """Test OutpostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()