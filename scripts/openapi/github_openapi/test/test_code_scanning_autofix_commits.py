# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.code_scanning_autofix_commits import CodeScanningAutofixCommits

class TestCodeScanningAutofixCommits(unittest.TestCase):
    """CodeScanningAutofixCommits unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CodeScanningAutofixCommits:
        """Test CodeScanningAutofixCommits
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CodeScanningAutofixCommits`
        """
        model = CodeScanningAutofixCommits()
        if include_optional:
            return CodeScanningAutofixCommits(
                target_ref = '',
                message = ''
            )
        else:
            return CodeScanningAutofixCommits(
        )
        """

    def testCodeScanningAutofixCommits(self):
        """Test CodeScanningAutofixCommits"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
