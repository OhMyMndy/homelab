# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.sigstore_bundle0_verification_material_tlog_entries_inner_inclusion_promise import SigstoreBundle0VerificationMaterialTlogEntriesInnerInclusionPromise

class TestSigstoreBundle0VerificationMaterialTlogEntriesInnerInclusionPromise(unittest.TestCase):
    """SigstoreBundle0VerificationMaterialTlogEntriesInnerInclusionPromise unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SigstoreBundle0VerificationMaterialTlogEntriesInnerInclusionPromise:
        """Test SigstoreBundle0VerificationMaterialTlogEntriesInnerInclusionPromise
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SigstoreBundle0VerificationMaterialTlogEntriesInnerInclusionPromise`
        """
        model = SigstoreBundle0VerificationMaterialTlogEntriesInnerInclusionPromise()
        if include_optional:
            return SigstoreBundle0VerificationMaterialTlogEntriesInnerInclusionPromise(
                signed_entry_timestamp = ''
            )
        else:
            return SigstoreBundle0VerificationMaterialTlogEntriesInnerInclusionPromise(
        )
        """

    def testSigstoreBundle0VerificationMaterialTlogEntriesInnerInclusionPromise(self):
        """Test SigstoreBundle0VerificationMaterialTlogEntriesInnerInclusionPromise"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()