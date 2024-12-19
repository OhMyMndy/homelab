# WebhookGithubAppAuthorizationRevoked


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_github_app_authorization_revoked import WebhookGithubAppAuthorizationRevoked

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookGithubAppAuthorizationRevoked from a JSON string
webhook_github_app_authorization_revoked_instance = WebhookGithubAppAuthorizationRevoked.from_json(json)
# print the JSON string representation of the object
print(WebhookGithubAppAuthorizationRevoked.to_json())

# convert the object into a dict
webhook_github_app_authorization_revoked_dict = webhook_github_app_authorization_revoked_instance.to_dict()
# create an instance of WebhookGithubAppAuthorizationRevoked from a dict
webhook_github_app_authorization_revoked_from_dict = WebhookGithubAppAuthorizationRevoked.from_dict(webhook_github_app_authorization_revoked_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


