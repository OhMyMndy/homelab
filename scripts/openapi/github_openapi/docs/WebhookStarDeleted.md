# WebhookStarDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**starred_at** | **object** | The time the star was created. This is a timestamp in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. Will be &#x60;null&#x60; for the &#x60;deleted&#x60; action. | 

## Example

```python
from github_openapi.models.webhook_star_deleted import WebhookStarDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookStarDeleted from a JSON string
webhook_star_deleted_instance = WebhookStarDeleted.from_json(json)
# print the JSON string representation of the object
print(WebhookStarDeleted.to_json())

# convert the object into a dict
webhook_star_deleted_dict = webhook_star_deleted_instance.to_dict()
# create an instance of WebhookStarDeleted from a dict
webhook_star_deleted_from_dict = WebhookStarDeleted.from_dict(webhook_star_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


