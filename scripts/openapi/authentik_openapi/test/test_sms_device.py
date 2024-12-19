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

from authentik_openapi.models.sms_device import SMSDevice

class TestSMSDevice(unittest.TestCase):
    """SMSDevice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SMSDevice:
        """Test SMSDevice
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SMSDevice`
        """
        model = SMSDevice()
        if include_optional:
            return SMSDevice(
                name = '',
                pk = 56,
                phone_number = ''
            )
        else:
            return SMSDevice(
                name = '',
                pk = 56,
                phone_number = '',
        )
        """

    def testSMSDevice(self):
        """Test SMSDevice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
