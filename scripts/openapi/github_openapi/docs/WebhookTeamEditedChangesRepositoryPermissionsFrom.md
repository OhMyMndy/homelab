# WebhookTeamEditedChangesRepositoryPermissionsFrom


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin** | **bool** | The previous version of the team member&#39;s &#x60;admin&#x60; permission on a repository, if the action was &#x60;edited&#x60;. | [optional] 
**pull** | **bool** | The previous version of the team member&#39;s &#x60;pull&#x60; permission on a repository, if the action was &#x60;edited&#x60;. | [optional] 
**push** | **bool** | The previous version of the team member&#39;s &#x60;push&#x60; permission on a repository, if the action was &#x60;edited&#x60;. | [optional] 

## Example

```python
from github_openapi.models.webhook_team_edited_changes_repository_permissions_from import WebhookTeamEditedChangesRepositoryPermissionsFrom

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookTeamEditedChangesRepositoryPermissionsFrom from a JSON string
webhook_team_edited_changes_repository_permissions_from_instance = WebhookTeamEditedChangesRepositoryPermissionsFrom.from_json(json)
# print the JSON string representation of the object
print(WebhookTeamEditedChangesRepositoryPermissionsFrom.to_json())

# convert the object into a dict
webhook_team_edited_changes_repository_permissions_from_dict = webhook_team_edited_changes_repository_permissions_from_instance.to_dict()
# create an instance of WebhookTeamEditedChangesRepositoryPermissionsFrom from a dict
webhook_team_edited_changes_repository_permissions_from_from_dict = WebhookTeamEditedChangesRepositoryPermissionsFrom.from_dict(webhook_team_edited_changes_repository_permissions_from_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


