# WebhookRepositoryDispatchSample


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The &#x60;event_type&#x60; that was specified in the &#x60;POST /repos/{owner}/{repo}/dispatches&#x60; request body. | 
**branch** | **str** |  | 
**client_payload** | **Dict[str, object]** | The &#x60;client_payload&#x60; that was specified in the &#x60;POST /repos/{owner}/{repo}/dispatches&#x60; request body. | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_repository_dispatch_sample import WebhookRepositoryDispatchSample

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRepositoryDispatchSample from a JSON string
webhook_repository_dispatch_sample_instance = WebhookRepositoryDispatchSample.from_json(json)
# print the JSON string representation of the object
print(WebhookRepositoryDispatchSample.to_json())

# convert the object into a dict
webhook_repository_dispatch_sample_dict = webhook_repository_dispatch_sample_instance.to_dict()
# create an instance of WebhookRepositoryDispatchSample from a dict
webhook_repository_dispatch_sample_from_dict = WebhookRepositoryDispatchSample.from_dict(webhook_repository_dispatch_sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


