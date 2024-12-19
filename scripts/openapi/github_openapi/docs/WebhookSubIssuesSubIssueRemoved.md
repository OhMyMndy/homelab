# WebhookSubIssuesSubIssueRemoved


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**sub_issue_id** | **float** | The ID of the sub-issue. | 
**sub_issue** | [**Issue**](Issue.md) |  | 
**sub_issue_repo** | [**Repository**](Repository.md) |  | 
**parent_issue_id** | **float** | The ID of the parent issue. | 
**parent_issue** | [**Issue**](Issue.md) |  | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_sub_issues_sub_issue_removed import WebhookSubIssuesSubIssueRemoved

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubIssuesSubIssueRemoved from a JSON string
webhook_sub_issues_sub_issue_removed_instance = WebhookSubIssuesSubIssueRemoved.from_json(json)
# print the JSON string representation of the object
print(WebhookSubIssuesSubIssueRemoved.to_json())

# convert the object into a dict
webhook_sub_issues_sub_issue_removed_dict = webhook_sub_issues_sub_issue_removed_instance.to_dict()
# create an instance of WebhookSubIssuesSubIssueRemoved from a dict
webhook_sub_issues_sub_issue_removed_from_dict = WebhookSubIssuesSubIssueRemoved.from_dict(webhook_sub_issues_sub_issue_removed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


