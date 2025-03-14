# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.repository_webhooks_template_repository import RepositoryWebhooksTemplateRepository

class TestRepositoryWebhooksTemplateRepository(unittest.TestCase):
    """RepositoryWebhooksTemplateRepository unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RepositoryWebhooksTemplateRepository:
        """Test RepositoryWebhooksTemplateRepository
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RepositoryWebhooksTemplateRepository`
        """
        model = RepositoryWebhooksTemplateRepository()
        if include_optional:
            return RepositoryWebhooksTemplateRepository(
                id = 56,
                node_id = '',
                name = '',
                full_name = '',
                owner = github_openapi.models.repository_webhooks_template_repository_owner.repository_webhooks_template_repository_owner(
                    login = '', 
                    id = 56, 
                    node_id = '', 
                    avatar_url = '', 
                    gravatar_id = '', 
                    url = '', 
                    html_url = '', 
                    followers_url = '', 
                    following_url = '', 
                    gists_url = '', 
                    starred_url = '', 
                    subscriptions_url = '', 
                    organizations_url = '', 
                    repos_url = '', 
                    events_url = '', 
                    received_events_url = '', 
                    type = '', 
                    site_admin = True, ),
                private = True,
                html_url = '',
                description = '',
                fork = True,
                url = '',
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
                downloads_url = '',
                events_url = '',
                forks_url = '',
                git_commits_url = '',
                git_refs_url = '',
                git_tags_url = '',
                git_url = '',
                issue_comment_url = '',
                issue_events_url = '',
                issues_url = '',
                keys_url = '',
                labels_url = '',
                languages_url = '',
                merges_url = '',
                milestones_url = '',
                notifications_url = '',
                pulls_url = '',
                releases_url = '',
                ssh_url = '',
                stargazers_url = '',
                statuses_url = '',
                subscribers_url = '',
                subscription_url = '',
                tags_url = '',
                teams_url = '',
                trees_url = '',
                clone_url = '',
                mirror_url = '',
                hooks_url = '',
                svn_url = '',
                homepage = '',
                language = '',
                forks_count = 56,
                stargazers_count = 56,
                watchers_count = 56,
                size = 56,
                default_branch = '',
                open_issues_count = 56,
                is_template = True,
                topics = [
                    ''
                    ],
                has_issues = True,
                has_projects = True,
                has_wiki = True,
                has_pages = True,
                has_downloads = True,
                archived = True,
                disabled = True,
                visibility = '',
                pushed_at = '',
                created_at = '',
                updated_at = '',
                permissions = github_openapi.models.minimal_repository_permissions.minimal_repository_permissions(
                    admin = True, 
                    maintain = True, 
                    push = True, 
                    triage = True, 
                    pull = True, ),
                allow_rebase_merge = True,
                temp_clone_token = '',
                allow_squash_merge = True,
                allow_auto_merge = True,
                delete_branch_on_merge = True,
                allow_update_branch = True,
                use_squash_pr_title_as_default = True,
                squash_merge_commit_title = 'PR_TITLE',
                squash_merge_commit_message = 'PR_BODY',
                merge_commit_title = 'PR_TITLE',
                merge_commit_message = 'PR_BODY',
                allow_merge_commit = True,
                subscribers_count = 56,
                network_count = 56
            )
        else:
            return RepositoryWebhooksTemplateRepository(
        )
        """

    def testRepositoryWebhooksTemplateRepository(self):
        """Test RepositoryWebhooksTemplateRepository"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
