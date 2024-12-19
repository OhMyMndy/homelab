# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_package_published_package_package_version import WebhookPackagePublishedPackagePackageVersion

class TestWebhookPackagePublishedPackagePackageVersion(unittest.TestCase):
    """WebhookPackagePublishedPackagePackageVersion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookPackagePublishedPackagePackageVersion:
        """Test WebhookPackagePublishedPackagePackageVersion
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookPackagePublishedPackagePackageVersion`
        """
        model = WebhookPackagePublishedPackagePackageVersion()
        if include_optional:
            return WebhookPackagePublishedPackagePackageVersion(
                author = github_openapi.models.user.User(
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
                body = None,
                body_html = '',
                container_metadata = github_openapi.models.webhook_package_published_package_package_version_container_metadata.webhook_package_published_package_package_version_container_metadata(
                    labels = github_openapi.models.labels.labels(), 
                    manifest = github_openapi.models.manifest.manifest(), 
                    tag = github_openapi.models.webhook_package_published_package_package_version_container_metadata_tag.webhook_package_published_package_package_version_container_metadata_tag(
                        digest = '', 
                        name = '', ), ),
                created_at = '',
                description = '',
                docker_metadata = [
                    github_openapi.models.webhook_package_published_package_package_version_docker_metadata_inner.webhook_package_published_package_package_version_docker_metadata_inner(
                        tags = [
                            ''
                            ], )
                    ],
                draft = True,
                html_url = '',
                id = 56,
                installation_command = '',
                manifest = '',
                metadata = [
                    { }
                    ],
                name = '',
                npm_metadata = github_openapi.models.webhook_package_published_package_package_version_npm_metadata.webhook_package_published_package_package_version_npm_metadata(
                    name = '', 
                    version = '', 
                    npm_user = '', 
                    author = github_openapi.models.author.author(), 
                    bugs = github_openapi.models.bugs.bugs(), 
                    dependencies = github_openapi.models.dependencies.dependencies(), 
                    dev_dependencies = github_openapi.models.dev_dependencies.dev_dependencies(), 
                    peer_dependencies = github_openapi.models.peer_dependencies.peer_dependencies(), 
                    optional_dependencies = github_openapi.models.optional_dependencies.optional_dependencies(), 
                    description = '', 
                    dist = github_openapi.models.dist.dist(), 
                    git_head = '', 
                    homepage = '', 
                    license = '', 
                    main = '', 
                    repository = github_openapi.models.repository.repository(), 
                    scripts = github_openapi.models.scripts.scripts(), 
                    id = '', 
                    node_version = '', 
                    npm_version = '', 
                    has_shrinkwrap = True, 
                    maintainers = [
                        None
                        ], 
                    contributors = [
                        None
                        ], 
                    engines = github_openapi.models.engines.engines(), 
                    keywords = [
                        ''
                        ], 
                    files = [
                        ''
                        ], 
                    bin = github_openapi.models.bin.bin(), 
                    man = github_openapi.models.man.man(), 
                    directories = github_openapi.models.directories.directories(), 
                    os = [
                        ''
                        ], 
                    cpu = [
                        ''
                        ], 
                    readme = '', 
                    installation_command = '', 
                    release_id = 56, 
                    commit_oid = '', 
                    published_via_actions = True, 
                    deleted_by_id = 56, ),
                nuget_metadata = [
                    github_openapi.models.webhook_package_published_package_package_version_nuget_metadata_inner.webhook_package_published_package_package_version_nuget_metadata_inner(
                        id = null, 
                        name = '', 
                        value = null, )
                    ],
                package_files = [
                    github_openapi.models.webhook_package_published_package_package_version_package_files_inner.webhook_package_published_package_package_version_package_files_inner(
                        content_type = '', 
                        created_at = '', 
                        download_url = '', 
                        id = 56, 
                        md5 = '', 
                        name = '', 
                        sha1 = '', 
                        sha256 = '', 
                        size = 56, 
                        state = '', 
                        updated_at = '', )
                    ],
                package_url = '',
                prerelease = True,
                release = github_openapi.models.webhook_package_published_package_package_version_release.webhook_package_published_package_package_version_release(
                    author = github_openapi.models.user.User(
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
                    created_at = '', 
                    draft = True, 
                    html_url = '', 
                    id = 56, 
                    name = '', 
                    prerelease = True, 
                    published_at = '', 
                    tag_name = '', 
                    target_commitish = '', 
                    url = '', ),
                rubygems_metadata = [
                    github_openapi.models.ruby_gems_metadata.Ruby Gems metadata(
                        name = '', 
                        description = '', 
                        readme = '', 
                        homepage = '', 
                        version_info = github_openapi.models.webhook_rubygems_metadata_version_info.webhook_rubygems_metadata_version_info(
                            version = '', ), 
                        platform = '', 
                        metadata = {
                            'key' : ''
                            }, 
                        repo = '', 
                        dependencies = [
                            {
                                'key' : ''
                                }
                            ], 
                        commit_oid = '', )
                    ],
                source_url = '',
                summary = '',
                tag_name = '',
                target_commitish = '',
                target_oid = '',
                updated_at = '',
                version = ''
            )
        else:
            return WebhookPackagePublishedPackagePackageVersion(
                description = '',
                html_url = '',
                id = 56,
                installation_command = '',
                metadata = [
                    { }
                    ],
                name = '',
                package_files = [
                    github_openapi.models.webhook_package_published_package_package_version_package_files_inner.webhook_package_published_package_package_version_package_files_inner(
                        content_type = '', 
                        created_at = '', 
                        download_url = '', 
                        id = 56, 
                        md5 = '', 
                        name = '', 
                        sha1 = '', 
                        sha256 = '', 
                        size = 56, 
                        state = '', 
                        updated_at = '', )
                    ],
                summary = '',
                version = '',
        )
        """

    def testWebhookPackagePublishedPackagePackageVersion(self):
        """Test WebhookPackagePublishedPackagePackageVersion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
