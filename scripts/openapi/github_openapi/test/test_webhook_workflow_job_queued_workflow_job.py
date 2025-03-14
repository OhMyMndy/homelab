# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_workflow_job_queued_workflow_job import WebhookWorkflowJobQueuedWorkflowJob

class TestWebhookWorkflowJobQueuedWorkflowJob(unittest.TestCase):
    """WebhookWorkflowJobQueuedWorkflowJob unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookWorkflowJobQueuedWorkflowJob:
        """Test WebhookWorkflowJobQueuedWorkflowJob
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookWorkflowJobQueuedWorkflowJob`
        """
        model = WebhookWorkflowJobQueuedWorkflowJob()
        if include_optional:
            return WebhookWorkflowJobQueuedWorkflowJob(
                check_run_url = '',
                completed_at = '',
                conclusion = '',
                created_at = '',
                head_sha = '',
                html_url = '',
                id = 56,
                labels = [
                    ''
                    ],
                name = '',
                node_id = '',
                run_attempt = 56,
                run_id = 1.337,
                run_url = '',
                runner_group_id = 56,
                runner_group_name = '',
                runner_id = 56,
                runner_name = '',
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'queued',
                head_branch = '',
                workflow_name = '',
                steps = [
                    github_openapi.models.workflow_step.Workflow Step(
                        completed_at = '', 
                        conclusion = 'failure', 
                        name = '', 
                        number = 56, 
                        started_at = '', 
                        status = 'completed', )
                    ],
                url = ''
            )
        else:
            return WebhookWorkflowJobQueuedWorkflowJob(
                check_run_url = '',
                completed_at = '',
                conclusion = '',
                created_at = '',
                head_sha = '',
                html_url = '',
                id = 56,
                labels = [
                    ''
                    ],
                name = '',
                node_id = '',
                run_attempt = 56,
                run_id = 1.337,
                run_url = '',
                runner_group_id = 56,
                runner_group_name = '',
                runner_id = 56,
                runner_name = '',
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'queued',
                head_branch = '',
                workflow_name = '',
                steps = [
                    github_openapi.models.workflow_step.Workflow Step(
                        completed_at = '', 
                        conclusion = 'failure', 
                        name = '', 
                        number = 56, 
                        started_at = '', 
                        status = 'completed', )
                    ],
                url = '',
        )
        """

    def testWebhookWorkflowJobQueuedWorkflowJob(self):
        """Test WebhookWorkflowJobQueuedWorkflowJob"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
