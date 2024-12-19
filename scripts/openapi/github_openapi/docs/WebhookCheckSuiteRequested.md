# WebhookCheckSuiteRequested


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**check_suite** | [**WebhookCheckSuiteRequestedCheckSuite**](WebhookCheckSuiteRequestedCheckSuite.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_check_suite_requested import WebhookCheckSuiteRequested

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCheckSuiteRequested from a JSON string
webhook_check_suite_requested_instance = WebhookCheckSuiteRequested.from_json(json)
# print the JSON string representation of the object
print(WebhookCheckSuiteRequested.to_json())

# convert the object into a dict
webhook_check_suite_requested_dict = webhook_check_suite_requested_instance.to_dict()
# create an instance of WebhookCheckSuiteRequested from a dict
webhook_check_suite_requested_from_dict = WebhookCheckSuiteRequested.from_dict(webhook_check_suite_requested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


