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

from authentik_openapi.models.redirect_challenge import RedirectChallenge

class TestRedirectChallenge(unittest.TestCase):
    """RedirectChallenge unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RedirectChallenge:
        """Test RedirectChallenge
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RedirectChallenge`
        """
        model = RedirectChallenge()
        if include_optional:
            return RedirectChallenge(
                type = 'native',
                flow_info = authentik_openapi.models.contextual_flow_info.ContextualFlowInfo(
                    title = '', 
                    background = '', 
                    cancel_url = '', 
                    layout = 'stacked', ),
                component = 'xak-flow-redirect',
                response_errors = {
                    'key' : [
                        authentik_openapi.models.error_detail.ErrorDetail(
                            string = '', 
                            code = '', )
                        ]
                    },
                to = ''
            )
        else:
            return RedirectChallenge(
                type = 'native',
                to = '',
        )
        """

    def testRedirectChallenge(self):
        """Test RedirectChallenge"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
