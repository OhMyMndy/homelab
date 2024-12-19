# WebhookTeamEditedChangesPrivacy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The previous version of the team&#39;s privacy if the action was &#x60;edited&#x60;. | 

## Example

```python
from github_openapi.models.webhook_team_edited_changes_privacy import WebhookTeamEditedChangesPrivacy

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookTeamEditedChangesPrivacy from a JSON string
webhook_team_edited_changes_privacy_instance = WebhookTeamEditedChangesPrivacy.from_json(json)
# print the JSON string representation of the object
print(WebhookTeamEditedChangesPrivacy.to_json())

# convert the object into a dict
webhook_team_edited_changes_privacy_dict = webhook_team_edited_changes_privacy_instance.to_dict()
# create an instance of WebhookTeamEditedChangesPrivacy from a dict
webhook_team_edited_changes_privacy_from_dict = WebhookTeamEditedChangesPrivacy.from_dict(webhook_team_edited_changes_privacy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


