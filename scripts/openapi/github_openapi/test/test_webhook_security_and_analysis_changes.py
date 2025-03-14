# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_security_and_analysis_changes import WebhookSecurityAndAnalysisChanges

class TestWebhookSecurityAndAnalysisChanges(unittest.TestCase):
    """WebhookSecurityAndAnalysisChanges unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookSecurityAndAnalysisChanges:
        """Test WebhookSecurityAndAnalysisChanges
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookSecurityAndAnalysisChanges`
        """
        model = WebhookSecurityAndAnalysisChanges()
        if include_optional:
            return WebhookSecurityAndAnalysisChanges(
                var_from = github_openapi.models.webhook_security_and_analysis_changes_from.webhook_security_and_analysis_changes_from(
                    security_and_analysis = github_openapi.models.security_and_analysis.security-and-analysis(
                        advanced_security = github_openapi.models.security_and_analysis_advanced_security.security_and_analysis_advanced_security(
                            status = 'enabled', ), 
                        dependabot_security_updates = github_openapi.models.security_and_analysis_dependabot_security_updates.security_and_analysis_dependabot_security_updates(
                            status = 'enabled', ), 
                        secret_scanning = github_openapi.models.security_and_analysis_advanced_security.security_and_analysis_advanced_security(
                            status = 'enabled', ), 
                        secret_scanning_push_protection = , 
                        secret_scanning_non_provider_patterns = , 
                        secret_scanning_ai_detection = , ), )
            )
        else:
            return WebhookSecurityAndAnalysisChanges(
        )
        """

    def testWebhookSecurityAndAnalysisChanges(self):
        """Test WebhookSecurityAndAnalysisChanges"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
