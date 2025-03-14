# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.copilot_ide_code_completions import CopilotIdeCodeCompletions

class TestCopilotIdeCodeCompletions(unittest.TestCase):
    """CopilotIdeCodeCompletions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CopilotIdeCodeCompletions:
        """Test CopilotIdeCodeCompletions
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CopilotIdeCodeCompletions`
        """
        model = CopilotIdeCodeCompletions()
        if include_optional:
            return CopilotIdeCodeCompletions(
                total_engaged_users = 56,
                languages = [
                    github_openapi.models.copilot_ide_code_completions_languages_inner.copilot_ide_code_completions_languages_inner(
                        name = '', 
                        total_engaged_users = 56, )
                    ],
                editors = [
                    { }
                    ]
            )
        else:
            return CopilotIdeCodeCompletions(
        )
        """

    def testCopilotIdeCodeCompletions(self):
        """Test CopilotIdeCodeCompletions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
