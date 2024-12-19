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

from authentik_openapi.models.totp_device_request import TOTPDeviceRequest

class TestTOTPDeviceRequest(unittest.TestCase):
    """TOTPDeviceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TOTPDeviceRequest:
        """Test TOTPDeviceRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TOTPDeviceRequest`
        """
        model = TOTPDeviceRequest()
        if include_optional:
            return TOTPDeviceRequest(
                name = '0'
            )
        else:
            return TOTPDeviceRequest(
                name = '0',
        )
        """

    def testTOTPDeviceRequest(self):
        """Test TOTPDeviceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
