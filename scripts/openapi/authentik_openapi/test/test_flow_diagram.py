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

from authentik_openapi.models.flow_diagram import FlowDiagram

class TestFlowDiagram(unittest.TestCase):
    """FlowDiagram unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FlowDiagram:
        """Test FlowDiagram
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FlowDiagram`
        """
        model = FlowDiagram()
        if include_optional:
            return FlowDiagram(
                diagram = ''
            )
        else:
            return FlowDiagram(
                diagram = '',
        )
        """

    def testFlowDiagram(self):
        """Test FlowDiagram"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
