# coding: utf-8

"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2024.6.4
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from authentik_openapi.models.paginated_certificate_key_pair_list import PaginatedCertificateKeyPairList

class TestPaginatedCertificateKeyPairList(unittest.TestCase):
    """PaginatedCertificateKeyPairList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedCertificateKeyPairList:
        """Test PaginatedCertificateKeyPairList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedCertificateKeyPairList`
        """
        model = PaginatedCertificateKeyPairList()
        if include_optional:
            return PaginatedCertificateKeyPairList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.certificate_key_pair.CertificateKeyPair(
                        pk = '', 
                        name = '', 
                        fingerprint_sha256 = '', 
                        fingerprint_sha1 = '', 
                        cert_expiry = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        cert_subject = '', 
                        private_key_available = True, 
                        private_key_type = '', 
                        certificate_download_url = '', 
                        private_key_download_url = '', 
                        managed = '', )
                    ]
            )
        else:
            return PaginatedCertificateKeyPairList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.certificate_key_pair.CertificateKeyPair(
                        pk = '', 
                        name = '', 
                        fingerprint_sha256 = '', 
                        fingerprint_sha1 = '', 
                        cert_expiry = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        cert_subject = '', 
                        private_key_available = True, 
                        private_key_type = '', 
                        certificate_download_url = '', 
                        private_key_download_url = '', 
                        managed = '', )
                    ],
        )
        """

    def testPaginatedCertificateKeyPairList(self):
        """Test PaginatedCertificateKeyPairList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
