# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_deployment_review_approved_workflow_job_runs_inner import WebhookDeploymentReviewApprovedWorkflowJobRunsInner

class TestWebhookDeploymentReviewApprovedWorkflowJobRunsInner(unittest.TestCase):
    """WebhookDeploymentReviewApprovedWorkflowJobRunsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookDeploymentReviewApprovedWorkflowJobRunsInner:
        """Test WebhookDeploymentReviewApprovedWorkflowJobRunsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookDeploymentReviewApprovedWorkflowJobRunsInner`
        """
        model = WebhookDeploymentReviewApprovedWorkflowJobRunsInner()
        if include_optional:
            return WebhookDeploymentReviewApprovedWorkflowJobRunsInner(
                conclusion = None,
                created_at = '',
                environment = '',
                html_url = '',
                id = 56,
                name = '',
                status = '',
                updated_at = ''
            )
        else:
            return WebhookDeploymentReviewApprovedWorkflowJobRunsInner(
        )
        """

    def testWebhookDeploymentReviewApprovedWorkflowJobRunsInner(self):
        """Test WebhookDeploymentReviewApprovedWorkflowJobRunsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()