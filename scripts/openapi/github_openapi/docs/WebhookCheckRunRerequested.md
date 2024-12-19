# WebhookCheckRunRerequested


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
from github_openapi.models.webhook_check_run_rerequested import WebhookCheckRunRerequested

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCheckRunRerequested from a JSON string
webhook_check_run_rerequested_instance = WebhookCheckRunRerequested.from_json(json)
# print the JSON string representation of the object
print(WebhookCheckRunRerequested.to_json())

# convert the object into a dict
webhook_check_run_rerequested_dict = webhook_check_run_rerequested_instance.to_dict()
# create an instance of WebhookCheckRunRerequested from a dict
webhook_check_run_rerequested_from_dict = WebhookCheckRunRerequested.from_dict(webhook_check_run_rerequested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


