# RepositoryWebhooksTemplateRepositoryOwner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**node_id** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**gravatar_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**followers_url** | **str** |  | [optional] 
**following_url** | **str** |  | [optional] 
**gists_url** | **str** |  | [optional] 
**starred_url** | **str** |  | [optional] 
**subscriptions_url** | **str** |  | [optional] 
**organizations_url** | **str** |  | [optional] 
**repos_url** | **str** |  | [optional] 
**events_url** | **str** |  | [optional] 
**received_events_url** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**site_admin** | **bool** |  | [optional] 

## Example

```python
from github_openapi.models.repository_webhooks_template_repository_owner import RepositoryWebhooksTemplateRepositoryOwner

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryWebhooksTemplateRepositoryOwner from a JSON string
repository_webhooks_template_repository_owner_instance = RepositoryWebhooksTemplateRepositoryOwner.from_json(json)
# print the JSON string representation of the object
print(RepositoryWebhooksTemplateRepositoryOwner.to_json())

# convert the object into a dict
repository_webhooks_template_repository_owner_dict = repository_webhooks_template_repository_owner_instance.to_dict()
# create an instance of RepositoryWebhooksTemplateRepositoryOwner from a dict
repository_webhooks_template_repository_owner_from_dict = RepositoryWebhooksTemplateRepositoryOwner.from_dict(repository_webhooks_template_repository_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


