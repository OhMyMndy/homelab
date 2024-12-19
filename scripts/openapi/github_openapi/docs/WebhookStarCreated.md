# WebhookStarCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**starred_at** | **str** | The time the star was created. This is a timestamp in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. Will be &#x60;null&#x60; for the &#x60;deleted&#x60; action. | 

## Example

```python
from github_openapi.models.webhook_star_created import WebhookStarCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookStarCreated from a JSON string
webhook_star_created_instance = WebhookStarCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookStarCreated.to_json())

# convert the object into a dict
webhook_star_created_dict = webhook_star_created_instance.to_dict()
# create an instance of WebhookStarCreated from a dict
webhook_star_created_from_dict = WebhookStarCreated.from_dict(webhook_star_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


