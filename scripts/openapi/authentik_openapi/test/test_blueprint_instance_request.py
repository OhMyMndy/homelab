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

from authentik_openapi.models.blueprint_instance_request import BlueprintInstanceRequest

class TestBlueprintInstanceRequest(unittest.TestCase):
    """BlueprintInstanceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BlueprintInstanceRequest:
        """Test BlueprintInstanceRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BlueprintInstanceRequest`
        """
        model = BlueprintInstanceRequest()
        if include_optional:
            return BlueprintInstanceRequest(
                name = '0',
                path = '',
                context = None,
                enabled = True,
                content = ''
            )
        else:
            return BlueprintInstanceRequest(
                name = '0',
        )
        """

    def testBlueprintInstanceRequest(self):
        """Test BlueprintInstanceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
