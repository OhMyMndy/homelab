# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.gist_simple_forks_inner import GistSimpleForksInner

class TestGistSimpleForksInner(unittest.TestCase):
    """GistSimpleForksInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GistSimpleForksInner:
        """Test GistSimpleForksInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GistSimpleForksInner`
        """
        model = GistSimpleForksInner()
        if include_optional:
            return GistSimpleForksInner(
                id = '',
                url = '',
                user = github_openapi.models.public_user.Public User(
                    login = '', 
                    id = 56, 
                    user_view_type = '', 
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
                    site_admin = True, 
                    name = '', 
                    company = '', 
                    blog = '', 
                    location = '', 
                    email = '', 
                    notification_email = '', 
                    hireable = True, 
                    bio = '', 
                    twitter_username = '', 
                    public_repos = 56, 
                    public_gists = 56, 
                    followers = 56, 
                    following = 56, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    plan = github_openapi.models.public_user_plan.public_user_plan(
                        collaborators = 56, 
                        name = '', 
                        space = 56, 
                        private_repos = 56, ), 
                    private_gists = 1, 
                    total_private_repos = 2, 
                    owned_private_repos = 2, 
                    disk_usage = 1, 
                    collaborators = 3, ),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return GistSimpleForksInner(
        )
        """

    def testGistSimpleForksInner(self):
        """Test GistSimpleForksInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()