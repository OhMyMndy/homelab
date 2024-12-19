# WebhookInstallationTargetRenamedAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived_at** | **str** |  | [optional] 
**avatar_url** | **str** |  | 
**created_at** | **str** |  | [optional] 
**description** | **object** |  | [optional] 
**events_url** | **str** |  | [optional] 
**followers** | **int** |  | [optional] 
**followers_url** | **str** |  | [optional] 
**following** | **int** |  | [optional] 
**following_url** | **str** |  | [optional] 
**gists_url** | **str** |  | [optional] 
**gravatar_id** | **str** |  | [optional] 
**has_organization_projects** | **bool** |  | [optional] 
**has_repository_projects** | **bool** |  | [optional] 
**hooks_url** | **str** |  | [optional] 
**html_url** | **str** |  | 
**id** | **int** |  | 
**is_verified** | **bool** |  | [optional] 
**issues_url** | **str** |  | [optional] 
**login** | **str** |  | [optional] 
**members_url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**node_id** | **str** |  | 
**organizations_url** | **str** |  | [optional] 
**public_gists** | **int** |  | [optional] 
**public_members_url** | **str** |  | [optional] 
**public_repos** | **int** |  | [optional] 
**received_events_url** | **str** |  | [optional] 
**repos_url** | **str** |  | [optional] 
**site_admin** | **bool** |  | [optional] 
**slug** | **str** |  | [optional] 
**starred_url** | **str** |  | [optional] 
**subscriptions_url** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**website_url** | **object** |  | [optional] 
**user_view_type** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.webhook_installation_target_renamed_account import WebhookInstallationTargetRenamedAccount

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookInstallationTargetRenamedAccount from a JSON string
webhook_installation_target_renamed_account_instance = WebhookInstallationTargetRenamedAccount.from_json(json)
# print the JSON string representation of the object
print(WebhookInstallationTargetRenamedAccount.to_json())

# convert the object into a dict
webhook_installation_target_renamed_account_dict = webhook_installation_target_renamed_account_instance.to_dict()
# create an instance of WebhookInstallationTargetRenamedAccount from a dict
webhook_installation_target_renamed_account_from_dict = WebhookInstallationTargetRenamedAccount.from_dict(webhook_installation_target_renamed_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


