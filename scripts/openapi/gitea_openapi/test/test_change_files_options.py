# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_openapi.models.change_files_options import ChangeFilesOptions

class TestChangeFilesOptions(unittest.TestCase):
    """ChangeFilesOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChangeFilesOptions:
        """Test ChangeFilesOptions
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChangeFilesOptions`
        """
        model = ChangeFilesOptions()
        if include_optional:
            return ChangeFilesOptions(
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
                files = [
                    gitea_openapi.models.change_file_operation.ChangeFileOperation(
                        content = '', 
                        from_path = '', 
                        operation = 'create', 
                        path = '', 
                        sha = '', )
                    ],
                message = '',
                new_branch = '',
                signoff = True
            )
        else:
            return ChangeFilesOptions(
                files = [
                    gitea_openapi.models.change_file_operation.ChangeFileOperation(
                        content = '', 
                        from_path = '', 
                        operation = 'create', 
                        path = '', 
                        sha = '', )
                    ],
        )
        """

    def testChangeFilesOptions(self):
        """Test ChangeFilesOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
