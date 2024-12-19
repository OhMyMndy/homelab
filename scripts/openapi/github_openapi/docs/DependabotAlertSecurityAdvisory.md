# DependabotAlertSecurityAdvisory

Details for the GitHub Security Advisory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ghsa_id** | **str** | The unique GitHub Security Advisory ID assigned to the advisory. | [readonly] 
**cve_id** | **str** | The unique CVE ID assigned to the advisory. | [readonly] 
**summary** | **str** | A short, plain text summary of the advisory. | [readonly] 
**description** | **str** | A long-form Markdown-supported description of the advisory. | [readonly] 
**vulnerabilities** | [**List[DependabotAlertSecurityVulnerability]**](DependabotAlertSecurityVulnerability.md) | Vulnerable version range information for the advisory. | [readonly] 
**severity** | **str** | The severity of the advisory. | [readonly] 
**cvss** | [**DependabotAlertSecurityAdvisoryCvss**](DependabotAlertSecurityAdvisoryCvss.md) |  | 
**cvss_severities** | [**CvssSeverities**](CvssSeverities.md) |  | [optional] 
**cwes** | [**List[DependabotAlertSecurityAdvisoryCwesInner]**](DependabotAlertSecurityAdvisoryCwesInner.md) | Details for the advisory pertaining to Common Weakness Enumeration. | [readonly] 
**identifiers** | [**List[DependabotAlertSecurityAdvisoryIdentifiersInner]**](DependabotAlertSecurityAdvisoryIdentifiersInner.md) | Values that identify this advisory among security information sources. | [readonly] 
**references** | [**List[DependabotAlertSecurityAdvisoryReferencesInner]**](DependabotAlertSecurityAdvisoryReferencesInner.md) | Links to additional advisory information. | [readonly] 
**published_at** | **datetime** | The time that the advisory was published in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [readonly] 
**updated_at** | **datetime** | The time that the advisory was last modified in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [readonly] 
**withdrawn_at** | **datetime** | The time that the advisory was withdrawn in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [readonly] 

## Example

```python
from github_openapi.models.dependabot_alert_security_advisory import DependabotAlertSecurityAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of DependabotAlertSecurityAdvisory from a JSON string
dependabot_alert_security_advisory_instance = DependabotAlertSecurityAdvisory.from_json(json)
# print the JSON string representation of the object
print(DependabotAlertSecurityAdvisory.to_json())

# convert the object into a dict
dependabot_alert_security_advisory_dict = dependabot_alert_security_advisory_instance.to_dict()
# create an instance of DependabotAlertSecurityAdvisory from a dict
dependabot_alert_security_advisory_from_dict = DependabotAlertSecurityAdvisory.from_dict(dependabot_alert_security_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


