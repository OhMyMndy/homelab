# WebhookCodeScanningAlertClosedByUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**alert** | [**WebhookCodeScanningAlertClosedByUserAlert**](WebhookCodeScanningAlertClosedByUserAlert.md) |  | 
**commit_oid** | **str** | The commit SHA of the code scanning alert. When the action is &#x60;reopened_by_user&#x60; or &#x60;closed_by_user&#x60;, the event was triggered by the &#x60;sender&#x60; and this value will be empty. | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**ref** | **str** | The Git reference of the code scanning alert. When the action is &#x60;reopened_by_user&#x60; or &#x60;closed_by_user&#x60;, the event was triggered by the &#x60;sender&#x60; and this value will be empty. | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_code_scanning_alert_closed_by_user import WebhookCodeScanningAlertClosedByUser

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCodeScanningAlertClosedByUser from a JSON string
webhook_code_scanning_alert_closed_by_user_instance = WebhookCodeScanningAlertClosedByUser.from_json(json)
# print the JSON string representation of the object
print(WebhookCodeScanningAlertClosedByUser.to_json())

# convert the object into a dict
webhook_code_scanning_alert_closed_by_user_dict = webhook_code_scanning_alert_closed_by_user_instance.to_dict()
# create an instance of WebhookCodeScanningAlertClosedByUser from a dict
webhook_code_scanning_alert_closed_by_user_from_dict = WebhookCodeScanningAlertClosedByUser.from_dict(webhook_code_scanning_alert_closed_by_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


