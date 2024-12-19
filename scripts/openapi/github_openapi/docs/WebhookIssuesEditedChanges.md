# WebhookIssuesEditedChanges

The changes to the issue.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**WebhooksChangesBody**](WebhooksChangesBody.md) |  | [optional] 
**title** | [**WebhookIssuesEditedChangesTitle**](WebhookIssuesEditedChangesTitle.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_issues_edited_changes import WebhookIssuesEditedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssuesEditedChanges from a JSON string
webhook_issues_edited_changes_instance = WebhookIssuesEditedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookIssuesEditedChanges.to_json())

# convert the object into a dict
webhook_issues_edited_changes_dict = webhook_issues_edited_changes_instance.to_dict()
# create an instance of WebhookIssuesEditedChanges from a dict
webhook_issues_edited_changes_from_dict = WebhookIssuesEditedChanges.from_dict(webhook_issues_edited_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


