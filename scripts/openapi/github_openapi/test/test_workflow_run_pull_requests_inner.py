# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.workflow_run_pull_requests_inner import WorkflowRunPullRequestsInner

class TestWorkflowRunPullRequestsInner(unittest.TestCase):
    """WorkflowRunPullRequestsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkflowRunPullRequestsInner:
        """Test WorkflowRunPullRequestsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkflowRunPullRequestsInner`
        """
        model = WorkflowRunPullRequestsInner()
        if include_optional:
            return WorkflowRunPullRequestsInner(
                base = github_openapi.models.check_run_pull_request_base.Check_Run_Pull_Request_base(
                    ref = '', 
                    repo = github_openapi.models.repo_ref.Repo Ref(
                        id = 56, 
                        name = '', 
                        url = '', ), 
                    sha = '', ),
                head = github_openapi.models.check_run_pull_request_base.Check_Run_Pull_Request_base(
                    ref = '', 
                    repo = github_openapi.models.repo_ref.Repo Ref(
                        id = 56, 
                        name = '', 
                        url = '', ), 
                    sha = '', ),
                id = 1.337,
                number = 1.337,
                url = ''
            )
        else:
            return WorkflowRunPullRequestsInner(
                base = github_openapi.models.check_run_pull_request_base.Check_Run_Pull_Request_base(
                    ref = '', 
                    repo = github_openapi.models.repo_ref.Repo Ref(
                        id = 56, 
                        name = '', 
                        url = '', ), 
                    sha = '', ),
                head = github_openapi.models.check_run_pull_request_base.Check_Run_Pull_Request_base(
                    ref = '', 
                    repo = github_openapi.models.repo_ref.Repo Ref(
                        id = 56, 
                        name = '', 
                        url = '', ), 
                    sha = '', ),
                id = 1.337,
                number = 1.337,
                url = '',
        )
        """

    def testWorkflowRunPullRequestsInner(self):
        """Test WorkflowRunPullRequestsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()