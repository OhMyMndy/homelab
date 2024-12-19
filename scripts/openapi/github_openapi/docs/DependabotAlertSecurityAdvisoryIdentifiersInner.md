# DependabotAlertSecurityAdvisoryIdentifiersInner

An advisory identifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of advisory identifier. | [readonly] 
**value** | **str** | The value of the advisory identifer. | [readonly] 

## Example

```python
from github_openapi.models.dependabot_alert_security_advisory_identifiers_inner import DependabotAlertSecurityAdvisoryIdentifiersInner

# TODO update the JSON string below
json = "{}"
# create an instance of DependabotAlertSecurityAdvisoryIdentifiersInner from a JSON string
dependabot_alert_security_advisory_identifiers_inner_instance = DependabotAlertSecurityAdvisoryIdentifiersInner.from_json(json)
# print the JSON string representation of the object
print(DependabotAlertSecurityAdvisoryIdentifiersInner.to_json())

# convert the object into a dict
dependabot_alert_security_advisory_identifiers_inner_dict = dependabot_alert_security_advisory_identifiers_inner_instance.to_dict()
# create an instance of DependabotAlertSecurityAdvisoryIdentifiersInner from a dict
dependabot_alert_security_advisory_identifiers_inner_from_dict = DependabotAlertSecurityAdvisoryIdentifiersInner.from_dict(dependabot_alert_security_advisory_identifiers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


