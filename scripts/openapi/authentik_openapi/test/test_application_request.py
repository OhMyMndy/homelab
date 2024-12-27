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

from authentik_openapi.models.application_request import ApplicationRequest

class TestApplicationRequest(unittest.TestCase):
    """ApplicationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApplicationRequest:
        """Test ApplicationRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApplicationRequest`
        """
        model = ApplicationRequest()
        if include_optional:
            return ApplicationRequest(
                name = '0',
                slug = 'z0',
                provider = 56,
                backchannel_providers = [
                    56
                    ],
                open_in_new_tab = True,
                meta_launch_url = '',
                meta_description = '',
                meta_publisher = '',
                policy_engine_mode = 'all',
                group = ''
            )
        else:
            return ApplicationRequest(
                name = '0',
                slug = 'z0',
        )
        """

    def testApplicationRequest(self):
        """Test ApplicationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()