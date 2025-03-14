# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.sigstore_bundle0_verification_material_tlog_entries_inner import SigstoreBundle0VerificationMaterialTlogEntriesInner

class TestSigstoreBundle0VerificationMaterialTlogEntriesInner(unittest.TestCase):
    """SigstoreBundle0VerificationMaterialTlogEntriesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SigstoreBundle0VerificationMaterialTlogEntriesInner:
        """Test SigstoreBundle0VerificationMaterialTlogEntriesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SigstoreBundle0VerificationMaterialTlogEntriesInner`
        """
        model = SigstoreBundle0VerificationMaterialTlogEntriesInner()
        if include_optional:
            return SigstoreBundle0VerificationMaterialTlogEntriesInner(
                log_index = '',
                log_id = github_openapi.models.sigstore_bundle_0_verification_material_tlog_entries_inner_log_id.sigstore_bundle_0_verificationMaterial_tlogEntries_inner_logId(
                    key_id = '', ),
                kind_version = github_openapi.models.sigstore_bundle_0_verification_material_tlog_entries_inner_kind_version.sigstore_bundle_0_verificationMaterial_tlogEntries_inner_kindVersion(
                    kind = '', 
                    version = '', ),
                integrated_time = '',
                inclusion_promise = github_openapi.models.sigstore_bundle_0_verification_material_tlog_entries_inner_inclusion_promise.sigstore_bundle_0_verificationMaterial_tlogEntries_inner_inclusionPromise(
                    signed_entry_timestamp = '', ),
                inclusion_proof = '',
                canonicalized_body = ''
            )
        else:
            return SigstoreBundle0VerificationMaterialTlogEntriesInner(
        )
        """

    def testSigstoreBundle0VerificationMaterialTlogEntriesInner(self):
        """Test SigstoreBundle0VerificationMaterialTlogEntriesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
