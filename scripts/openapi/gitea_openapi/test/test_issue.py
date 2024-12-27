# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_openapi.models.issue import Issue

class TestIssue(unittest.TestCase):
    """Issue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Issue:
        """Test Issue
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Issue`
        """
        model = Issue()
        if include_optional:
            return Issue(
                assets = [
                    gitea_openapi.models.attachment.Attachment(
                        browser_download_url = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        download_count = 56, 
                        id = 56, 
                        name = '', 
                        size = 56, 
                        uuid = '', )
                    ],
                assignee = gitea_openapi.models.user.User(
                    active = True, 
                    avatar_url = '', 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    description = '', 
                    email = '', 
                    followers_count = 56, 
                    following_count = 56, 
                    full_name = '', 
                    id = 56, 
                    is_admin = True, 
                    language = '', 
                    last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    location = '', 
                    login = '', 
                    login_name = 'empty', 
                    prohibit_login = True, 
                    restricted = True, 
                    source_id = 56, 
                    starred_repos_count = 56, 
                    visibility = '', 
                    website = '', ),
                assignees = [
                    gitea_openapi.models.user.User(
                        active = True, 
                        avatar_url = '', 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        description = '', 
                        email = '', 
                        followers_count = 56, 
                        following_count = 56, 
                        full_name = '', 
                        id = 56, 
                        is_admin = True, 
                        language = '', 
                        last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        location = '', 
                        login = '', 
                        login_name = 'empty', 
                        prohibit_login = True, 
                        restricted = True, 
                        source_id = 56, 
                        starred_repos_count = 56, 
                        visibility = '', 
                        website = '', )
                    ],
                body = '',
                closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                comments = 56,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                html_url = '',
                id = 56,
                is_locked = True,
                labels = [
                    gitea_openapi.models.label.Label(
                        color = '00aabb', 
                        description = '', 
                        exclusive = False, 
                        id = 56, 
                        is_archived = False, 
                        name = '', 
                        url = '', )
                    ],
                milestone = gitea_openapi.models.milestone.Milestone(
                    closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    closed_issues = 56, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    description = '', 
                    due_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = 56, 
                    open_issues = 56, 
                    state = '', 
                    title = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                number = 56,
                original_author = '',
                original_author_id = 56,
                pin_order = 56,
                pull_request = gitea_openapi.models.pull_request_meta.PullRequestMeta(
                    draft = True, 
                    merged = True, 
                    merged_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                ref = '',
                repository = gitea_openapi.models.repository_meta.RepositoryMeta(
                    full_name = '', 
                    id = 56, 
                    name = '', 
                    owner = '', ),
                state = '',
                title = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                url = '',
                user = gitea_openapi.models.user.User(
                    active = True, 
                    avatar_url = '', 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    description = '', 
                    email = '', 
                    followers_count = 56, 
                    following_count = 56, 
                    full_name = '', 
                    id = 56, 
                    is_admin = True, 
                    language = '', 
                    last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    location = '', 
                    login = '', 
                    login_name = 'empty', 
                    prohibit_login = True, 
                    restricted = True, 
                    source_id = 56, 
                    starred_repos_count = 56, 
                    visibility = '', 
                    website = '', )
            )
        else:
            return Issue(
        )
        """

    def testIssue(self):
        """Test Issue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()