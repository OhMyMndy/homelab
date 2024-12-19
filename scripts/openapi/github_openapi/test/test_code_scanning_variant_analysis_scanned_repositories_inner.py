# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.code_scanning_variant_analysis_scanned_repositories_inner import CodeScanningVariantAnalysisScannedRepositoriesInner

class TestCodeScanningVariantAnalysisScannedRepositoriesInner(unittest.TestCase):
    """CodeScanningVariantAnalysisScannedRepositoriesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CodeScanningVariantAnalysisScannedRepositoriesInner:
        """Test CodeScanningVariantAnalysisScannedRepositoriesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CodeScanningVariantAnalysisScannedRepositoriesInner`
        """
        model = CodeScanningVariantAnalysisScannedRepositoriesInner()
        if include_optional:
            return CodeScanningVariantAnalysisScannedRepositoriesInner(
                repository = github_openapi.models.repository_identifier.Repository Identifier(
                    id = 1296269, 
                    name = 'Hello-World', 
                    full_name = 'octocat/Hello-World', 
                    private = True, 
                    stargazers_count = 80, 
                    updated_at = '2011-01-26T19:14:43Z', ),
                analysis_status = 'pending',
                result_count = 56,
                artifact_size_in_bytes = 56,
                failure_message = ''
            )
        else:
            return CodeScanningVariantAnalysisScannedRepositoriesInner(
                repository = github_openapi.models.repository_identifier.Repository Identifier(
                    id = 1296269, 
                    name = 'Hello-World', 
                    full_name = 'octocat/Hello-World', 
                    private = True, 
                    stargazers_count = 80, 
                    updated_at = '2011-01-26T19:14:43Z', ),
                analysis_status = 'pending',
        )
        """

    def testCodeScanningVariantAnalysisScannedRepositoriesInner(self):
        """Test CodeScanningVariantAnalysisScannedRepositoriesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
