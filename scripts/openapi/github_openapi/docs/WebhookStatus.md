# WebhookStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_url** | **str** |  | [optional] 
**branches** | [**List[WebhookStatusBranchesInner]**](WebhookStatusBranchesInner.md) | An array of branch objects containing the status&#39; SHA. Each branch contains the given SHA, but the SHA may or may not be the head of the branch. The array includes a maximum of 10 branches. | 
**commit** | [**WebhookStatusCommit**](WebhookStatusCommit.md) |  | 
**context** | **str** |  | 
**created_at** | **str** |  | 
**description** | **str** | The optional human-readable description added to the status. | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**id** | **int** | The unique identifier of the status. | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**name** | **str** |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**sha** | **str** | The Commit SHA. | 
**state** | **str** | The new state. Can be &#x60;pending&#x60;, &#x60;success&#x60;, &#x60;failure&#x60;, or &#x60;error&#x60;. | 
**target_url** | **str** | The optional link added to the status. | 
**updated_at** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_status import WebhookStatus

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookStatus from a JSON string
webhook_status_instance = WebhookStatus.from_json(json)
# print the JSON string representation of the object
print(WebhookStatus.to_json())

# convert the object into a dict
webhook_status_dict = webhook_status_instance.to_dict()
# create an instance of WebhookStatus from a dict
webhook_status_from_dict = WebhookStatus.from_dict(webhook_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


