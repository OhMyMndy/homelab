# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.runner_groups_org import RunnerGroupsOrg

class TestRunnerGroupsOrg(unittest.TestCase):
    """RunnerGroupsOrg unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RunnerGroupsOrg:
        """Test RunnerGroupsOrg
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RunnerGroupsOrg`
        """
        model = RunnerGroupsOrg()
        if include_optional:
            return RunnerGroupsOrg(
                id = 1.337,
                name = '',
                visibility = '',
                default = True,
                selected_repositories_url = '',
                runners_url = '',
                hosted_runners_url = '',
                inherited = True,
                inherited_allows_public_repositories = True,
                allows_public_repositories = True,
                workflow_restrictions_read_only = True,
                restricted_to_workflows = True,
                selected_workflows = [
                    'octo-org/octo-repo/.github/workflows/deploy.yaml@main'
                    ]
            )
        else:
            return RunnerGroupsOrg(
                id = 1.337,
                name = '',
                visibility = '',
                default = True,
                runners_url = '',
                inherited = True,
                allows_public_repositories = True,
        )
        """

    def testRunnerGroupsOrg(self):
        """Test RunnerGroupsOrg"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()