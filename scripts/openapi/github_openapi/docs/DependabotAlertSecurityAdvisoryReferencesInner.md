# DependabotAlertSecurityAdvisoryReferencesInner

A link to additional advisory information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL of the reference. | [readonly] 

## Example

```python
from github_openapi.models.dependabot_alert_security_advisory_references_inner import DependabotAlertSecurityAdvisoryReferencesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DependabotAlertSecurityAdvisoryReferencesInner from a JSON string
dependabot_alert_security_advisory_references_inner_instance = DependabotAlertSecurityAdvisoryReferencesInner.from_json(json)
# print the JSON string representation of the object
print(DependabotAlertSecurityAdvisoryReferencesInner.to_json())

# convert the object into a dict
dependabot_alert_security_advisory_references_inner_dict = dependabot_alert_security_advisory_references_inner_instance.to_dict()
# create an instance of DependabotAlertSecurityAdvisoryReferencesInner from a dict
dependabot_alert_security_advisory_references_inner_from_dict = DependabotAlertSecurityAdvisoryReferencesInner.from_dict(dependabot_alert_security_advisory_references_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


