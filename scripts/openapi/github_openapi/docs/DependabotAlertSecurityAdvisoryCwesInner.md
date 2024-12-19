# DependabotAlertSecurityAdvisoryCwesInner

A CWE weakness assigned to the advisory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cwe_id** | **str** | The unique CWE ID. | [readonly] 
**name** | **str** | The short, plain text name of the CWE. | [readonly] 

## Example

```python
from github_openapi.models.dependabot_alert_security_advisory_cwes_inner import DependabotAlertSecurityAdvisoryCwesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DependabotAlertSecurityAdvisoryCwesInner from a JSON string
dependabot_alert_security_advisory_cwes_inner_instance = DependabotAlertSecurityAdvisoryCwesInner.from_json(json)
# print the JSON string representation of the object
print(DependabotAlertSecurityAdvisoryCwesInner.to_json())

# convert the object into a dict
dependabot_alert_security_advisory_cwes_inner_dict = dependabot_alert_security_advisory_cwes_inner_instance.to_dict()
# create an instance of DependabotAlertSecurityAdvisoryCwesInner from a dict
dependabot_alert_security_advisory_cwes_inner_from_dict = DependabotAlertSecurityAdvisoryCwesInner.from_dict(dependabot_alert_security_advisory_cwes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


