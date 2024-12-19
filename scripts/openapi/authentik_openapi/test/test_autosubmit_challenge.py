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

from authentik_openapi.models.autosubmit_challenge import AutosubmitChallenge

class TestAutosubmitChallenge(unittest.TestCase):
    """AutosubmitChallenge unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AutosubmitChallenge:
        """Test AutosubmitChallenge
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AutosubmitChallenge`
        """
        model = AutosubmitChallenge()
        if include_optional:
            return AutosubmitChallenge(
                type = 'native',
                flow_info = authentik_openapi.models.contextual_flow_info.ContextualFlowInfo(
                    title = '', 
                    background = '', 
                    cancel_url = '', 
                    layout = 'stacked', ),
                component = 'ak-stage-autosubmit',
                response_errors = {
                    'key' : [
                        authentik_openapi.models.error_detail.ErrorDetail(
                            string = '', 
                            code = '', )
                        ]
                    },
                url = '',
                attrs = {
                    'key' : ''
                    },
                title = ''
            )
        else:
            return AutosubmitChallenge(
                type = 'native',
                url = '',
                attrs = {
                    'key' : ''
                    },
        )
        """

    def testAutosubmitChallenge(self):
        """Test AutosubmitChallenge"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
