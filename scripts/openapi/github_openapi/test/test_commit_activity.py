# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.commit_activity import CommitActivity

class TestCommitActivity(unittest.TestCase):
    """CommitActivity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommitActivity:
        """Test CommitActivity
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommitActivity`
        """
        model = CommitActivity()
        if include_optional:
            return CommitActivity(
                days = [0,3,26,20,39,1,0],
                total = 89,
                week = 1336280400
            )
        else:
            return CommitActivity(
                days = [0,3,26,20,39,1,0],
                total = 89,
                week = 1336280400,
        )
        """

    def testCommitActivity(self):
        """Test CommitActivity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()