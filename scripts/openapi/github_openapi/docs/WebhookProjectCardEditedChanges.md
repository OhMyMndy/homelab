# WebhookProjectCardEditedChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | [**WebhookProjectCardEditedChangesNote**](WebhookProjectCardEditedChangesNote.md) |  | 

## Example

```python
from github_openapi.models.webhook_project_card_edited_changes import WebhookProjectCardEditedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectCardEditedChanges from a JSON string
webhook_project_card_edited_changes_instance = WebhookProjectCardEditedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectCardEditedChanges.to_json())

# convert the object into a dict
webhook_project_card_edited_changes_dict = webhook_project_card_edited_changes_instance.to_dict()
# create an instance of WebhookProjectCardEditedChanges from a dict
webhook_project_card_edited_changes_from_dict = WebhookProjectCardEditedChanges.from_dict(webhook_project_card_edited_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


