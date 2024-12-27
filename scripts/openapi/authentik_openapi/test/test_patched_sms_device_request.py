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

from authentik_openapi.models.patched_sms_device_request import PatchedSMSDeviceRequest

class TestPatchedSMSDeviceRequest(unittest.TestCase):
    """PatchedSMSDeviceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedSMSDeviceRequest:
        """Test PatchedSMSDeviceRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedSMSDeviceRequest`
        """
        model = PatchedSMSDeviceRequest()
        if include_optional:
            return PatchedSMSDeviceRequest(
                name = '0'
            )
        else:
            return PatchedSMSDeviceRequest(
        )
        """

    def testPatchedSMSDeviceRequest(self):
        """Test PatchedSMSDeviceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()