# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_openapi.models.delete_file_options import DeleteFileOptions

class TestDeleteFileOptions(unittest.TestCase):
    """DeleteFileOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeleteFileOptions:
        """Test DeleteFileOptions
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeleteFileOptions`
        """
        model = DeleteFileOptions()
        if include_optional:
            return DeleteFileOptions(
                author = gitea_openapi.models.identity.Identity(
                    email = '', 
                    name = '', ),
                branch = '',
                committer = gitea_openapi.models.identity.Identity(
                    email = '', 
                    name = '', ),
                dates = gitea_openapi.models.commit_date_options.CommitDateOptions(
                    author = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    committer = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                message = '',
                new_branch = '',
                sha = '',
                signoff = True
            )
        else:
            return DeleteFileOptions(
                sha = '',
        )
        """

    def testDeleteFileOptions(self):
        """Test DeleteFileOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()