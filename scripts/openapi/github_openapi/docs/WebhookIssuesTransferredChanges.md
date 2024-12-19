# WebhookIssuesTransferredChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_issue** | [**Issue9**](Issue9.md) |  | 
**new_repository** | [**Repository2**](Repository2.md) |  | 

## Example

```python
from github_openapi.models.webhook_issues_transferred_changes import WebhookIssuesTransferredChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssuesTransferredChanges from a JSON string
webhook_issues_transferred_changes_instance = WebhookIssuesTransferredChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookIssuesTransferredChanges.to_json())

# convert the object into a dict
webhook_issues_transferred_changes_dict = webhook_issues_transferred_changes_instance.to_dict()
# create an instance of WebhookIssuesTransferredChanges from a dict
webhook_issues_transferred_changes_from_dict = WebhookIssuesTransferredChanges.from_dict(webhook_issues_transferred_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


