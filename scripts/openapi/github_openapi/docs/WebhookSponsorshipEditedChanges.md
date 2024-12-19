# WebhookSponsorshipEditedChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privacy_level** | [**WebhookSponsorshipEditedChangesPrivacyLevel**](WebhookSponsorshipEditedChangesPrivacyLevel.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_sponsorship_edited_changes import WebhookSponsorshipEditedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSponsorshipEditedChanges from a JSON string
webhook_sponsorship_edited_changes_instance = WebhookSponsorshipEditedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookSponsorshipEditedChanges.to_json())

# convert the object into a dict
webhook_sponsorship_edited_changes_dict = webhook_sponsorship_edited_changes_instance.to_dict()
# create an instance of WebhookSponsorshipEditedChanges from a dict
webhook_sponsorship_edited_changes_from_dict = WebhookSponsorshipEditedChanges.from_dict(webhook_sponsorship_edited_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


