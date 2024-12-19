# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_openapi.models.issue_labels_option import IssueLabelsOption

class TestIssueLabelsOption(unittest.TestCase):
    """IssueLabelsOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IssueLabelsOption:
        """Test IssueLabelsOption
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IssueLabelsOption`
        """
        model = IssueLabelsOption()
        if include_optional:
            return IssueLabelsOption(
                labels = [
                    56
                    ]
            )
        else:
            return IssueLabelsOption(
        )
        """

    def testIssueLabelsOption(self):
        """Test IssueLabelsOption"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
