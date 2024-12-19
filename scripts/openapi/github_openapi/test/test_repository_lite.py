# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.repository_lite import RepositoryLite

class TestRepositoryLite(unittest.TestCase):
    """RepositoryLite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RepositoryLite:
        """Test RepositoryLite
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RepositoryLite`
        """
        model = RepositoryLite()
        if include_optional:
            return RepositoryLite(
                archive_url = '',
                assignees_url = '',
                blobs_url = '',
                branches_url = '',
                collaborators_url = '',
                comments_url = '',
                commits_url = '',
                compare_url = '',
                contents_url = '',
                contributors_url = '',
                deployments_url = '',
                description = '',
                downloads_url = '',
                events_url = '',
                fork = True,
                forks_url = '',
                full_name = '',
                git_commits_url = '',
                git_refs_url = '',
                git_tags_url = '',
                hooks_url = '',
                html_url = '',
                id = 56,
                issue_comment_url = '',
                issue_events_url = '',
                issues_url = '',
                keys_url = '',
                labels_url = '',
                languages_url = '',
                merges_url = '',
                milestones_url = '',
                name = '',
                node_id = '',
                notifications_url = '',
                owner = github_openapi.models.user.User(
                    avatar_url = '', 
                    deleted = True, 
                    email = '', 
                    events_url = '', 
                    followers_url = '', 
                    following_url = '', 
                    gists_url = '', 
                    gravatar_id = '', 
                    html_url = '', 
                    id = 56, 
                    login = '', 
                    name = '', 
                    node_id = '', 
                    organizations_url = '', 
                    received_events_url = '', 
                    repos_url = '', 
                    site_admin = True, 
                    starred_url = '', 
                    subscriptions_url = '', 
                    type = 'Bot', 
                    url = '', 
                    user_view_type = '', ),
                private = True,
                pulls_url = '',
                releases_url = '',
                stargazers_url = '',
                statuses_url = '',
                subscribers_url = '',
                subscription_url = '',
                tags_url = '',
                teams_url = '',
                trees_url = '',
                url = ''
            )
        else:
            return RepositoryLite(
                archive_url = '',
                assignees_url = '',
                blobs_url = '',
                branches_url = '',
                collaborators_url = '',
                comments_url = '',
                commits_url = '',
                compare_url = '',
                contents_url = '',
                contributors_url = '',
                deployments_url = '',
                description = '',
                downloads_url = '',
                events_url = '',
                fork = True,
                forks_url = '',
                full_name = '',
                git_commits_url = '',
                git_refs_url = '',
                git_tags_url = '',
                hooks_url = '',
                html_url = '',
                id = 56,
                issue_comment_url = '',
                issue_events_url = '',
                issues_url = '',
                keys_url = '',
                labels_url = '',
                languages_url = '',
                merges_url = '',
                milestones_url = '',
                name = '',
                node_id = '',
                notifications_url = '',
                owner = github_openapi.models.user.User(
                    avatar_url = '', 
                    deleted = True, 
                    email = '', 
                    events_url = '', 
                    followers_url = '', 
                    following_url = '', 
                    gists_url = '', 
                    gravatar_id = '', 
                    html_url = '', 
                    id = 56, 
                    login = '', 
                    name = '', 
                    node_id = '', 
                    organizations_url = '', 
                    received_events_url = '', 
                    repos_url = '', 
                    site_admin = True, 
                    starred_url = '', 
                    subscriptions_url = '', 
                    type = 'Bot', 
                    url = '', 
                    user_view_type = '', ),
                private = True,
                pulls_url = '',
                releases_url = '',
                stargazers_url = '',
                statuses_url = '',
                subscribers_url = '',
                subscription_url = '',
                tags_url = '',
                teams_url = '',
                trees_url = '',
                url = '',
        )
        """

    def testRepositoryLite(self):
        """Test RepositoryLite"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
