# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.actions_list_repo_access_to_self_hosted_runner_group_in_org200_response import ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response

class TestActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response(unittest.TestCase):
    """ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response:
        """Test ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response`
        """
        model = ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response()
        if include_optional:
            return ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response(
                total_count = 1.337,
                repositories = [
                    github_openapi.models.minimal_repository.Minimal Repository(
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
                            secret_scanning_ai_detection = , ), )
                    ]
            )
        else:
            return ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response(
                total_count = 1.337,
                repositories = [
                    github_openapi.models.minimal_repository.Minimal Repository(
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
                            secret_scanning_ai_detection = , ), )
                    ],
        )
        """

    def testActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response(self):
        """Test ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
