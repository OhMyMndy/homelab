# WebhookIssueCommentCreatedIssueAllOfUser


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

## Example

```python
from github_openapi.models.webhook_issue_comment_created_issue_all_of_user import WebhookIssueCommentCreatedIssueAllOfUser

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssueCommentCreatedIssueAllOfUser from a JSON string
webhook_issue_comment_created_issue_all_of_user_instance = WebhookIssueCommentCreatedIssueAllOfUser.from_json(json)
# print the JSON string representation of the object
print(WebhookIssueCommentCreatedIssueAllOfUser.to_json())

# convert the object into a dict
webhook_issue_comment_created_issue_all_of_user_dict = webhook_issue_comment_created_issue_all_of_user_instance.to_dict()
# create an instance of WebhookIssueCommentCreatedIssueAllOfUser from a dict
webhook_issue_comment_created_issue_all_of_user_from_dict = WebhookIssueCommentCreatedIssueAllOfUser.from_dict(webhook_issue_comment_created_issue_all_of_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


