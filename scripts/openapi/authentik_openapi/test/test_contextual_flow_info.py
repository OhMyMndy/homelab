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

from authentik_openapi.models.contextual_flow_info import ContextualFlowInfo

class TestContextualFlowInfo(unittest.TestCase):
    """ContextualFlowInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContextualFlowInfo:
        """Test ContextualFlowInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContextualFlowInfo`
        """
        model = ContextualFlowInfo()
        if include_optional:
            return ContextualFlowInfo(
                title = '',
                background = '',
                cancel_url = '',
                layout = 'stacked'
            )
        else:
            return ContextualFlowInfo(
                cancel_url = '',
                layout = 'stacked',
        )
        """

    def testContextualFlowInfo(self):
        """Test ContextualFlowInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()