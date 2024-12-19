# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.actions_list_repo_workflows200_response import ActionsListRepoWorkflows200Response

class TestActionsListRepoWorkflows200Response(unittest.TestCase):
    """ActionsListRepoWorkflows200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActionsListRepoWorkflows200Response:
        """Test ActionsListRepoWorkflows200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActionsListRepoWorkflows200Response`
        """
        model = ActionsListRepoWorkflows200Response()
        if include_optional:
            return ActionsListRepoWorkflows200Response(
                total_count = 56,
                workflows = [
                    github_openapi.models.workflow.Workflow(
                        id = 5, 
                        node_id = 'MDg6V29ya2Zsb3cxMg==', 
                        name = 'CI', 
                        path = 'ruby.yaml', 
                        state = 'active', 
                        created_at = '2019-12-06T14:20:20Z', 
                        updated_at = '2019-12-06T14:20:20Z', 
                        url = 'https://api.github.com/repos/actions/setup-ruby/workflows/5', 
                        html_url = 'https://github.com/actions/setup-ruby/blob/master/.github/workflows/ruby.yaml', 
                        badge_url = 'https://github.com/actions/setup-ruby/workflows/CI/badge.svg', 
                        deleted_at = '2019-12-06T14:20:20Z', )
                    ]
            )
        else:
            return ActionsListRepoWorkflows200Response(
                total_count = 56,
                workflows = [
                    github_openapi.models.workflow.Workflow(
                        id = 5, 
                        node_id = 'MDg6V29ya2Zsb3cxMg==', 
                        name = 'CI', 
                        path = 'ruby.yaml', 
                        state = 'active', 
                        created_at = '2019-12-06T14:20:20Z', 
                        updated_at = '2019-12-06T14:20:20Z', 
                        url = 'https://api.github.com/repos/actions/setup-ruby/workflows/5', 
                        html_url = 'https://github.com/actions/setup-ruby/blob/master/.github/workflows/ruby.yaml', 
                        badge_url = 'https://github.com/actions/setup-ruby/workflows/CI/badge.svg', 
                        deleted_at = '2019-12-06T14:20:20Z', )
                    ],
        )
        """

    def testActionsListRepoWorkflows200Response(self):
        """Test ActionsListRepoWorkflows200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
