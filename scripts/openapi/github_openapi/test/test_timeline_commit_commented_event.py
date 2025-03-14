# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.timeline_commit_commented_event import TimelineCommitCommentedEvent

class TestTimelineCommitCommentedEvent(unittest.TestCase):
    """TimelineCommitCommentedEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimelineCommitCommentedEvent:
        """Test TimelineCommitCommentedEvent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimelineCommitCommentedEvent`
        """
        model = TimelineCommitCommentedEvent()
        if include_optional:
            return TimelineCommitCommentedEvent(
                event = '',
                node_id = '',
                commit_id = '',
                comments = [
                    github_openapi.models.commit_comment.Commit Comment(
                        html_url = '', 
                        url = '', 
                        id = 56, 
                        node_id = '', 
                        body = '', 
                        path = '', 
                        position = 56, 
                        line = 56, 
                        commit_id = '', 
                        user = github_openapi.models.simple_user.Simple User(
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
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        author_association = 'OWNER', 
                        reactions = github_openapi.models.reaction_rollup.Reaction Rollup(
                            url = '', 
                            total_count = 56, 
                            +1 = 56, 
                            _1 = 56, 
                            laugh = 56, 
                            confused = 56, 
                            heart = 56, 
                            hooray = 56, 
                            eyes = 56, 
                            rocket = 56, ), )
                    ]
            )
        else:
            return TimelineCommitCommentedEvent(
        )
        """

    def testTimelineCommitCommentedEvent(self):
        """Test TimelineCommitCommentedEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
