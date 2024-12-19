# DependabotAlertWithRepository

A Dependabot alert.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | The security alert number. | [readonly] 
**state** | **str** | The state of the Dependabot alert. | [readonly] 
**dependency** | [**DependabotAlertWithRepositoryDependency**](DependabotAlertWithRepositoryDependency.md) |  | 
**security_advisory** | [**DependabotAlertSecurityAdvisory**](DependabotAlertSecurityAdvisory.md) |  | 
**security_vulnerability** | [**DependabotAlertSecurityVulnerability**](DependabotAlertSecurityVulnerability.md) |  | 
**url** | **str** | The REST API URL of the alert resource. | [readonly] 
**html_url** | **str** | The GitHub URL of the alert resource. | [readonly] 
**created_at** | **datetime** | The time that the alert was created in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [readonly] 
**updated_at** | **datetime** | The time that the alert was last updated in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [readonly] 
**dismissed_at** | **datetime** | The time that the alert was dismissed in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [readonly] 
**dismissed_by** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**dismissed_reason** | **str** | The reason that the alert was dismissed. | 
**dismissed_comment** | **str** | An optional comment associated with the alert&#39;s dismissal. | 
**fixed_at** | **datetime** | The time that the alert was no longer detected and was considered fixed in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [readonly] 
**auto_dismissed_at** | **datetime** | The time that the alert was auto-dismissed in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] [readonly] 
**repository** | [**SimpleRepository**](SimpleRepository.md) |  | 

## Example

```python
from github_openapi.models.dependabot_alert_with_repository import DependabotAlertWithRepository

# TODO update the JSON string below
json = "{}"
# create an instance of DependabotAlertWithRepository from a JSON string
dependabot_alert_with_repository_instance = DependabotAlertWithRepository.from_json(json)
# print the JSON string representation of the object
print(DependabotAlertWithRepository.to_json())

# convert the object into a dict
dependabot_alert_with_repository_dict = dependabot_alert_with_repository_instance.to_dict()
# create an instance of DependabotAlertWithRepository from a dict
dependabot_alert_with_repository_from_dict = DependabotAlertWithRepository.from_dict(dependabot_alert_with_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


