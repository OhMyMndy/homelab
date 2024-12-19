# WebhookProjectCardMovedChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_id** | [**WebhookProjectCardMovedChangesColumnId**](WebhookProjectCardMovedChangesColumnId.md) |  | 

## Example

```python
from github_openapi.models.webhook_project_card_moved_changes import WebhookProjectCardMovedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectCardMovedChanges from a JSON string
webhook_project_card_moved_changes_instance = WebhookProjectCardMovedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectCardMovedChanges.to_json())

# convert the object into a dict
webhook_project_card_moved_changes_dict = webhook_project_card_moved_changes_instance.to_dict()
# create an instance of WebhookProjectCardMovedChanges from a dict
webhook_project_card_moved_changes_from_dict = WebhookProjectCardMovedChanges.from_dict(webhook_project_card_moved_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


