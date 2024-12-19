# WebhookSecurityAdvisoryPublished


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**security_advisory** | [**WebhooksSecurityAdvisory**](WebhooksSecurityAdvisory.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_security_advisory_published import WebhookSecurityAdvisoryPublished

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSecurityAdvisoryPublished from a JSON string
webhook_security_advisory_published_instance = WebhookSecurityAdvisoryPublished.from_json(json)
# print the JSON string representation of the object
print(WebhookSecurityAdvisoryPublished.to_json())

# convert the object into a dict
webhook_security_advisory_published_dict = webhook_security_advisory_published_instance.to_dict()
# create an instance of WebhookSecurityAdvisoryPublished from a dict
webhook_security_advisory_published_from_dict = WebhookSecurityAdvisoryPublished.from_dict(webhook_security_advisory_published_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


