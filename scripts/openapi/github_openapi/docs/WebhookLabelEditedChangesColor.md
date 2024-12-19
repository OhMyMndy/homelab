# WebhookLabelEditedChangesColor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The previous version of the color if the action was &#x60;edited&#x60;. | 

## Example

```python
from github_openapi.models.webhook_label_edited_changes_color import WebhookLabelEditedChangesColor

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookLabelEditedChangesColor from a JSON string
webhook_label_edited_changes_color_instance = WebhookLabelEditedChangesColor.from_json(json)
# print the JSON string representation of the object
print(WebhookLabelEditedChangesColor.to_json())

# convert the object into a dict
webhook_label_edited_changes_color_dict = webhook_label_edited_changes_color_instance.to_dict()
# create an instance of WebhookLabelEditedChangesColor from a dict
webhook_label_edited_changes_color_from_dict = WebhookLabelEditedChangesColor.from_dict(webhook_label_edited_changes_color_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


