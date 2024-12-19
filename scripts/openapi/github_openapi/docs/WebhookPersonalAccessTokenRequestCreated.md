# WebhookPersonalAccessTokenRequestCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**personal_access_token_request** | [**PersonalAccessTokenRequest**](PersonalAccessTokenRequest.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_personal_access_token_request_created import WebhookPersonalAccessTokenRequestCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPersonalAccessTokenRequestCreated from a JSON string
webhook_personal_access_token_request_created_instance = WebhookPersonalAccessTokenRequestCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookPersonalAccessTokenRequestCreated.to_json())

# convert the object into a dict
webhook_personal_access_token_request_created_dict = webhook_personal_access_token_request_created_instance.to_dict()
# create an instance of WebhookPersonalAccessTokenRequestCreated from a dict
webhook_personal_access_token_request_created_from_dict = WebhookPersonalAccessTokenRequestCreated.from_dict(webhook_personal_access_token_request_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


