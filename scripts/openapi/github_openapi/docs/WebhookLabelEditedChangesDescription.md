# WebhookLabelEditedChangesDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The previous version of the description if the action was &#x60;edited&#x60;. | 

## Example

```python
from github_openapi.models.webhook_label_edited_changes_description import WebhookLabelEditedChangesDescription

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookLabelEditedChangesDescription from a JSON string
webhook_label_edited_changes_description_instance = WebhookLabelEditedChangesDescription.from_json(json)
# print the JSON string representation of the object
print(WebhookLabelEditedChangesDescription.to_json())

# convert the object into a dict
webhook_label_edited_changes_description_dict = webhook_label_edited_changes_description_instance.to_dict()
# create an instance of WebhookLabelEditedChangesDescription from a dict
webhook_label_edited_changes_description_from_dict = WebhookLabelEditedChangesDescription.from_dict(webhook_label_edited_changes_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


