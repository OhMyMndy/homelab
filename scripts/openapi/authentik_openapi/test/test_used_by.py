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

from authentik_openapi.models.used_by import UsedBy

class TestUsedBy(unittest.TestCase):
    """UsedBy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsedBy:
        """Test UsedBy
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsedBy`
        """
        model = UsedBy()
        if include_optional:
            return UsedBy(
                app = '',
                model_name = '',
                pk = '',
                name = '',
                action = 'cascade'
            )
        else:
            return UsedBy(
                app = '',
                model_name = '',
                pk = '',
                name = '',
                action = 'cascade',
        )
        """

    def testUsedBy(self):
        """Test UsedBy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()