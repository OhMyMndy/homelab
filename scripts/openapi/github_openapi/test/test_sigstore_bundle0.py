# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.sigstore_bundle0 import SigstoreBundle0

class TestSigstoreBundle0(unittest.TestCase):
    """SigstoreBundle0 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SigstoreBundle0:
        """Test SigstoreBundle0
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SigstoreBundle0`
        """
        model = SigstoreBundle0()
        if include_optional:
            return SigstoreBundle0(
                media_type = '',
                verification_material = github_openapi.models.sigstore_bundle_0_verification_material.sigstore_bundle_0_verificationMaterial(
                    x509_certificate_chain = github_openapi.models.sigstore_bundle_0_verification_material_x509_certificate_chain.sigstore_bundle_0_verificationMaterial_x509CertificateChain(
                        certificates = [
                            github_openapi.models.sigstore_bundle_0_verification_material_x509_certificate_chain_certificates_inner.sigstore_bundle_0_verificationMaterial_x509CertificateChain_certificates_inner(
                                raw_bytes = '', )
                            ], ), 
                    tlog_entries = [
                        github_openapi.models.sigstore_bundle_0_verification_material_tlog_entries_inner.sigstore_bundle_0_verificationMaterial_tlogEntries_inner(
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
                            canonicalized_body = '', )
                        ], 
                    timestamp_verification_data = '', ),
                dsse_envelope = github_openapi.models.sigstore_bundle_0_dsse_envelope.sigstore_bundle_0_dsseEnvelope(
                    payload = '', 
                    payload_type = '', 
                    signatures = [
                        github_openapi.models.sigstore_bundle_0_dsse_envelope_signatures_inner.sigstore_bundle_0_dsseEnvelope_signatures_inner(
                            sig = '', 
                            keyid = '', )
                        ], )
            )
        else:
            return SigstoreBundle0(
        )
        """

    def testSigstoreBundle0(self):
        """Test SigstoreBundle0"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()