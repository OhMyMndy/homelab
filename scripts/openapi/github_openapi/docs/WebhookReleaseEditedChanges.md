# WebhookReleaseEditedChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**WebhookProjectEditedChangesBody**](WebhookProjectEditedChangesBody.md) |  | [optional] 
**name** | [**WebhookLabelEditedChangesName**](WebhookLabelEditedChangesName.md) |  | [optional] 
**make_latest** | [**WebhookReleaseEditedChangesMakeLatest**](WebhookReleaseEditedChangesMakeLatest.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_release_edited_changes import WebhookReleaseEditedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookReleaseEditedChanges from a JSON string
webhook_release_edited_changes_instance = WebhookReleaseEditedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookReleaseEditedChanges.to_json())

# convert the object into a dict
webhook_release_edited_changes_dict = webhook_release_edited_changes_instance.to_dict()
# create an instance of WebhookReleaseEditedChanges from a dict
webhook_release_edited_changes_from_dict = WebhookReleaseEditedChanges.from_dict(webhook_release_edited_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


