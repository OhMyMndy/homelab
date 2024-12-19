# DependabotUpdateAlertRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state of the Dependabot alert. A &#x60;dismissed_reason&#x60; must be provided when setting the state to &#x60;dismissed&#x60;. | 
**dismissed_reason** | **str** | **Required when &#x60;state&#x60; is &#x60;dismissed&#x60;.** A reason for dismissing the alert. | [optional] 
**dismissed_comment** | **str** | An optional comment associated with dismissing the alert. | [optional] 

## Example

```python
from github_openapi.models.dependabot_update_alert_request import DependabotUpdateAlertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DependabotUpdateAlertRequest from a JSON string
dependabot_update_alert_request_instance = DependabotUpdateAlertRequest.from_json(json)
# print the JSON string representation of the object
print(DependabotUpdateAlertRequest.to_json())

# convert the object into a dict
dependabot_update_alert_request_dict = dependabot_update_alert_request_instance.to_dict()
# create an instance of DependabotUpdateAlertRequest from a dict
dependabot_update_alert_request_from_dict = DependabotUpdateAlertRequest.from_dict(dependabot_update_alert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


