# WebhookTeamEditedChanges

The changes to the team if the action was `edited`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**WebhookLabelEditedChangesDescription**](WebhookLabelEditedChangesDescription.md) |  | [optional] 
**name** | [**WebhookLabelEditedChangesName**](WebhookLabelEditedChangesName.md) |  | [optional] 
**privacy** | [**WebhookTeamEditedChangesPrivacy**](WebhookTeamEditedChangesPrivacy.md) |  | [optional] 
**notification_setting** | [**WebhookTeamEditedChangesNotificationSetting**](WebhookTeamEditedChangesNotificationSetting.md) |  | [optional] 
**repository** | [**WebhookTeamEditedChangesRepository**](WebhookTeamEditedChangesRepository.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_team_edited_changes import WebhookTeamEditedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookTeamEditedChanges from a JSON string
webhook_team_edited_changes_instance = WebhookTeamEditedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookTeamEditedChanges.to_json())

# convert the object into a dict
webhook_team_edited_changes_dict = webhook_team_edited_changes_instance.to_dict()
# create an instance of WebhookTeamEditedChanges from a dict
webhook_team_edited_changes_from_dict = WebhookTeamEditedChanges.from_dict(webhook_team_edited_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


