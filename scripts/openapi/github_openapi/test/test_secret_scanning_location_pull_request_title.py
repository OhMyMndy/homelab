# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.secret_scanning_location_pull_request_title import SecretScanningLocationPullRequestTitle

class TestSecretScanningLocationPullRequestTitle(unittest.TestCase):
    """SecretScanningLocationPullRequestTitle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SecretScanningLocationPullRequestTitle:
        """Test SecretScanningLocationPullRequestTitle
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SecretScanningLocationPullRequestTitle`
        """
        model = SecretScanningLocationPullRequestTitle()
        if include_optional:
            return SecretScanningLocationPullRequestTitle(
                pull_request_title_url = 'https://api.github.com/repos/octocat/Hello-World/pulls/2846'
            )
        else:
            return SecretScanningLocationPullRequestTitle(
                pull_request_title_url = 'https://api.github.com/repos/octocat/Hello-World/pulls/2846',
        )
        """

    def testSecretScanningLocationPullRequestTitle(self):
        """Test SecretScanningLocationPullRequestTitle"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
