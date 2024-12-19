# WebhookProjectEditedChangesName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The changes to the project if the action was &#x60;edited&#x60;. | 

## Example

```python
from github_openapi.models.webhook_project_edited_changes_name import WebhookProjectEditedChangesName

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectEditedChangesName from a JSON string
webhook_project_edited_changes_name_instance = WebhookProjectEditedChangesName.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectEditedChangesName.to_json())

# convert the object into a dict
webhook_project_edited_changes_name_dict = webhook_project_edited_changes_name_instance.to_dict()
# create an instance of WebhookProjectEditedChangesName from a dict
webhook_project_edited_changes_name_from_dict = WebhookProjectEditedChangesName.from_dict(webhook_project_edited_changes_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


