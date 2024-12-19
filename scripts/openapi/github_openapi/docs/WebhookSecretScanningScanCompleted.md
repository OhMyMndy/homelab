# WebhookSecretScanningScanCompleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**type** | **str** | What type of scan was completed | 
**source** | **str** | What type of content was scanned | 
**started_at** | **datetime** | The time that the alert was resolved in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | 
**completed_at** | **datetime** | The time that the alert was resolved in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | 
**secret_types** | **List[str]** | List of patterns that were updated. This will be empty for normal backfill scans or custom pattern updates | [optional] 
**custom_pattern_name** | **str** | If the scan was triggered by a custom pattern update, this will be the name of the pattern that was updated | [optional] 
**custom_pattern_scope** | **str** | If the scan was triggered by a custom pattern update, this will be the scope of the pattern that was updated | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_secret_scanning_scan_completed import WebhookSecretScanningScanCompleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSecretScanningScanCompleted from a JSON string
webhook_secret_scanning_scan_completed_instance = WebhookSecretScanningScanCompleted.from_json(json)
# print the JSON string representation of the object
print(WebhookSecretScanningScanCompleted.to_json())

# convert the object into a dict
webhook_secret_scanning_scan_completed_dict = webhook_secret_scanning_scan_completed_instance.to_dict()
# create an instance of WebhookSecretScanningScanCompleted from a dict
webhook_secret_scanning_scan_completed_from_dict = WebhookSecretScanningScanCompleted.from_dict(webhook_secret_scanning_scan_completed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


