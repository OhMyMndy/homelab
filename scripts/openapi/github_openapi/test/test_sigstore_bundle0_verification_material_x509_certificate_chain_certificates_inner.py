# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.sigstore_bundle0_verification_material_x509_certificate_chain_certificates_inner import SigstoreBundle0VerificationMaterialX509CertificateChainCertificatesInner

class TestSigstoreBundle0VerificationMaterialX509CertificateChainCertificatesInner(unittest.TestCase):
    """SigstoreBundle0VerificationMaterialX509CertificateChainCertificatesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SigstoreBundle0VerificationMaterialX509CertificateChainCertificatesInner:
        """Test SigstoreBundle0VerificationMaterialX509CertificateChainCertificatesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SigstoreBundle0VerificationMaterialX509CertificateChainCertificatesInner`
        """
        model = SigstoreBundle0VerificationMaterialX509CertificateChainCertificatesInner()
        if include_optional:
            return SigstoreBundle0VerificationMaterialX509CertificateChainCertificatesInner(
                raw_bytes = ''
            )
        else:
            return SigstoreBundle0VerificationMaterialX509CertificateChainCertificatesInner(
        )
        """

    def testSigstoreBundle0VerificationMaterialX509CertificateChainCertificatesInner(self):
        """Test SigstoreBundle0VerificationMaterialX509CertificateChainCertificatesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
