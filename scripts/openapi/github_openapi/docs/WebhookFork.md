# WebhookFork

A user forks a repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**forkee** | [**WebhookForkForkee**](WebhookForkForkee.md) |  | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_fork import WebhookFork

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookFork from a JSON string
webhook_fork_instance = WebhookFork.from_json(json)
# print the JSON string representation of the object
print(WebhookFork.to_json())

# convert the object into a dict
webhook_fork_dict = webhook_fork_instance.to_dict()
# create an instance of WebhookFork from a dict
webhook_fork_from_dict = WebhookFork.from_dict(webhook_fork_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


