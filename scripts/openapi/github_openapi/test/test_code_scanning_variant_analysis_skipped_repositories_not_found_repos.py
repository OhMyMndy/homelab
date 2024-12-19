# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.code_scanning_variant_analysis_skipped_repositories_not_found_repos import CodeScanningVariantAnalysisSkippedRepositoriesNotFoundRepos

class TestCodeScanningVariantAnalysisSkippedRepositoriesNotFoundRepos(unittest.TestCase):
    """CodeScanningVariantAnalysisSkippedRepositoriesNotFoundRepos unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CodeScanningVariantAnalysisSkippedRepositoriesNotFoundRepos:
        """Test CodeScanningVariantAnalysisSkippedRepositoriesNotFoundRepos
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CodeScanningVariantAnalysisSkippedRepositoriesNotFoundRepos`
        """
        model = CodeScanningVariantAnalysisSkippedRepositoriesNotFoundRepos()
        if include_optional:
            return CodeScanningVariantAnalysisSkippedRepositoriesNotFoundRepos(
                repository_count = 2,
                repository_full_names = [
                    ''
                    ]
            )
        else:
            return CodeScanningVariantAnalysisSkippedRepositoriesNotFoundRepos(
                repository_count = 2,
                repository_full_names = [
                    ''
                    ],
        )
        """

    def testCodeScanningVariantAnalysisSkippedRepositoriesNotFoundRepos(self):
        """Test CodeScanningVariantAnalysisSkippedRepositoriesNotFoundRepos"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()