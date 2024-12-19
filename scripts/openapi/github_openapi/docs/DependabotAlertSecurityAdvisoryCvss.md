# DependabotAlertSecurityAdvisoryCvss

Details for the advisory pertaining to the Common Vulnerability Scoring System.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **float** | The overall CVSS score of the advisory. | [readonly] 
**vector_string** | **str** | The full CVSS vector string for the advisory. | [readonly] 

## Example

```python
from github_openapi.models.dependabot_alert_security_advisory_cvss import DependabotAlertSecurityAdvisoryCvss

# TODO update the JSON string below
json = "{}"
# create an instance of DependabotAlertSecurityAdvisoryCvss from a JSON string
dependabot_alert_security_advisory_cvss_instance = DependabotAlertSecurityAdvisoryCvss.from_json(json)
# print the JSON string representation of the object
print(DependabotAlertSecurityAdvisoryCvss.to_json())

# convert the object into a dict
dependabot_alert_security_advisory_cvss_dict = dependabot_alert_security_advisory_cvss_instance.to_dict()
# create an instance of DependabotAlertSecurityAdvisoryCvss from a dict
dependabot_alert_security_advisory_cvss_from_dict = DependabotAlertSecurityAdvisoryCvss.from_dict(dependabot_alert_security_advisory_cvss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


