# WebhookSponsorshipEditedChangesPrivacyLevel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The &#x60;edited&#x60; event types include the details about the change when someone edits a sponsorship to change the privacy. | 

## Example

```python
from github_openapi.models.webhook_sponsorship_edited_changes_privacy_level import WebhookSponsorshipEditedChangesPrivacyLevel

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSponsorshipEditedChangesPrivacyLevel from a JSON string
webhook_sponsorship_edited_changes_privacy_level_instance = WebhookSponsorshipEditedChangesPrivacyLevel.from_json(json)
# print the JSON string representation of the object
print(WebhookSponsorshipEditedChangesPrivacyLevel.to_json())

# convert the object into a dict
webhook_sponsorship_edited_changes_privacy_level_dict = webhook_sponsorship_edited_changes_privacy_level_instance.to_dict()
# create an instance of WebhookSponsorshipEditedChangesPrivacyLevel from a dict
webhook_sponsorship_edited_changes_privacy_level_from_dict = WebhookSponsorshipEditedChangesPrivacyLevel.from_dict(webhook_sponsorship_edited_changes_privacy_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


