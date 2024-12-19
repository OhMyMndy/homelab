# WebhookSecurityAndAnalysis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**WebhookSecurityAndAnalysisChanges**](WebhookSecurityAndAnalysisChanges.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**FullRepository**](FullRepository.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_security_and_analysis import WebhookSecurityAndAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSecurityAndAnalysis from a JSON string
webhook_security_and_analysis_instance = WebhookSecurityAndAnalysis.from_json(json)
# print the JSON string representation of the object
print(WebhookSecurityAndAnalysis.to_json())

# convert the object into a dict
webhook_security_and_analysis_dict = webhook_security_and_analysis_instance.to_dict()
# create an instance of WebhookSecurityAndAnalysis from a dict
webhook_security_and_analysis_from_dict = WebhookSecurityAndAnalysis.from_dict(webhook_security_and_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


