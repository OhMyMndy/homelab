# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.repos_delete_file_request_author import ReposDeleteFileRequestAuthor

class TestReposDeleteFileRequestAuthor(unittest.TestCase):
    """ReposDeleteFileRequestAuthor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReposDeleteFileRequestAuthor:
        """Test ReposDeleteFileRequestAuthor
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReposDeleteFileRequestAuthor`
        """
        model = ReposDeleteFileRequestAuthor()
        if include_optional:
            return ReposDeleteFileRequestAuthor(
                name = '',
                email = ''
            )
        else:
            return ReposDeleteFileRequestAuthor(
        )
        """

    def testReposDeleteFileRequestAuthor(self):
        """Test ReposDeleteFileRequestAuthor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()