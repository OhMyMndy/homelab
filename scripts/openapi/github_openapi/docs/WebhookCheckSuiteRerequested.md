# WebhookCheckSuiteRerequested


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**check_suite** | [**WebhookCheckSuiteRerequestedCheckSuite**](WebhookCheckSuiteRerequestedCheckSuite.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_check_suite_rerequested import WebhookCheckSuiteRerequested

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCheckSuiteRerequested from a JSON string
webhook_check_suite_rerequested_instance = WebhookCheckSuiteRerequested.from_json(json)
# print the JSON string representation of the object
print(WebhookCheckSuiteRerequested.to_json())

# convert the object into a dict
webhook_check_suite_rerequested_dict = webhook_check_suite_rerequested_instance.to_dict()
# create an instance of WebhookCheckSuiteRerequested from a dict
webhook_check_suite_rerequested_from_dict = WebhookCheckSuiteRerequested.from_dict(webhook_check_suite_rerequested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


