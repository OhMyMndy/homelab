# WebhookCheckSuiteCompleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**check_suite** | [**WebhookCheckSuiteCompletedCheckSuite**](WebhookCheckSuiteCompletedCheckSuite.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_check_suite_completed import WebhookCheckSuiteCompleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCheckSuiteCompleted from a JSON string
webhook_check_suite_completed_instance = WebhookCheckSuiteCompleted.from_json(json)
# print the JSON string representation of the object
print(WebhookCheckSuiteCompleted.to_json())

# convert the object into a dict
webhook_check_suite_completed_dict = webhook_check_suite_completed_instance.to_dict()
# create an instance of WebhookCheckSuiteCompleted from a dict
webhook_check_suite_completed_from_dict = WebhookCheckSuiteCompleted.from_dict(webhook_check_suite_completed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


