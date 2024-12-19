# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.dependency_graph_diff_inner import DependencyGraphDiffInner

class TestDependencyGraphDiffInner(unittest.TestCase):
    """DependencyGraphDiffInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DependencyGraphDiffInner:
        """Test DependencyGraphDiffInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DependencyGraphDiffInner`
        """
        model = DependencyGraphDiffInner()
        if include_optional:
            return DependencyGraphDiffInner(
                change_type = 'added',
                manifest = 'path/to/package-lock.json',
                ecosystem = 'npm',
                name = '@actions/core',
                version = '1.0.0',
                package_url = 'pkg:/npm/%40actions/core@1.1.0',
                license = 'MIT',
                source_repository_url = 'https://github.com/github/actions',
                vulnerabilities = [
                    github_openapi.models.dependency_graph_diff_inner_vulnerabilities_inner.dependency_graph_diff_inner_vulnerabilities_inner(
                        severity = 'critical', 
                        advisory_ghsa_id = 'GHSA-rf4j-j272-fj86', 
                        advisory_summary = 'A summary of the advisory.', 
                        advisory_url = 'https://github.com/advisories/GHSA-rf4j-j272-fj86', )
                    ],
                scope = 'unknown'
            )
        else:
            return DependencyGraphDiffInner(
                change_type = 'added',
                manifest = 'path/to/package-lock.json',
                ecosystem = 'npm',
                name = '@actions/core',
                version = '1.0.0',
                package_url = 'pkg:/npm/%40actions/core@1.1.0',
                license = 'MIT',
                source_repository_url = 'https://github.com/github/actions',
                vulnerabilities = [
                    github_openapi.models.dependency_graph_diff_inner_vulnerabilities_inner.dependency_graph_diff_inner_vulnerabilities_inner(
                        severity = 'critical', 
                        advisory_ghsa_id = 'GHSA-rf4j-j272-fj86', 
                        advisory_summary = 'A summary of the advisory.', 
                        advisory_url = 'https://github.com/advisories/GHSA-rf4j-j272-fj86', )
                    ],
                scope = 'unknown',
        )
        """

    def testDependencyGraphDiffInner(self):
        """Test DependencyGraphDiffInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()