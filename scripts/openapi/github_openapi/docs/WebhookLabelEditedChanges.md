# WebhookLabelEditedChanges

The changes to the label if the action was `edited`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | [**WebhookLabelEditedChangesColor**](WebhookLabelEditedChangesColor.md) |  | [optional] 
**description** | [**WebhookLabelEditedChangesDescription**](WebhookLabelEditedChangesDescription.md) |  | [optional] 
**name** | [**WebhookLabelEditedChangesName**](WebhookLabelEditedChangesName.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_label_edited_changes import WebhookLabelEditedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookLabelEditedChanges from a JSON string
webhook_label_edited_changes_instance = WebhookLabelEditedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookLabelEditedChanges.to_json())

# convert the object into a dict
webhook_label_edited_changes_dict = webhook_label_edited_changes_instance.to_dict()
# create an instance of WebhookLabelEditedChanges from a dict
webhook_label_edited_changes_from_dict = WebhookLabelEditedChanges.from_dict(webhook_label_edited_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


