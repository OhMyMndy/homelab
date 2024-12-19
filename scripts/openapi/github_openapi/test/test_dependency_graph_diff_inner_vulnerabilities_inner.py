# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.dependency_graph_diff_inner_vulnerabilities_inner import DependencyGraphDiffInnerVulnerabilitiesInner

class TestDependencyGraphDiffInnerVulnerabilitiesInner(unittest.TestCase):
    """DependencyGraphDiffInnerVulnerabilitiesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DependencyGraphDiffInnerVulnerabilitiesInner:
        """Test DependencyGraphDiffInnerVulnerabilitiesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DependencyGraphDiffInnerVulnerabilitiesInner`
        """
        model = DependencyGraphDiffInnerVulnerabilitiesInner()
        if include_optional:
            return DependencyGraphDiffInnerVulnerabilitiesInner(
                severity = 'critical',
                advisory_ghsa_id = 'GHSA-rf4j-j272-fj86',
                advisory_summary = 'A summary of the advisory.',
                advisory_url = 'https://github.com/advisories/GHSA-rf4j-j272-fj86'
            )
        else:
            return DependencyGraphDiffInnerVulnerabilitiesInner(
                severity = 'critical',
                advisory_ghsa_id = 'GHSA-rf4j-j272-fj86',
                advisory_summary = 'A summary of the advisory.',
                advisory_url = 'https://github.com/advisories/GHSA-rf4j-j272-fj86',
        )
        """

    def testDependencyGraphDiffInnerVulnerabilitiesInner(self):
        """Test DependencyGraphDiffInnerVulnerabilitiesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()