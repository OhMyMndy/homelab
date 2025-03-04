# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.repos_update_request import ReposUpdateRequest

class TestReposUpdateRequest(unittest.TestCase):
    """ReposUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReposUpdateRequest:
        """Test ReposUpdateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReposUpdateRequest`
        """
        model = ReposUpdateRequest()
        if include_optional:
            return ReposUpdateRequest(
                name = '',
                description = '',
                homepage = '',
                private = True,
                visibility = 'public',
                security_and_analysis = github_openapi.models.repos_update_request_security_and_analysis.repos_update_request_security_and_analysis(
                    advanced_security = github_openapi.models.repos_update_request_security_and_analysis_advanced_security.repos_update_request_security_and_analysis_advanced_security(
                        status = '', ), 
                    secret_scanning = github_openapi.models.repos_update_request_security_and_analysis_secret_scanning.repos_update_request_security_and_analysis_secret_scanning(
                        status = '', ), 
                    secret_scanning_push_protection = github_openapi.models.repos_update_request_security_and_analysis_secret_scanning_push_protection.repos_update_request_security_and_analysis_secret_scanning_push_protection(
                        status = '', ), 
                    secret_scanning_ai_detection = github_openapi.models.repos_update_request_security_and_analysis_secret_scanning_ai_detection.repos_update_request_security_and_analysis_secret_scanning_ai_detection(
                        status = '', ), 
                    secret_scanning_non_provider_patterns = github_openapi.models.repos_update_request_security_and_analysis_secret_scanning_non_provider_patterns.repos_update_request_security_and_analysis_secret_scanning_non_provider_patterns(
                        status = '', ), ),
                has_issues = True,
                has_projects = True,
                has_wiki = True,
                is_template = True,
                default_branch = '',
                allow_squash_merge = True,
                allow_merge_commit = True,
                allow_rebase_merge = True,
                allow_auto_merge = True,
                delete_branch_on_merge = True,
                allow_update_branch = True,
                use_squash_pr_title_as_default = True,
                squash_merge_commit_title = 'PR_TITLE',
                squash_merge_commit_message = 'PR_BODY',
                merge_commit_title = 'PR_TITLE',
                merge_commit_message = 'PR_BODY',
                archived = True,
                allow_forking = True,
                web_commit_signoff_required = True
            )
        else:
            return ReposUpdateRequest(
        )
        """

    def testReposUpdateRequest(self):
        """Test ReposUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
