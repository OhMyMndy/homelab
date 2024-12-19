# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.dependency_graph_spdx_sbom_sbom_packages_inner_external_refs_inner import DependencyGraphSpdxSbomSbomPackagesInnerExternalRefsInner

class TestDependencyGraphSpdxSbomSbomPackagesInnerExternalRefsInner(unittest.TestCase):
    """DependencyGraphSpdxSbomSbomPackagesInnerExternalRefsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DependencyGraphSpdxSbomSbomPackagesInnerExternalRefsInner:
        """Test DependencyGraphSpdxSbomSbomPackagesInnerExternalRefsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DependencyGraphSpdxSbomSbomPackagesInnerExternalRefsInner`
        """
        model = DependencyGraphSpdxSbomSbomPackagesInnerExternalRefsInner()
        if include_optional:
            return DependencyGraphSpdxSbomSbomPackagesInnerExternalRefsInner(
                reference_category = 'PACKAGE-MANAGER',
                reference_locator = 'pkg:gem/rails@6.0.1',
                reference_type = 'purl'
            )
        else:
            return DependencyGraphSpdxSbomSbomPackagesInnerExternalRefsInner(
                reference_category = 'PACKAGE-MANAGER',
                reference_locator = 'pkg:gem/rails@6.0.1',
                reference_type = 'purl',
        )
        """

    def testDependencyGraphSpdxSbomSbomPackagesInnerExternalRefsInner(self):
        """Test DependencyGraphSpdxSbomSbomPackagesInnerExternalRefsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
