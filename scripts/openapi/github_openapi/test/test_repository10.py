# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.repository10 import Repository10

class TestRepository10(unittest.TestCase):
    """Repository10 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Repository10:
        """Test Repository10
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Repository10`
        """
        model = Repository10()
        if include_optional:
            return Repository10(
                allow_auto_merge = True,
                allow_forking = True,
                allow_merge_commit = True,
                allow_rebase_merge = True,
                allow_squash_merge = True,
                allow_update_branch = True,
                archive_url = '',
                archived = True,
                assignees_url = '',
                blobs_url = '',
                branches_url = '',
                clone_url = '',
                collaborators_url = '',
                comments_url = '',
                commits_url = '',
                compare_url = '',
                contents_url = '',
                contributors_url = '',
                created_at = None,
                default_branch = '',
                delete_branch_on_merge = True,
                deployments_url = '',
                description = '',
                disabled = True,
                downloads_url = '',
                events_url = '',
                fork = True,
                forks = 56,
                forks_count = 56,
                forks_url = '',
                full_name = '',
                git_commits_url = '',
                git_refs_url = '',
                git_tags_url = '',
                git_url = '',
                has_downloads = True,
                has_issues = True,
                has_pages = True,
                has_projects = True,
                has_wiki = True,
                has_discussions = True,
                homepage = '',
                hooks_url = '',
                html_url = '',
                id = 56,
                is_template = True,
                issue_comment_url = '',
                issue_events_url = '',
                issues_url = '',
                keys_url = '',
                labels_url = '',
                language = '',
                languages_url = '',
                license = github_openapi.models.license.License(
                    key = '', 
                    name = '', 
                    node_id = '', 
                    spdx_id = '', 
                    url = '', ),
                master_branch = '',
                merge_commit_message = 'PR_BODY',
                merge_commit_title = 'PR_TITLE',
                merges_url = '',
                milestones_url = '',
                mirror_url = '',
                name = '',
                node_id = '',
                notifications_url = '',
                open_issues = 56,
                open_issues_count = 56,
                organization = '',
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
                permissions = github_openapi.models.repository_permissions.Repository_permissions(
                    admin = True, 
                    maintain = True, 
                    pull = True, 
                    push = True, 
                    triage = True, ),
                private = True,
                public = True,
                pulls_url = '',
                pushed_at = None,
                releases_url = '',
                role_name = '',
                size = 56,
                squash_merge_commit_message = 'PR_BODY',
                squash_merge_commit_title = 'PR_TITLE',
                ssh_url = '',
                stargazers = 56,
                stargazers_count = 56,
                stargazers_url = '',
                statuses_url = '',
                subscribers_url = '',
                subscription_url = '',
                svn_url = '',
                tags_url = '',
                teams_url = '',
                topics = [
                    ''
                    ],
                trees_url = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                url = '',
                use_squash_pr_title_as_default = True,
                visibility = 'public',
                watchers = 56,
                watchers_count = 56,
                web_commit_signoff_required = True
            )
        else:
            return Repository10(
                archive_url = '',
                archived = True,
                assignees_url = '',
                blobs_url = '',
                branches_url = '',
                clone_url = '',
                collaborators_url = '',
                comments_url = '',
                commits_url = '',
                compare_url = '',
                contents_url = '',
                contributors_url = '',
                created_at = None,
                default_branch = '',
                deployments_url = '',
                description = '',
                downloads_url = '',
                events_url = '',
                fork = True,
                forks = 56,
                forks_count = 56,
                forks_url = '',
                full_name = '',
                git_commits_url = '',
                git_refs_url = '',
                git_tags_url = '',
                git_url = '',
                has_downloads = True,
                has_issues = True,
                has_pages = True,
                has_projects = True,
                has_wiki = True,
                has_discussions = True,
                homepage = '',
                hooks_url = '',
                html_url = '',
                id = 56,
                issue_comment_url = '',
                issue_events_url = '',
                issues_url = '',
                keys_url = '',
                labels_url = '',
                language = '',
                languages_url = '',
                license = github_openapi.models.license.License(
                    key = '', 
                    name = '', 
                    node_id = '', 
                    spdx_id = '', 
                    url = '', ),
                merges_url = '',
                milestones_url = '',
                mirror_url = '',
                name = '',
                node_id = '',
                notifications_url = '',
                open_issues = 56,
                open_issues_count = 56,
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
                pushed_at = None,
                releases_url = '',
                size = 56,
                ssh_url = '',
                stargazers_count = 56,
                stargazers_url = '',
                statuses_url = '',
                subscribers_url = '',
                subscription_url = '',
                svn_url = '',
                tags_url = '',
                teams_url = '',
                topics = [
                    ''
                    ],
                trees_url = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                url = '',
                visibility = 'public',
                watchers = 56,
                watchers_count = 56,
        )
        """

    def testRepository10(self):
        """Test Repository10"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
