# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_openapi.models.pull_request import PullRequest

class TestPullRequest(unittest.TestCase):
    """PullRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PullRequest:
        """Test PullRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PullRequest`
        """
        model = PullRequest()
        if include_optional:
            return PullRequest(
                allow_maintainer_edit = True,
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
                base = gitea_openapi.models.pr_branch_info.PRBranchInfo(
                    label = '', 
                    ref = '', 
                    repo = gitea_openapi.models.repository.Repository(
                        allow_fast_forward_only_merge = True, 
                        allow_merge_commits = True, 
                        allow_rebase = True, 
                        allow_rebase_explicit = True, 
                        allow_rebase_update = True, 
                        allow_squash_merge = True, 
                        archived = True, 
                        archived_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        avatar_url = '', 
                        clone_url = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        default_allow_maintainer_edit = True, 
                        default_branch = '', 
                        default_delete_branch_after_merge = True, 
                        default_merge_style = '', 
                        description = '', 
                        empty = True, 
                        external_tracker = gitea_openapi.models.external_tracker.ExternalTracker(
                            external_tracker_format = '', 
                            external_tracker_regexp_pattern = '', 
                            external_tracker_style = '', 
                            external_tracker_url = '', ), 
                        external_wiki = gitea_openapi.models.external_wiki.ExternalWiki(
                            external_wiki_url = '', ), 
                        fork = True, 
                        forks_count = 56, 
                        full_name = '', 
                        has_actions = True, 
                        has_issues = True, 
                        has_packages = True, 
                        has_projects = True, 
                        has_pull_requests = True, 
                        has_releases = True, 
                        has_wiki = True, 
                        html_url = '', 
                        id = 56, 
                        ignore_whitespace_conflicts = True, 
                        internal = True, 
                        internal_tracker = gitea_openapi.models.internal_tracker.InternalTracker(
                            allow_only_contributors_to_track_time = True, 
                            enable_issue_dependencies = True, 
                            enable_time_tracker = True, ), 
                        language = '', 
                        languages_url = '', 
                        link = '', 
                        mirror = True, 
                        mirror_interval = '', 
                        mirror_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        object_format_name = 'sha1', 
                        open_issues_count = 56, 
                        open_pr_counter = 56, 
                        original_url = '', 
                        owner = gitea_openapi.models.user.User(
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
                        parent = gitea_openapi.models.repository.Repository(
                            allow_fast_forward_only_merge = True, 
                            allow_merge_commits = True, 
                            allow_rebase = True, 
                            allow_rebase_explicit = True, 
                            allow_rebase_update = True, 
                            allow_squash_merge = True, 
                            archived = True, 
                            archived_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            avatar_url = '', 
                            clone_url = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            default_allow_maintainer_edit = True, 
                            default_branch = '', 
                            default_delete_branch_after_merge = True, 
                            default_merge_style = '', 
                            description = '', 
                            empty = True, 
                            fork = True, 
                            forks_count = 56, 
                            full_name = '', 
                            has_actions = True, 
                            has_issues = True, 
                            has_packages = True, 
                            has_projects = True, 
                            has_pull_requests = True, 
                            has_releases = True, 
                            has_wiki = True, 
                            html_url = '', 
                            id = 56, 
                            ignore_whitespace_conflicts = True, 
                            internal = True, 
                            language = '', 
                            languages_url = '', 
                            link = '', 
                            mirror = True, 
                            mirror_interval = '', 
                            mirror_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            name = '', 
                            object_format_name = 'sha1', 
                            open_issues_count = 56, 
                            open_pr_counter = 56, 
                            original_url = '', 
                            permissions = gitea_openapi.models.permission.Permission(
                                admin = True, 
                                pull = True, 
                                push = True, ), 
                            private = True, 
                            projects_mode = '', 
                            release_counter = 56, 
                            repo_transfer = gitea_openapi.models.repo_transfer.RepoTransfer(
                                doer = gitea_openapi.models.user.User(
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
                                recipient = , 
                                teams = [
                                    gitea_openapi.models.team.Team(
                                        can_create_org_repo = True, 
                                        description = '', 
                                        id = 56, 
                                        includes_all_repositories = True, 
                                        name = '', 
                                        organization = gitea_openapi.models.organization.Organization(
                                            avatar_url = '', 
                                            description = '', 
                                            email = '', 
                                            full_name = '', 
                                            id = 56, 
                                            location = '', 
                                            name = '', 
                                            repo_admin_change_team_access = True, 
                                            username = '', 
                                            visibility = '', 
                                            website = '', ), 
                                        permission = 'none', 
                                        units = [repo.code, repo.issues, repo.ext_issues, repo.wiki, repo.pulls, repo.releases, repo.projects, repo.ext_wiki], 
                                        units_map = {"repo.code":"read","repo.ext_issues":"none","repo.ext_wiki":"none","repo.issues":"write","repo.projects":"none","repo.pulls":"owner","repo.releases":"none","repo.wiki":"admin"}, )
                                    ], ), 
                            size = 56, 
                            ssh_url = '', 
                            stars_count = 56, 
                            template = True, 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            url = '', 
                            watchers_count = 56, 
                            website = '', ), 
                        permissions = gitea_openapi.models.permission.Permission(
                            admin = True, 
                            pull = True, 
                            push = True, ), 
                        private = True, 
                        projects_mode = '', 
                        release_counter = 56, 
                        repo_transfer = gitea_openapi.models.repo_transfer.RepoTransfer(), 
                        size = 56, 
                        ssh_url = '', 
                        stars_count = 56, 
                        template = True, 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        url = '', 
                        watchers_count = 56, 
                        website = '', ), 
                    repo_id = 56, 
                    sha = '', ),
                body = '',
                closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                comments = 56,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                diff_url = '',
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                head = gitea_openapi.models.pr_branch_info.PRBranchInfo(
                    label = '', 
                    ref = '', 
                    repo = gitea_openapi.models.repository.Repository(
                        allow_fast_forward_only_merge = True, 
                        allow_merge_commits = True, 
                        allow_rebase = True, 
                        allow_rebase_explicit = True, 
                        allow_rebase_update = True, 
                        allow_squash_merge = True, 
                        archived = True, 
                        archived_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        avatar_url = '', 
                        clone_url = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        default_allow_maintainer_edit = True, 
                        default_branch = '', 
                        default_delete_branch_after_merge = True, 
                        default_merge_style = '', 
                        description = '', 
                        empty = True, 
                        external_tracker = gitea_openapi.models.external_tracker.ExternalTracker(
                            external_tracker_format = '', 
                            external_tracker_regexp_pattern = '', 
                            external_tracker_style = '', 
                            external_tracker_url = '', ), 
                        external_wiki = gitea_openapi.models.external_wiki.ExternalWiki(
                            external_wiki_url = '', ), 
                        fork = True, 
                        forks_count = 56, 
                        full_name = '', 
                        has_actions = True, 
                        has_issues = True, 
                        has_packages = True, 
                        has_projects = True, 
                        has_pull_requests = True, 
                        has_releases = True, 
                        has_wiki = True, 
                        html_url = '', 
                        id = 56, 
                        ignore_whitespace_conflicts = True, 
                        internal = True, 
                        internal_tracker = gitea_openapi.models.internal_tracker.InternalTracker(
                            allow_only_contributors_to_track_time = True, 
                            enable_issue_dependencies = True, 
                            enable_time_tracker = True, ), 
                        language = '', 
                        languages_url = '', 
                        link = '', 
                        mirror = True, 
                        mirror_interval = '', 
                        mirror_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        object_format_name = 'sha1', 
                        open_issues_count = 56, 
                        open_pr_counter = 56, 
                        original_url = '', 
                        owner = gitea_openapi.models.user.User(
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
                        parent = gitea_openapi.models.repository.Repository(
                            allow_fast_forward_only_merge = True, 
                            allow_merge_commits = True, 
                            allow_rebase = True, 
                            allow_rebase_explicit = True, 
                            allow_rebase_update = True, 
                            allow_squash_merge = True, 
                            archived = True, 
                            archived_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            avatar_url = '', 
                            clone_url = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            default_allow_maintainer_edit = True, 
                            default_branch = '', 
                            default_delete_branch_after_merge = True, 
                            default_merge_style = '', 
                            description = '', 
                            empty = True, 
                            fork = True, 
                            forks_count = 56, 
                            full_name = '', 
                            has_actions = True, 
                            has_issues = True, 
                            has_packages = True, 
                            has_projects = True, 
                            has_pull_requests = True, 
                            has_releases = True, 
                            has_wiki = True, 
                            html_url = '', 
                            id = 56, 
                            ignore_whitespace_conflicts = True, 
                            internal = True, 
                            language = '', 
                            languages_url = '', 
                            link = '', 
                            mirror = True, 
                            mirror_interval = '', 
                            mirror_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            name = '', 
                            object_format_name = 'sha1', 
                            open_issues_count = 56, 
                            open_pr_counter = 56, 
                            original_url = '', 
                            permissions = gitea_openapi.models.permission.Permission(
                                admin = True, 
                                pull = True, 
                                push = True, ), 
                            private = True, 
                            projects_mode = '', 
                            release_counter = 56, 
                            repo_transfer = gitea_openapi.models.repo_transfer.RepoTransfer(
                                doer = gitea_openapi.models.user.User(
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
                                recipient = , 
                                teams = [
                                    gitea_openapi.models.team.Team(
                                        can_create_org_repo = True, 
                                        description = '', 
                                        id = 56, 
                                        includes_all_repositories = True, 
                                        name = '', 
                                        organization = gitea_openapi.models.organization.Organization(
                                            avatar_url = '', 
                                            description = '', 
                                            email = '', 
                                            full_name = '', 
                                            id = 56, 
                                            location = '', 
                                            name = '', 
                                            repo_admin_change_team_access = True, 
                                            username = '', 
                                            visibility = '', 
                                            website = '', ), 
                                        permission = 'none', 
                                        units = [repo.code, repo.issues, repo.ext_issues, repo.wiki, repo.pulls, repo.releases, repo.projects, repo.ext_wiki], 
                                        units_map = {"repo.code":"read","repo.ext_issues":"none","repo.ext_wiki":"none","repo.issues":"write","repo.projects":"none","repo.pulls":"owner","repo.releases":"none","repo.wiki":"admin"}, )
                                    ], ), 
                            size = 56, 
                            ssh_url = '', 
                            stars_count = 56, 
                            template = True, 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            url = '', 
                            watchers_count = 56, 
                            website = '', ), 
                        permissions = gitea_openapi.models.permission.Permission(
                            admin = True, 
                            pull = True, 
                            push = True, ), 
                        private = True, 
                        projects_mode = '', 
                        release_counter = 56, 
                        repo_transfer = gitea_openapi.models.repo_transfer.RepoTransfer(), 
                        size = 56, 
                        ssh_url = '', 
                        stars_count = 56, 
                        template = True, 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        url = '', 
                        watchers_count = 56, 
                        website = '', ), 
                    repo_id = 56, 
                    sha = '', ),
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
                merge_base = '',
                merge_commit_sha = '',
                mergeable = True,
                merged = True,
                merged_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                merged_by = gitea_openapi.models.user.User(
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
                patch_url = '',
                pin_order = 56,
                requested_reviewers = [
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
            return PullRequest(
        )
        """

    def testPullRequest(self):
        """Test PullRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
