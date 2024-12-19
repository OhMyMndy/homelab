# WebhookCheckRunCompleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**check_run** | [**CheckRunWithSimpleCheckSuite**](CheckRunWithSimpleCheckSuite.md) |  | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_check_run_completed import WebhookCheckRunCompleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCheckRunCompleted from a JSON string
webhook_check_run_completed_instance = WebhookCheckRunCompleted.from_json(json)
# print the JSON string representation of the object
print(WebhookCheckRunCompleted.to_json())

# convert the object into a dict
webhook_check_run_completed_dict = webhook_check_run_completed_instance.to_dict()
# create an instance of WebhookCheckRunCompleted from a dict
webhook_check_run_completed_from_dict = WebhookCheckRunCompleted.from_dict(webhook_check_run_completed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


