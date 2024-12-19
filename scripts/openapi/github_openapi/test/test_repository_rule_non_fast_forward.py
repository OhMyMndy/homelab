# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.repository_rule_non_fast_forward import RepositoryRuleNonFastForward

class TestRepositoryRuleNonFastForward(unittest.TestCase):
    """RepositoryRuleNonFastForward unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RepositoryRuleNonFastForward:
        """Test RepositoryRuleNonFastForward
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RepositoryRuleNonFastForward`
        """
        model = RepositoryRuleNonFastForward()
        if include_optional:
            return RepositoryRuleNonFastForward(
                type = 'non_fast_forward'
            )
        else:
            return RepositoryRuleNonFastForward(
                type = 'non_fast_forward',
        )
        """

    def testRepositoryRuleNonFastForward(self):
        """Test RepositoryRuleNonFastForward"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()