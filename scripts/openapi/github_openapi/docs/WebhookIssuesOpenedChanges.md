# WebhookIssuesOpenedChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_issue** | [**Issue6**](Issue6.md) |  | 
**old_repository** | [**Repository1**](Repository1.md) |  | 

## Example

```python
from github_openapi.models.webhook_issues_opened_changes import WebhookIssuesOpenedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssuesOpenedChanges from a JSON string
webhook_issues_opened_changes_instance = WebhookIssuesOpenedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookIssuesOpenedChanges.to_json())

# convert the object into a dict
webhook_issues_opened_changes_dict = webhook_issues_opened_changes_instance.to_dict()
# create an instance of WebhookIssuesOpenedChanges from a dict
webhook_issues_opened_changes_from_dict = WebhookIssuesOpenedChanges.from_dict(webhook_issues_opened_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


