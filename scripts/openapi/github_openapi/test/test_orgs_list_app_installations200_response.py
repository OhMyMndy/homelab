# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.orgs_list_app_installations200_response import OrgsListAppInstallations200Response

class TestOrgsListAppInstallations200Response(unittest.TestCase):
    """OrgsListAppInstallations200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrgsListAppInstallations200Response:
        """Test OrgsListAppInstallations200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrgsListAppInstallations200Response`
        """
        model = OrgsListAppInstallations200Response()
        if include_optional:
            return OrgsListAppInstallations200Response(
                total_count = 56,
                installations = [
                    github_openapi.models.installation.Installation(
                        id = 1, 
                        account = null, 
                        repository_selection = 'all', 
                        access_tokens_url = 'https://api.github.com/app/installations/1/access_tokens', 
                        repositories_url = 'https://api.github.com/installation/repositories', 
                        html_url = 'https://github.com/organizations/github/settings/installations/1', 
                        app_id = 1, 
                        target_id = 56, 
                        target_type = 'Organization', 
                        permissions = {"contents":"read","issues":"read","deployments":"write","single_file":"read"}, 
                        events = [
                            ''
                            ], 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        single_file_name = 'config.yaml', 
                        has_multiple_single_files = True, 
                        single_file_paths = ["config.yml",".github/issue_TEMPLATE.md"], 
                        app_slug = 'github-actions', 
                        suspended_by = github_openapi.models.simple_user.Simple User(
                            name = '', 
                            email = '', 
                            login = 'octocat', 
                            id = 1, 
                            node_id = 'MDQ6VXNlcjE=', 
                            avatar_url = 'https://github.com/images/error/octocat_happy.gif', 
                            gravatar_id = '41d064eb2195891e12d0413f63227ea7', 
                            url = 'https://api.github.com/users/octocat', 
                            html_url = 'https://github.com/octocat', 
                            followers_url = 'https://api.github.com/users/octocat/followers', 
                            following_url = 'https://api.github.com/users/octocat/following{/other_user}', 
                            gists_url = 'https://api.github.com/users/octocat/gists{/gist_id}', 
                            starred_url = 'https://api.github.com/users/octocat/starred{/owner}{/repo}', 
                            subscriptions_url = 'https://api.github.com/users/octocat/subscriptions', 
                            organizations_url = 'https://api.github.com/users/octocat/orgs', 
                            repos_url = 'https://api.github.com/users/octocat/repos', 
                            events_url = 'https://api.github.com/users/octocat/events{/privacy}', 
                            received_events_url = 'https://api.github.com/users/octocat/received_events', 
                            type = 'User', 
                            site_admin = True, 
                            starred_at = '"2020-07-09T00:17:55Z"', 
                            user_view_type = 'public', ), 
                        suspended_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        contact_email = '"test_13f1e99741e3e004@d7e1eb0bc0a1ba12.com"', )
                    ]
            )
        else:
            return OrgsListAppInstallations200Response(
                total_count = 56,
                installations = [
                    github_openapi.models.installation.Installation(
                        id = 1, 
                        account = null, 
                        repository_selection = 'all', 
                        access_tokens_url = 'https://api.github.com/app/installations/1/access_tokens', 
                        repositories_url = 'https://api.github.com/installation/repositories', 
                        html_url = 'https://github.com/organizations/github/settings/installations/1', 
                        app_id = 1, 
                        target_id = 56, 
                        target_type = 'Organization', 
                        permissions = {"contents":"read","issues":"read","deployments":"write","single_file":"read"}, 
                        events = [
                            ''
                            ], 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        single_file_name = 'config.yaml', 
                        has_multiple_single_files = True, 
                        single_file_paths = ["config.yml",".github/issue_TEMPLATE.md"], 
                        app_slug = 'github-actions', 
                        suspended_by = github_openapi.models.simple_user.Simple User(
                            name = '', 
                            email = '', 
                            login = 'octocat', 
                            id = 1, 
                            node_id = 'MDQ6VXNlcjE=', 
                            avatar_url = 'https://github.com/images/error/octocat_happy.gif', 
                            gravatar_id = '41d064eb2195891e12d0413f63227ea7', 
                            url = 'https://api.github.com/users/octocat', 
                            html_url = 'https://github.com/octocat', 
                            followers_url = 'https://api.github.com/users/octocat/followers', 
                            following_url = 'https://api.github.com/users/octocat/following{/other_user}', 
                            gists_url = 'https://api.github.com/users/octocat/gists{/gist_id}', 
                            starred_url = 'https://api.github.com/users/octocat/starred{/owner}{/repo}', 
                            subscriptions_url = 'https://api.github.com/users/octocat/subscriptions', 
                            organizations_url = 'https://api.github.com/users/octocat/orgs', 
                            repos_url = 'https://api.github.com/users/octocat/repos', 
                            events_url = 'https://api.github.com/users/octocat/events{/privacy}', 
                            received_events_url = 'https://api.github.com/users/octocat/received_events', 
                            type = 'User', 
                            site_admin = True, 
                            starred_at = '"2020-07-09T00:17:55Z"', 
                            user_view_type = 'public', ), 
                        suspended_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        contact_email = '"test_13f1e99741e3e004@d7e1eb0bc0a1ba12.com"', )
                    ],
        )
        """

    def testOrgsListAppInstallations200Response(self):
        """Test OrgsListAppInstallations200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
