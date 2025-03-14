# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.secret_scanning_location_issue_body import SecretScanningLocationIssueBody

class TestSecretScanningLocationIssueBody(unittest.TestCase):
    """SecretScanningLocationIssueBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SecretScanningLocationIssueBody:
        """Test SecretScanningLocationIssueBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SecretScanningLocationIssueBody`
        """
        model = SecretScanningLocationIssueBody()
        if include_optional:
            return SecretScanningLocationIssueBody(
                issue_body_url = 'https://api.github.com/repos/octocat/Hello-World/issues/1347'
            )
        else:
            return SecretScanningLocationIssueBody(
                issue_body_url = 'https://api.github.com/repos/octocat/Hello-World/issues/1347',
        )
        """

    def testSecretScanningLocationIssueBody(self):
        """Test SecretScanningLocationIssueBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
