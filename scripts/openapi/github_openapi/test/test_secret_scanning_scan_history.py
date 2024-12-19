# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.secret_scanning_scan_history import SecretScanningScanHistory

class TestSecretScanningScanHistory(unittest.TestCase):
    """SecretScanningScanHistory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SecretScanningScanHistory:
        """Test SecretScanningScanHistory
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SecretScanningScanHistory`
        """
        model = SecretScanningScanHistory()
        if include_optional:
            return SecretScanningScanHistory(
                incremental_scans = [
                    github_openapi.models.secret_scanning_scan.secret-scanning-scan(
                        type = '', 
                        status = '', 
                        completed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                pattern_update_scans = [
                    github_openapi.models.secret_scanning_scan.secret-scanning-scan(
                        type = '', 
                        status = '', 
                        completed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                backfill_scans = [
                    github_openapi.models.secret_scanning_scan.secret-scanning-scan(
                        type = '', 
                        status = '', 
                        completed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                custom_pattern_backfill_scans = [
                    null
                    ]
            )
        else:
            return SecretScanningScanHistory(
        )
        """

    def testSecretScanningScanHistory(self):
        """Test SecretScanningScanHistory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
