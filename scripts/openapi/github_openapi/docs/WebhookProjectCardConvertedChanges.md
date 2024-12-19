# WebhookProjectCardConvertedChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | [**WebhookDiscussionCommentEditedChangesBody**](WebhookDiscussionCommentEditedChangesBody.md) |  | 

## Example

```python
from github_openapi.models.webhook_project_card_converted_changes import WebhookProjectCardConvertedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectCardConvertedChanges from a JSON string
webhook_project_card_converted_changes_instance = WebhookProjectCardConvertedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectCardConvertedChanges.to_json())

# convert the object into a dict
webhook_project_card_converted_changes_dict = webhook_project_card_converted_changes_instance.to_dict()
# create an instance of WebhookProjectCardConvertedChanges from a dict
webhook_project_card_converted_changes_from_dict = WebhookProjectCardConvertedChanges.from_dict(webhook_project_card_converted_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


