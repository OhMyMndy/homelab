# WebhookInstallationTargetRenamedChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | [**WebhookDiscussionCommentEditedChangesBody**](WebhookDiscussionCommentEditedChangesBody.md) |  | [optional] 
**slug** | [**WebhookDiscussionCommentEditedChangesBody**](WebhookDiscussionCommentEditedChangesBody.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_installation_target_renamed_changes import WebhookInstallationTargetRenamedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookInstallationTargetRenamedChanges from a JSON string
webhook_installation_target_renamed_changes_instance = WebhookInstallationTargetRenamedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookInstallationTargetRenamedChanges.to_json())

# convert the object into a dict
webhook_installation_target_renamed_changes_dict = webhook_installation_target_renamed_changes_instance.to_dict()
# create an instance of WebhookInstallationTargetRenamedChanges from a dict
webhook_installation_target_renamed_changes_from_dict = WebhookInstallationTargetRenamedChanges.from_dict(webhook_installation_target_renamed_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


