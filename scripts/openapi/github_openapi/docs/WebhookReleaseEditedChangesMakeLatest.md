# WebhookReleaseEditedChangesMakeLatest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **bool** | Whether this release was explicitly &#x60;edited&#x60; to be the latest. | 

## Example

```python
from github_openapi.models.webhook_release_edited_changes_make_latest import WebhookReleaseEditedChangesMakeLatest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookReleaseEditedChangesMakeLatest from a JSON string
webhook_release_edited_changes_make_latest_instance = WebhookReleaseEditedChangesMakeLatest.from_json(json)
# print the JSON string representation of the object
print(WebhookReleaseEditedChangesMakeLatest.to_json())

# convert the object into a dict
webhook_release_edited_changes_make_latest_dict = webhook_release_edited_changes_make_latest_instance.to_dict()
# create an instance of WebhookReleaseEditedChangesMakeLatest from a dict
webhook_release_edited_changes_make_latest_from_dict = WebhookReleaseEditedChangesMakeLatest.from_dict(webhook_release_edited_changes_make_latest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


