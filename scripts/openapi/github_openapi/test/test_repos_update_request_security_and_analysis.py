# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.repos_update_request_security_and_analysis import ReposUpdateRequestSecurityAndAnalysis

class TestReposUpdateRequestSecurityAndAnalysis(unittest.TestCase):
    """ReposUpdateRequestSecurityAndAnalysis unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReposUpdateRequestSecurityAndAnalysis:
        """Test ReposUpdateRequestSecurityAndAnalysis
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReposUpdateRequestSecurityAndAnalysis`
        """
        model = ReposUpdateRequestSecurityAndAnalysis()
        if include_optional:
            return ReposUpdateRequestSecurityAndAnalysis(
                advanced_security = github_openapi.models.repos_update_request_security_and_analysis_advanced_security.repos_update_request_security_and_analysis_advanced_security(
                    status = '', ),
                secret_scanning = github_openapi.models.repos_update_request_security_and_analysis_secret_scanning.repos_update_request_security_and_analysis_secret_scanning(
                    status = '', ),
                secret_scanning_push_protection = github_openapi.models.repos_update_request_security_and_analysis_secret_scanning_push_protection.repos_update_request_security_and_analysis_secret_scanning_push_protection(
                    status = '', ),
                secret_scanning_ai_detection = github_openapi.models.repos_update_request_security_and_analysis_secret_scanning_ai_detection.repos_update_request_security_and_analysis_secret_scanning_ai_detection(
                    status = '', ),
                secret_scanning_non_provider_patterns = github_openapi.models.repos_update_request_security_and_analysis_secret_scanning_non_provider_patterns.repos_update_request_security_and_analysis_secret_scanning_non_provider_patterns(
                    status = '', )
            )
        else:
            return ReposUpdateRequestSecurityAndAnalysis(
        )
        """

    def testReposUpdateRequestSecurityAndAnalysis(self):
        """Test ReposUpdateRequestSecurityAndAnalysis"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()