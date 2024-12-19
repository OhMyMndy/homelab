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

from authentik_openapi.models.shell_challenge import ShellChallenge

class TestShellChallenge(unittest.TestCase):
    """ShellChallenge unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ShellChallenge:
        """Test ShellChallenge
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ShellChallenge`
        """
        model = ShellChallenge()
        if include_optional:
            return ShellChallenge(
                type = 'native',
                flow_info = authentik_openapi.models.contextual_flow_info.ContextualFlowInfo(
                    title = '', 
                    background = '', 
                    cancel_url = '', 
                    layout = 'stacked', ),
                component = 'xak-flow-shell',
                response_errors = {
                    'key' : [
                        authentik_openapi.models.error_detail.ErrorDetail(
                            string = '', 
                            code = '', )
                        ]
                    },
                body = ''
            )
        else:
            return ShellChallenge(
                type = 'native',
                body = '',
        )
        """

    def testShellChallenge(self):
        """Test ShellChallenge"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
