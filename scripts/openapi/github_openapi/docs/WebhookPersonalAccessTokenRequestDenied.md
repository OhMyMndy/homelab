# WebhookPersonalAccessTokenRequestDenied


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**personal_access_token_request** | [**PersonalAccessTokenRequest**](PersonalAccessTokenRequest.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | 

## Example

```python
from github_openapi.models.webhook_personal_access_token_request_denied import WebhookPersonalAccessTokenRequestDenied

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPersonalAccessTokenRequestDenied from a JSON string
webhook_personal_access_token_request_denied_instance = WebhookPersonalAccessTokenRequestDenied.from_json(json)
# print the JSON string representation of the object
print(WebhookPersonalAccessTokenRequestDenied.to_json())

# convert the object into a dict
webhook_personal_access_token_request_denied_dict = webhook_personal_access_token_request_denied_instance.to_dict()
# create an instance of WebhookPersonalAccessTokenRequestDenied from a dict
webhook_personal_access_token_request_denied_from_dict = WebhookPersonalAccessTokenRequestDenied.from_dict(webhook_personal_access_token_request_denied_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


