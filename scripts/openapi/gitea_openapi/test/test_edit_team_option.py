# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_openapi.models.edit_team_option import EditTeamOption

class TestEditTeamOption(unittest.TestCase):
    """EditTeamOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EditTeamOption:
        """Test EditTeamOption
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EditTeamOption`
        """
        model = EditTeamOption()
        if include_optional:
            return EditTeamOption(
                can_create_org_repo = True,
                description = '',
                includes_all_repositories = True,
                name = '',
                permission = 'read',
                units = [repo.code, repo.issues, repo.ext_issues, repo.wiki, repo.pulls, repo.releases, repo.projects, repo.ext_wiki],
                units_map = {"repo.code":"read","repo.ext_issues":"none","repo.ext_wiki":"none","repo.issues":"write","repo.projects":"none","repo.pulls":"owner","repo.releases":"none","repo.wiki":"admin"}
            )
        else:
            return EditTeamOption(
                name = '',
        )
        """

    def testEditTeamOption(self):
        """Test EditTeamOption"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()