# WebhookLabelEditedChangesName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The previous version of the name if the action was &#x60;edited&#x60;. | 

## Example

```python
from github_openapi.models.webhook_label_edited_changes_name import WebhookLabelEditedChangesName

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookLabelEditedChangesName from a JSON string
webhook_label_edited_changes_name_instance = WebhookLabelEditedChangesName.from_json(json)
# print the JSON string representation of the object
print(WebhookLabelEditedChangesName.to_json())

# convert the object into a dict
webhook_label_edited_changes_name_dict = webhook_label_edited_changes_name_instance.to_dict()
# create an instance of WebhookLabelEditedChangesName from a dict
webhook_label_edited_changes_name_from_dict = WebhookLabelEditedChangesName.from_dict(webhook_label_edited_changes_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


