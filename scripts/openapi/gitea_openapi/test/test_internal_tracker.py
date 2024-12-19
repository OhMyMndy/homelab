# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_openapi.models.internal_tracker import InternalTracker

class TestInternalTracker(unittest.TestCase):
    """InternalTracker unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InternalTracker:
        """Test InternalTracker
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InternalTracker`
        """
        model = InternalTracker()
        if include_optional:
            return InternalTracker(
                allow_only_contributors_to_track_time = True,
                enable_issue_dependencies = True,
                enable_time_tracker = True
            )
        else:
            return InternalTracker(
        )
        """

    def testInternalTracker(self):
        """Test InternalTracker"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
