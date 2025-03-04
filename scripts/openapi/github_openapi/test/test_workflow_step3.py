# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.workflow_step3 import WorkflowStep3

class TestWorkflowStep3(unittest.TestCase):
    """WorkflowStep3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkflowStep3:
        """Test WorkflowStep3
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkflowStep3`
        """
        model = WorkflowStep3()
        if include_optional:
            return WorkflowStep3(
                completed_at = '',
                conclusion = 'failure',
                name = '',
                number = 56,
                started_at = '',
                status = 'completed'
            )
        else:
            return WorkflowStep3(
                completed_at = '',
                conclusion = 'failure',
                name = '',
                number = 56,
                started_at = '',
                status = 'completed',
        )
        """

    def testWorkflowStep3(self):
        """Test WorkflowStep3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
