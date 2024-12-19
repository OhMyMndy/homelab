# WebhookIssueCommentDeletedIssueAllOfUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_url** | **str** |  | [optional] 
**events_url** | **str** |  | [optional] 
**followers_url** | **str** |  | [optional] 
**following_url** | **str** |  | [optional] 
**gists_url** | **str** |  | [optional] 
**gravatar_id** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**login** | **str** |  | [optional] 
**node_id** | **str** |  | [optional] 
**organizations_url** | **str** |  | [optional] 
**received_events_url** | **str** |  | [optional] 
**repos_url** | **str** |  | [optional] 
**site_admin** | **bool** |  | [optional] 
**starred_url** | **str** |  | [optional] 
**subscriptions_url** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**user_view_type** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.webhook_issue_comment_deleted_issue_all_of_user import WebhookIssueCommentDeletedIssueAllOfUser

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssueCommentDeletedIssueAllOfUser from a JSON string
webhook_issue_comment_deleted_issue_all_of_user_instance = WebhookIssueCommentDeletedIssueAllOfUser.from_json(json)
# print the JSON string representation of the object
print(WebhookIssueCommentDeletedIssueAllOfUser.to_json())

# convert the object into a dict
webhook_issue_comment_deleted_issue_all_of_user_dict = webhook_issue_comment_deleted_issue_all_of_user_instance.to_dict()
# create an instance of WebhookIssueCommentDeletedIssueAllOfUser from a dict
webhook_issue_comment_deleted_issue_all_of_user_from_dict = WebhookIssueCommentDeletedIssueAllOfUser.from_dict(webhook_issue_comment_deleted_issue_all_of_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


