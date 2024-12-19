# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.gpg_key import GpgKey

class TestGpgKey(unittest.TestCase):
    """GpgKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GpgKey:
        """Test GpgKey
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GpgKey`
        """
        model = GpgKey()
        if include_optional:
            return GpgKey(
                id = 3,
                name = 'Octocat's GPG Key',
                primary_key_id = 56,
                key_id = '3262EFF25BA0D270',
                public_key = 'xsBNBFayYZ...',
                emails = [{"email":"octocat@users.noreply.github.com","verified":true}],
                subkeys = [{"id":4,"primary_key_id":3,"key_id":"4A595D4C72EE49C7","public_key":"zsBNBFayYZ...","emails":[],"can_sign":false,"can_encrypt_comms":true,"can_encrypt_storage":true,"can_certify":false,"created_at":"2016-03-24T11:31:04-06:00","expires_at":null,"revoked":false}],
                can_sign = True,
                can_encrypt_comms = True,
                can_encrypt_storage = True,
                can_certify = True,
                created_at = '2016-03-24T11:31:04-06:00',
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                revoked = True,
                raw_key = ''
            )
        else:
            return GpgKey(
                id = 3,
                primary_key_id = 56,
                key_id = '3262EFF25BA0D270',
                public_key = 'xsBNBFayYZ...',
                emails = [{"email":"octocat@users.noreply.github.com","verified":true}],
                subkeys = [{"id":4,"primary_key_id":3,"key_id":"4A595D4C72EE49C7","public_key":"zsBNBFayYZ...","emails":[],"can_sign":false,"can_encrypt_comms":true,"can_encrypt_storage":true,"can_certify":false,"created_at":"2016-03-24T11:31:04-06:00","expires_at":null,"revoked":false}],
                can_sign = True,
                can_encrypt_comms = True,
                can_encrypt_storage = True,
                can_certify = True,
                created_at = '2016-03-24T11:31:04-06:00',
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                revoked = True,
                raw_key = '',
        )
        """

    def testGpgKey(self):
        """Test GpgKey"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
