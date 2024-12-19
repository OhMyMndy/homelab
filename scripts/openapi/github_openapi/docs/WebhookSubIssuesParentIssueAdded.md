# WebhookSubIssuesParentIssueAdded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**parent_issue_id** | **float** | The ID of the parent issue. | 
**parent_issue** | [**Issue**](Issue.md) |  | 
**parent_issue_repo** | [**Repository**](Repository.md) |  | 
**sub_issue_id** | **float** | The ID of the sub-issue. | 
**sub_issue** | [**Issue**](Issue.md) |  | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_sub_issues_parent_issue_added import WebhookSubIssuesParentIssueAdded

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubIssuesParentIssueAdded from a JSON string
webhook_sub_issues_parent_issue_added_instance = WebhookSubIssuesParentIssueAdded.from_json(json)
# print the JSON string representation of the object
print(WebhookSubIssuesParentIssueAdded.to_json())

# convert the object into a dict
webhook_sub_issues_parent_issue_added_dict = webhook_sub_issues_parent_issue_added_instance.to_dict()
# create an instance of WebhookSubIssuesParentIssueAdded from a dict
webhook_sub_issues_parent_issue_added_from_dict = WebhookSubIssuesParentIssueAdded.from_dict(webhook_sub_issues_parent_issue_added_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


