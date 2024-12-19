# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.gist_simple_files_value import GistSimpleFilesValue

class TestGistSimpleFilesValue(unittest.TestCase):
    """GistSimpleFilesValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GistSimpleFilesValue:
        """Test GistSimpleFilesValue
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GistSimpleFilesValue`
        """
        model = GistSimpleFilesValue()
        if include_optional:
            return GistSimpleFilesValue(
                filename = '',
                type = '',
                language = '',
                raw_url = '',
                size = 56,
                truncated = True,
                content = '',
                encoding = 'utf-8'
            )
        else:
            return GistSimpleFilesValue(
        )
        """

    def testGistSimpleFilesValue(self):
        """Test GistSimpleFilesValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()