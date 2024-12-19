# WebhookIssuesEditedChangesTitle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The previous version of the title. | 

## Example

```python
from github_openapi.models.webhook_issues_edited_changes_title import WebhookIssuesEditedChangesTitle

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssuesEditedChangesTitle from a JSON string
webhook_issues_edited_changes_title_instance = WebhookIssuesEditedChangesTitle.from_json(json)
# print the JSON string representation of the object
print(WebhookIssuesEditedChangesTitle.to_json())

# convert the object into a dict
webhook_issues_edited_changes_title_dict = webhook_issues_edited_changes_title_instance.to_dict()
# create an instance of WebhookIssuesEditedChangesTitle from a dict
webhook_issues_edited_changes_title_from_dict = WebhookIssuesEditedChangesTitle.from_dict(webhook_issues_edited_changes_title_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


