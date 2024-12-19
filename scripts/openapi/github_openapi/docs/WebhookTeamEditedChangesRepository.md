# WebhookTeamEditedChangesRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**WebhookTeamEditedChangesRepositoryPermissions**](WebhookTeamEditedChangesRepositoryPermissions.md) |  | 

## Example

```python
from github_openapi.models.webhook_team_edited_changes_repository import WebhookTeamEditedChangesRepository

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookTeamEditedChangesRepository from a JSON string
webhook_team_edited_changes_repository_instance = WebhookTeamEditedChangesRepository.from_json(json)
# print the JSON string representation of the object
print(WebhookTeamEditedChangesRepository.to_json())

# convert the object into a dict
webhook_team_edited_changes_repository_dict = webhook_team_edited_changes_repository_instance.to_dict()
# create an instance of WebhookTeamEditedChangesRepository from a dict
webhook_team_edited_changes_repository_from_dict = WebhookTeamEditedChangesRepository.from_dict(webhook_team_edited_changes_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


