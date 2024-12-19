# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.workflow_run_usage_billable_ubuntu_job_runs_inner import WorkflowRunUsageBillableUBUNTUJobRunsInner

class TestWorkflowRunUsageBillableUBUNTUJobRunsInner(unittest.TestCase):
    """WorkflowRunUsageBillableUBUNTUJobRunsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkflowRunUsageBillableUBUNTUJobRunsInner:
        """Test WorkflowRunUsageBillableUBUNTUJobRunsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkflowRunUsageBillableUBUNTUJobRunsInner`
        """
        model = WorkflowRunUsageBillableUBUNTUJobRunsInner()
        if include_optional:
            return WorkflowRunUsageBillableUBUNTUJobRunsInner(
                job_id = 56,
                duration_ms = 56
            )
        else:
            return WorkflowRunUsageBillableUBUNTUJobRunsInner(
                job_id = 56,
                duration_ms = 56,
        )
        """

    def testWorkflowRunUsageBillableUBUNTUJobRunsInner(self):
        """Test WorkflowRunUsageBillableUBUNTUJobRunsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
