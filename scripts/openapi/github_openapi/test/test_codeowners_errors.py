# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.codeowners_errors import CodeownersErrors

class TestCodeownersErrors(unittest.TestCase):
    """CodeownersErrors unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CodeownersErrors:
        """Test CodeownersErrors
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CodeownersErrors`
        """
        model = CodeownersErrors()
        if include_optional:
            return CodeownersErrors(
                errors = [
                    github_openapi.models.codeowners_errors_errors_inner.codeowners_errors_errors_inner(
                        line = 7, 
                        column = 3, 
                        source = '* user', 
                        kind = 'Invalid owner', 
                        suggestion = 'The pattern `/` will never match anything, did you mean `*` instead?', 
                        message = 'Invalid owner on line 7:

  * user
    ^', 
                        path = '.github/CODEOWNERS', )
                    ]
            )
        else:
            return CodeownersErrors(
                errors = [
                    github_openapi.models.codeowners_errors_errors_inner.codeowners_errors_errors_inner(
                        line = 7, 
                        column = 3, 
                        source = '* user', 
                        kind = 'Invalid owner', 
                        suggestion = 'The pattern `/` will never match anything, did you mean `*` instead?', 
                        message = 'Invalid owner on line 7:

  * user
    ^', 
                        path = '.github/CODEOWNERS', )
                    ],
        )
        """

    def testCodeownersErrors(self):
        """Test CodeownersErrors"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()