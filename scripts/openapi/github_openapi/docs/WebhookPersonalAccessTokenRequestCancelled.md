# WebhookPersonalAccessTokenRequestCancelled


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**personal_access_token_request** | [**PersonalAccessTokenRequest**](PersonalAccessTokenRequest.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | 

## Example

```python
from github_openapi.models.webhook_personal_access_token_request_cancelled import WebhookPersonalAccessTokenRequestCancelled

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPersonalAccessTokenRequestCancelled from a JSON string
webhook_personal_access_token_request_cancelled_instance = WebhookPersonalAccessTokenRequestCancelled.from_json(json)
# print the JSON string representation of the object
print(WebhookPersonalAccessTokenRequestCancelled.to_json())

# convert the object into a dict
webhook_personal_access_token_request_cancelled_dict = webhook_personal_access_token_request_cancelled_instance.to_dict()
# create an instance of WebhookPersonalAccessTokenRequestCancelled from a dict
webhook_personal_access_token_request_cancelled_from_dict = WebhookPersonalAccessTokenRequestCancelled.from_dict(webhook_personal_access_token_request_cancelled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


