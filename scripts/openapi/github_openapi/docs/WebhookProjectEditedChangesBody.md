# WebhookProjectEditedChangesBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The previous version of the body if the action was &#x60;edited&#x60;. | 

## Example

```python
from github_openapi.models.webhook_project_edited_changes_body import WebhookProjectEditedChangesBody

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectEditedChangesBody from a JSON string
webhook_project_edited_changes_body_instance = WebhookProjectEditedChangesBody.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectEditedChangesBody.to_json())

# convert the object into a dict
webhook_project_edited_changes_body_dict = webhook_project_edited_changes_body_instance.to_dict()
# create an instance of WebhookProjectEditedChangesBody from a dict
webhook_project_edited_changes_body_from_dict = WebhookProjectEditedChangesBody.from_dict(webhook_project_edited_changes_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


