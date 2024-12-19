# WebhookTeamEditedChangesNotificationSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The previous version of the team&#39;s notification setting if the action was &#x60;edited&#x60;. | 

## Example

```python
from github_openapi.models.webhook_team_edited_changes_notification_setting import WebhookTeamEditedChangesNotificationSetting

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookTeamEditedChangesNotificationSetting from a JSON string
webhook_team_edited_changes_notification_setting_instance = WebhookTeamEditedChangesNotificationSetting.from_json(json)
# print the JSON string representation of the object
print(WebhookTeamEditedChangesNotificationSetting.to_json())

# convert the object into a dict
webhook_team_edited_changes_notification_setting_dict = webhook_team_edited_changes_notification_setting_instance.to_dict()
# create an instance of WebhookTeamEditedChangesNotificationSetting from a dict
webhook_team_edited_changes_notification_setting_from_dict = WebhookTeamEditedChangesNotificationSetting.from_dict(webhook_team_edited_changes_notification_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


