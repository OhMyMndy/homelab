# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.sigstore_bundle0_dsse_envelope import SigstoreBundle0DsseEnvelope

class TestSigstoreBundle0DsseEnvelope(unittest.TestCase):
    """SigstoreBundle0DsseEnvelope unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SigstoreBundle0DsseEnvelope:
        """Test SigstoreBundle0DsseEnvelope
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SigstoreBundle0DsseEnvelope`
        """
        model = SigstoreBundle0DsseEnvelope()
        if include_optional:
            return SigstoreBundle0DsseEnvelope(
                payload = '',
                payload_type = '',
                signatures = [
                    github_openapi.models.sigstore_bundle_0_dsse_envelope_signatures_inner.sigstore_bundle_0_dsseEnvelope_signatures_inner(
                        sig = '', 
                        keyid = '', )
                    ]
            )
        else:
            return SigstoreBundle0DsseEnvelope(
        )
        """

    def testSigstoreBundle0DsseEnvelope(self):
        """Test SigstoreBundle0DsseEnvelope"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
