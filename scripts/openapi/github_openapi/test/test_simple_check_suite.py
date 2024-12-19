# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.simple_check_suite import SimpleCheckSuite

class TestSimpleCheckSuite(unittest.TestCase):
    """SimpleCheckSuite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SimpleCheckSuite:
        """Test SimpleCheckSuite
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SimpleCheckSuite`
        """
        model = SimpleCheckSuite()
        if include_optional:
            return SimpleCheckSuite(
                after = 'd6fde92930d4715a2b49857d24b940956b26d2d3',
                app = github_openapi.models.git_hub_app.GitHub app(
                    id = 37, 
                    slug = 'probot-owners', 
                    node_id = 'MDExOkludGVncmF0aW9uMQ==', 
                    client_id = '"Iv1.25b5d1e65ffc4022"', 
                    owner = github_openapi.models.simple_user.Simple User(
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
                    name = 'Probot Owners', 
                    description = 'The description of the app.', 
                    external_url = 'https://example.com', 
                    html_url = 'https://github.com/apps/super-ci', 
                    created_at = '2017-07-08T16:18:44-04:00', 
                    updated_at = '2017-07-08T16:18:44-04:00', 
                    permissions = {"issues":"read","deployments":"write"}, 
                    events = ["label","deployment"], 
                    installations_count = 5, 
                    client_secret = '"1d4b2097ac622ba702d19de498f005747a8b21d3"', 
                    webhook_secret = '"6fba8f2fc8a7e8f2cca5577eddd82ca7586b3b6b"', 
                    pem = '"-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEArYxrNYD/iT5CZVpRJu4rBKmmze3PVmT/gCo2ATUvDvZTPTey\nxcGJ3vvrJXazKk06pN05TN29o98jrYz4cengG3YGsXPNEpKsIrEl8NhbnxapEnM9\nJCMRe0P5JcPsfZlX6hmiT7136GRWiGOUba2X9+HKh8QJVLG5rM007TBER9/z9mWm\nrJuNh+m5l320oBQY/Qq3A7wzdEfZw8qm/mIN0FCeoXH1L6B8xXWaAYBwhTEh6SSn\nZHlO1Xu1JWDmAvBCi0RO5aRSKM8q9QEkvvHP4yweAtK3N8+aAbZ7ovaDhyGz8r6r\nzhU1b8Uo0Z2ysf503WqzQgIajr7Fry7/kUwpgQIDAQABAoIBADwJp80Ko1xHPZDy\nfcCKBDfIuPvkmSW6KumbsLMaQv1aGdHDwwTGv3t0ixSay8CGlxMRtRDyZPib6SvQ\n6OH/lpfpbMdW2ErkksgtoIKBVrDilfrcAvrNZu7NxRNbhCSvN8q0s4ICecjbbVQh\nnueSdlA6vGXbW58BHMq68uRbHkP+k+mM9U0mDJ1HMch67wlg5GbayVRt63H7R2+r\nVxcna7B80J/lCEjIYZznawgiTvp3MSanTglqAYi+m1EcSsP14bJIB9vgaxS79kTu\noiSo93leJbBvuGo8QEiUqTwMw4tDksmkLsoqNKQ1q9P7LZ9DGcujtPy4EZsamSJT\ny8OJt0ECgYEA2lxOxJsQk2kI325JgKFjo92mQeUObIvPfSNWUIZQDTjniOI6Gv63\nGLWVFrZcvQBWjMEQraJA9xjPbblV8PtfO87MiJGLWCHFxmPz2dzoedN+2Coxom8m\nV95CLz8QUShuao6u/RYcvUaZEoYs5bHcTmy5sBK80JyEmafJPtCQVxMCgYEAy3ar\nZr3yv4xRPEPMat4rseswmuMooSaK3SKub19WFI5IAtB/e7qR1Rj9JhOGcZz+OQrl\nT78O2OFYlgOIkJPvRMrPpK5V9lslc7tz1FSh3BZMRGq5jSyD7ETSOQ0c8T2O/s7v\nbeEPbVbDe4mwvM24XByH0GnWveVxaDl51ABD65sCgYB3ZAspUkOA5egVCh8kNpnd\nSd6SnuQBE3ySRlT2WEnCwP9Ph6oPgn+oAfiPX4xbRqkL8q/k0BdHQ4h+zNwhk7+h\nWtPYRAP1Xxnc/F+jGjb+DVaIaKGU18MWPg7f+FI6nampl3Q0KvfxwX0GdNhtio8T\nTj1E+SnFwh56SRQuxSh2gwKBgHKjlIO5NtNSflsUYFM+hyQiPiqnHzddfhSG+/3o\nm5nNaSmczJesUYreH5San7/YEy2UxAugvP7aSY2MxB+iGsiJ9WD2kZzTUlDZJ7RV\nUzWsoqBR+eZfVJ2FUWWvy8TpSG6trh4dFxImNtKejCR1TREpSiTV3Zb1dmahK9GV\nrK9NAoGAbBxRLoC01xfxCTgt5BDiBcFVh4fp5yYKwavJPLzHSpuDOrrI9jDn1oKN\nonq5sDU1i391zfQvdrbX4Ova48BN+B7p63FocP/MK5tyyBoT8zQEk2+vWDOw7H/Z\nu5dTCPxTIsoIwUw1I+7yIxqJzLPFgR2gVBwY1ra/8iAqCj+zeBw=\n-----END RSA PRIVATE KEY-----\n"', ),
                before = '146e867f55c26428e5f9fade55a9bbf5e95a7912',
                conclusion = 'neutral',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                head_branch = 'master',
                head_sha = '009b8a3a9ccbb128af87f9b1c0f4c62e8a304f6d',
                id = 5,
                node_id = 'MDEwOkNoZWNrU3VpdGU1',
                pull_requests = [
                    github_openapi.models.pull_request_minimal.Pull Request Minimal(
                        id = 56, 
                        number = 56, 
                        url = '', 
                        head = github_openapi.models.pull_request_minimal_head.pull_request_minimal_head(
                            ref = '', 
                            sha = '', 
                            repo = github_openapi.models.pull_request_minimal_head_repo.pull_request_minimal_head_repo(
                                id = 56, 
                                url = '', 
                                name = '', ), ), 
                        base = github_openapi.models.pull_request_minimal_head.pull_request_minimal_head(
                            ref = '', 
                            sha = '', 
                            repo = github_openapi.models.pull_request_minimal_head_repo.pull_request_minimal_head_repo(
                                id = 56, 
                                url = '', 
                                name = '', ), ), )
                    ],
                repository = github_openapi.models.minimal_repository.Minimal Repository(
                    id = 1296269, 
                    node_id = 'MDEwOlJlcG9zaXRvcnkxMjk2MjY5', 
                    name = 'Hello-World', 
                    full_name = 'octocat/Hello-World', 
                    owner = github_openapi.models.simple_user.Simple User(
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
                    private = True, 
                    html_url = 'https://github.com/octocat/Hello-World', 
                    description = 'This your first repo!', 
                    fork = True, 
                    url = 'https://api.github.com/repos/octocat/Hello-World', 
                    archive_url = 'http://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}', 
                    assignees_url = 'http://api.github.com/repos/octocat/Hello-World/assignees{/user}', 
                    blobs_url = 'http://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}', 
                    branches_url = 'http://api.github.com/repos/octocat/Hello-World/branches{/branch}', 
                    collaborators_url = 'http://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}', 
                    comments_url = 'http://api.github.com/repos/octocat/Hello-World/comments{/number}', 
                    commits_url = 'http://api.github.com/repos/octocat/Hello-World/commits{/sha}', 
                    compare_url = 'http://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}', 
                    contents_url = 'http://api.github.com/repos/octocat/Hello-World/contents/{+path}', 
                    contributors_url = 'http://api.github.com/repos/octocat/Hello-World/contributors', 
                    deployments_url = 'http://api.github.com/repos/octocat/Hello-World/deployments', 
                    downloads_url = 'http://api.github.com/repos/octocat/Hello-World/downloads', 
                    events_url = 'http://api.github.com/repos/octocat/Hello-World/events', 
                    forks_url = 'http://api.github.com/repos/octocat/Hello-World/forks', 
                    git_commits_url = 'http://api.github.com/repos/octocat/Hello-World/git/commits{/sha}', 
                    git_refs_url = 'http://api.github.com/repos/octocat/Hello-World/git/refs{/sha}', 
                    git_tags_url = 'http://api.github.com/repos/octocat/Hello-World/git/tags{/sha}', 
                    git_url = '', 
                    issue_comment_url = 'http://api.github.com/repos/octocat/Hello-World/issues/comments{/number}', 
                    issue_events_url = 'http://api.github.com/repos/octocat/Hello-World/issues/events{/number}', 
                    issues_url = 'http://api.github.com/repos/octocat/Hello-World/issues{/number}', 
                    keys_url = 'http://api.github.com/repos/octocat/Hello-World/keys{/key_id}', 
                    labels_url = 'http://api.github.com/repos/octocat/Hello-World/labels{/name}', 
                    languages_url = 'http://api.github.com/repos/octocat/Hello-World/languages', 
                    merges_url = 'http://api.github.com/repos/octocat/Hello-World/merges', 
                    milestones_url = 'http://api.github.com/repos/octocat/Hello-World/milestones{/number}', 
                    notifications_url = 'http://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}', 
                    pulls_url = 'http://api.github.com/repos/octocat/Hello-World/pulls{/number}', 
                    releases_url = 'http://api.github.com/repos/octocat/Hello-World/releases{/id}', 
                    ssh_url = '', 
                    stargazers_url = 'http://api.github.com/repos/octocat/Hello-World/stargazers', 
                    statuses_url = 'http://api.github.com/repos/octocat/Hello-World/statuses/{sha}', 
                    subscribers_url = 'http://api.github.com/repos/octocat/Hello-World/subscribers', 
                    subscription_url = 'http://api.github.com/repos/octocat/Hello-World/subscription', 
                    tags_url = 'http://api.github.com/repos/octocat/Hello-World/tags', 
                    teams_url = 'http://api.github.com/repos/octocat/Hello-World/teams', 
                    trees_url = 'http://api.github.com/repos/octocat/Hello-World/git/trees{/sha}', 
                    clone_url = '', 
                    mirror_url = '', 
                    hooks_url = 'http://api.github.com/repos/octocat/Hello-World/hooks', 
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
                    has_discussions = True, 
                    archived = True, 
                    disabled = True, 
                    visibility = '', 
                    pushed_at = '2011-01-26T19:06:43Z', 
                    created_at = '2011-01-26T19:01:12Z', 
                    updated_at = '2011-01-26T19:14:43Z', 
                    permissions = github_openapi.models.minimal_repository_permissions.minimal_repository_permissions(
                        admin = True, 
                        maintain = True, 
                        push = True, 
                        triage = True, 
                        pull = True, ), 
                    role_name = 'admin', 
                    temp_clone_token = '', 
                    delete_branch_on_merge = True, 
                    subscribers_count = 56, 
                    network_count = 56, 
                    code_of_conduct = github_openapi.models.code_of_conduct.Code Of Conduct(
                        key = 'contributor_covenant', 
                        name = 'Contributor Covenant', 
                        url = 'https://api.github.com/codes_of_conduct/contributor_covenant', 
                        body = '# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response
                  to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other behaviors that they deem inappropriate, threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces when an individual is representing the project or its community. Examples of representing a project or community include using an official project e-mail address,
                  posting via an official social media account, or acting as an appointed representative at an online or offline event. Representation of a project may be further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team at [EMAIL]. The project team will review and investigate all complaints, and will respond in a way that it deems appropriate to the circumstances. The project team is obligated to maintain confidentiality with regard to the reporter of an incident. Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good faith may face temporary or permanent repercussions as determined by other members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant](http://contributor-covenant.org), version 1.4, available at [http://contributor-covenant.org/version/1/4](http://contributor-covenant.org/version/1/4/).
', 
                        html_url = '', ), 
                    license = github_openapi.models.minimal_repository_license.minimal_repository_license(
                        key = '', 
                        name = '', 
                        spdx_id = '', 
                        url = '', 
                        node_id = '', ), 
                    forks = 0, 
                    open_issues = 0, 
                    watchers = 0, 
                    allow_forking = True, 
                    web_commit_signoff_required = False, 
                    security_and_analysis = github_openapi.models.security_and_analysis.security-and-analysis(
                        advanced_security = github_openapi.models.security_and_analysis_advanced_security.security_and_analysis_advanced_security(
                            status = 'enabled', ), 
                        dependabot_security_updates = github_openapi.models.security_and_analysis_dependabot_security_updates.security_and_analysis_dependabot_security_updates(
                            status = 'enabled', ), 
                        secret_scanning = github_openapi.models.security_and_analysis_advanced_security.security_and_analysis_advanced_security(
                            status = 'enabled', ), 
                        secret_scanning_push_protection = , 
                        secret_scanning_non_provider_patterns = , 
                        secret_scanning_ai_detection = , ), ),
                status = 'completed',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                url = 'https://api.github.com/repos/github/hello-world/check-suites/5'
            )
        else:
            return SimpleCheckSuite(
        )
        """

    def testSimpleCheckSuite(self):
        """Test SimpleCheckSuite"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
