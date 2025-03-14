# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.repository_rule_workflows_parameters import RepositoryRuleWorkflowsParameters

class TestRepositoryRuleWorkflowsParameters(unittest.TestCase):
    """RepositoryRuleWorkflowsParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RepositoryRuleWorkflowsParameters:
        """Test RepositoryRuleWorkflowsParameters
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RepositoryRuleWorkflowsParameters`
        """
        model = RepositoryRuleWorkflowsParameters()
        if include_optional:
            return RepositoryRuleWorkflowsParameters(
                do_not_enforce_on_create = True,
                workflows = [
                    github_openapi.models.workflow_file_reference.WorkflowFileReference(
                        path = '', 
                        ref = '', 
                        repository_id = 56, 
                        sha = '', )
                    ]
            )
        else:
            return RepositoryRuleWorkflowsParameters(
                workflows = [
                    github_openapi.models.workflow_file_reference.WorkflowFileReference(
                        path = '', 
                        ref = '', 
                        repository_id = 56, 
                        sha = '', )
                    ],
        )
        """

    def testRepositoryRuleWorkflowsParameters(self):
        """Test RepositoryRuleWorkflowsParameters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
