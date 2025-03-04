# coding: utf-8

# flake8: noqa
"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from gitea_openapi.models.api_error import APIError
from gitea_openapi.models.access_token import AccessToken
from gitea_openapi.models.action_variable import ActionVariable
from gitea_openapi.models.activity import Activity
from gitea_openapi.models.activity_pub import ActivityPub
from gitea_openapi.models.add_collaborator_option import AddCollaboratorOption
from gitea_openapi.models.add_time_option import AddTimeOption
from gitea_openapi.models.annotated_tag import AnnotatedTag
from gitea_openapi.models.annotated_tag_object import AnnotatedTagObject
from gitea_openapi.models.attachment import Attachment
from gitea_openapi.models.badge import Badge
from gitea_openapi.models.branch import Branch
from gitea_openapi.models.branch_protection import BranchProtection
from gitea_openapi.models.change_file_operation import ChangeFileOperation
from gitea_openapi.models.change_files_options import ChangeFilesOptions
from gitea_openapi.models.changed_file import ChangedFile
from gitea_openapi.models.combined_status import CombinedStatus
from gitea_openapi.models.comment import Comment
from gitea_openapi.models.commit import Commit
from gitea_openapi.models.commit_affected_files import CommitAffectedFiles
from gitea_openapi.models.commit_date_options import CommitDateOptions
from gitea_openapi.models.commit_meta import CommitMeta
from gitea_openapi.models.commit_stats import CommitStats
from gitea_openapi.models.commit_status import CommitStatus
from gitea_openapi.models.commit_user import CommitUser
from gitea_openapi.models.compare import Compare
from gitea_openapi.models.contents_response import ContentsResponse
from gitea_openapi.models.create_access_token_option import CreateAccessTokenOption
from gitea_openapi.models.create_branch_protection_option import CreateBranchProtectionOption
from gitea_openapi.models.create_branch_repo_option import CreateBranchRepoOption
from gitea_openapi.models.create_email_option import CreateEmailOption
from gitea_openapi.models.create_file_options import CreateFileOptions
from gitea_openapi.models.create_fork_option import CreateForkOption
from gitea_openapi.models.create_gpg_key_option import CreateGPGKeyOption
from gitea_openapi.models.create_hook_option import CreateHookOption
from gitea_openapi.models.create_issue_comment_option import CreateIssueCommentOption
from gitea_openapi.models.create_issue_option import CreateIssueOption
from gitea_openapi.models.create_key_option import CreateKeyOption
from gitea_openapi.models.create_label_option import CreateLabelOption
from gitea_openapi.models.create_milestone_option import CreateMilestoneOption
from gitea_openapi.models.create_o_auth2_application_options import CreateOAuth2ApplicationOptions
from gitea_openapi.models.create_or_update_secret_option import CreateOrUpdateSecretOption
from gitea_openapi.models.create_org_option import CreateOrgOption
from gitea_openapi.models.create_pull_request_option import CreatePullRequestOption
from gitea_openapi.models.create_pull_review_comment import CreatePullReviewComment
from gitea_openapi.models.create_pull_review_options import CreatePullReviewOptions
from gitea_openapi.models.create_push_mirror_option import CreatePushMirrorOption
from gitea_openapi.models.create_release_option import CreateReleaseOption
from gitea_openapi.models.create_repo_option import CreateRepoOption
from gitea_openapi.models.create_status_option import CreateStatusOption
from gitea_openapi.models.create_tag_option import CreateTagOption
from gitea_openapi.models.create_team_option import CreateTeamOption
from gitea_openapi.models.create_user_option import CreateUserOption
from gitea_openapi.models.create_variable_option import CreateVariableOption
from gitea_openapi.models.create_wiki_page_options import CreateWikiPageOptions
from gitea_openapi.models.cron import Cron
from gitea_openapi.models.delete_email_option import DeleteEmailOption
from gitea_openapi.models.delete_file_options import DeleteFileOptions
from gitea_openapi.models.deploy_key import DeployKey
from gitea_openapi.models.dismiss_pull_review_options import DismissPullReviewOptions
from gitea_openapi.models.edit_attachment_options import EditAttachmentOptions
from gitea_openapi.models.edit_branch_protection_option import EditBranchProtectionOption
from gitea_openapi.models.edit_deadline_option import EditDeadlineOption
from gitea_openapi.models.edit_git_hook_option import EditGitHookOption
from gitea_openapi.models.edit_hook_option import EditHookOption
from gitea_openapi.models.edit_issue_comment_option import EditIssueCommentOption
from gitea_openapi.models.edit_issue_option import EditIssueOption
from gitea_openapi.models.edit_label_option import EditLabelOption
from gitea_openapi.models.edit_milestone_option import EditMilestoneOption
from gitea_openapi.models.edit_org_option import EditOrgOption
from gitea_openapi.models.edit_pull_request_option import EditPullRequestOption
from gitea_openapi.models.edit_reaction_option import EditReactionOption
from gitea_openapi.models.edit_release_option import EditReleaseOption
from gitea_openapi.models.edit_repo_option import EditRepoOption
from gitea_openapi.models.edit_team_option import EditTeamOption
from gitea_openapi.models.edit_user_option import EditUserOption
from gitea_openapi.models.email import Email
from gitea_openapi.models.external_tracker import ExternalTracker
from gitea_openapi.models.external_wiki import ExternalWiki
from gitea_openapi.models.file_commit_response import FileCommitResponse
from gitea_openapi.models.file_delete_response import FileDeleteResponse
from gitea_openapi.models.file_links_response import FileLinksResponse
from gitea_openapi.models.file_response import FileResponse
from gitea_openapi.models.files_response import FilesResponse
from gitea_openapi.models.gpg_key import GPGKey
from gitea_openapi.models.gpg_key_email import GPGKeyEmail
from gitea_openapi.models.general_api_settings import GeneralAPISettings
from gitea_openapi.models.general_attachment_settings import GeneralAttachmentSettings
from gitea_openapi.models.general_repo_settings import GeneralRepoSettings
from gitea_openapi.models.general_ui_settings import GeneralUISettings
from gitea_openapi.models.generate_repo_option import GenerateRepoOption
from gitea_openapi.models.git_blob_response import GitBlobResponse
from gitea_openapi.models.git_entry import GitEntry
from gitea_openapi.models.git_hook import GitHook
from gitea_openapi.models.git_object import GitObject
from gitea_openapi.models.git_tree_response import GitTreeResponse
from gitea_openapi.models.gitignore_template_info import GitignoreTemplateInfo
from gitea_openapi.models.hook import Hook
from gitea_openapi.models.identity import Identity
from gitea_openapi.models.internal_tracker import InternalTracker
from gitea_openapi.models.issue import Issue
from gitea_openapi.models.issue_config import IssueConfig
from gitea_openapi.models.issue_config_contact_link import IssueConfigContactLink
from gitea_openapi.models.issue_config_validation import IssueConfigValidation
from gitea_openapi.models.issue_deadline import IssueDeadline
from gitea_openapi.models.issue_form_field import IssueFormField
from gitea_openapi.models.issue_labels_option import IssueLabelsOption
from gitea_openapi.models.issue_meta import IssueMeta
from gitea_openapi.models.issue_template import IssueTemplate
from gitea_openapi.models.label import Label
from gitea_openapi.models.label_template import LabelTemplate
from gitea_openapi.models.license_template_info import LicenseTemplateInfo
from gitea_openapi.models.licenses_template_list_entry import LicensesTemplateListEntry
from gitea_openapi.models.markdown_option import MarkdownOption
from gitea_openapi.models.markup_option import MarkupOption
from gitea_openapi.models.merge_pull_request_option import MergePullRequestOption
from gitea_openapi.models.migrate_repo_options import MigrateRepoOptions
from gitea_openapi.models.milestone import Milestone
from gitea_openapi.models.new_issue_pins_allowed import NewIssuePinsAllowed
from gitea_openapi.models.node_info import NodeInfo
from gitea_openapi.models.node_info_services import NodeInfoServices
from gitea_openapi.models.node_info_software import NodeInfoSoftware
from gitea_openapi.models.node_info_usage import NodeInfoUsage
from gitea_openapi.models.node_info_usage_users import NodeInfoUsageUsers
from gitea_openapi.models.note import Note
from gitea_openapi.models.notification_count import NotificationCount
from gitea_openapi.models.notification_subject import NotificationSubject
from gitea_openapi.models.notification_thread import NotificationThread
from gitea_openapi.models.o_auth2_application import OAuth2Application
from gitea_openapi.models.organization import Organization
from gitea_openapi.models.organization_permissions import OrganizationPermissions
from gitea_openapi.models.pr_branch_info import PRBranchInfo
from gitea_openapi.models.package import Package
from gitea_openapi.models.package_file import PackageFile
from gitea_openapi.models.payload_commit import PayloadCommit
from gitea_openapi.models.payload_commit_verification import PayloadCommitVerification
from gitea_openapi.models.payload_user import PayloadUser
from gitea_openapi.models.permission import Permission
from gitea_openapi.models.public_key import PublicKey
from gitea_openapi.models.pull_request import PullRequest
from gitea_openapi.models.pull_request_meta import PullRequestMeta
from gitea_openapi.models.pull_review import PullReview
from gitea_openapi.models.pull_review_comment import PullReviewComment
from gitea_openapi.models.pull_review_request_options import PullReviewRequestOptions
from gitea_openapi.models.push_mirror import PushMirror
from gitea_openapi.models.reaction import Reaction
from gitea_openapi.models.reference import Reference
from gitea_openapi.models.release import Release
from gitea_openapi.models.rename_user_option import RenameUserOption
from gitea_openapi.models.repo_collaborator_permission import RepoCollaboratorPermission
from gitea_openapi.models.repo_commit import RepoCommit
from gitea_openapi.models.repo_create_release_attachment_request import RepoCreateReleaseAttachmentRequest
from gitea_openapi.models.repo_topic_options import RepoTopicOptions
from gitea_openapi.models.repo_transfer import RepoTransfer
from gitea_openapi.models.repository import Repository
from gitea_openapi.models.repository_meta import RepositoryMeta
from gitea_openapi.models.search_results import SearchResults
from gitea_openapi.models.secret import Secret
from gitea_openapi.models.server_version import ServerVersion
from gitea_openapi.models.stop_watch import StopWatch
from gitea_openapi.models.submit_pull_review_options import SubmitPullReviewOptions
from gitea_openapi.models.tag import Tag
from gitea_openapi.models.team import Team
from gitea_openapi.models.team_search200_response import TeamSearch200Response
from gitea_openapi.models.timeline_comment import TimelineComment
from gitea_openapi.models.topic_name import TopicName
from gitea_openapi.models.topic_response import TopicResponse
from gitea_openapi.models.tracked_time import TrackedTime
from gitea_openapi.models.transfer_repo_option import TransferRepoOption
from gitea_openapi.models.update_file_options import UpdateFileOptions
from gitea_openapi.models.update_repo_avatar_option import UpdateRepoAvatarOption
from gitea_openapi.models.update_user_avatar_option import UpdateUserAvatarOption
from gitea_openapi.models.update_variable_option import UpdateVariableOption
from gitea_openapi.models.user import User
from gitea_openapi.models.user_badge_option import UserBadgeOption
from gitea_openapi.models.user_heatmap_data import UserHeatmapData
from gitea_openapi.models.user_search200_response import UserSearch200Response
from gitea_openapi.models.user_settings import UserSettings
from gitea_openapi.models.user_settings_options import UserSettingsOptions
from gitea_openapi.models.watch_info import WatchInfo
from gitea_openapi.models.wiki_commit import WikiCommit
from gitea_openapi.models.wiki_commit_list import WikiCommitList
from gitea_openapi.models.wiki_page import WikiPage
from gitea_openapi.models.wiki_page_meta_data import WikiPageMetaData
