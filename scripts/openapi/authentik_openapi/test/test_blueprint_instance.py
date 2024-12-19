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

from authentik_openapi.models.blueprint_instance import BlueprintInstance

class TestBlueprintInstance(unittest.TestCase):
    """BlueprintInstance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BlueprintInstance:
        """Test BlueprintInstance
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BlueprintInstance`
        """
        model = BlueprintInstance()
        if include_optional:
            return BlueprintInstance(
                pk = '',
                name = '',
                path = '',
                context = None,
                last_applied = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_applied_hash = '',
                status = 'successful',
                enabled = True,
                managed_models = [
                    ''
                    ],
                metadata = None,
                content = ''
            )
        else:
            return BlueprintInstance(
                pk = '',
                name = '',
                last_applied = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_applied_hash = '',
                status = 'successful',
                managed_models = [
                    ''
                    ],
                metadata = None,
        )
        """

    def testBlueprintInstance(self):
        """Test BlueprintInstance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
