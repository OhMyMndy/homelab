# WebhooksSecurityAdvisoryVulnerabilitiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_patched_version** | [**WebhooksSecurityAdvisoryVulnerabilitiesInnerFirstPatchedVersion**](WebhooksSecurityAdvisoryVulnerabilitiesInnerFirstPatchedVersion.md) |  | 
**package** | [**WebhooksSecurityAdvisoryVulnerabilitiesInnerPackage**](WebhooksSecurityAdvisoryVulnerabilitiesInnerPackage.md) |  | 
**severity** | **str** |  | 
**vulnerable_version_range** | **str** |  | 

## Example

```python
from github_openapi.models.webhooks_security_advisory_vulnerabilities_inner import WebhooksSecurityAdvisoryVulnerabilitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksSecurityAdvisoryVulnerabilitiesInner from a JSON string
webhooks_security_advisory_vulnerabilities_inner_instance = WebhooksSecurityAdvisoryVulnerabilitiesInner.from_json(json)
# print the JSON string representation of the object
print(WebhooksSecurityAdvisoryVulnerabilitiesInner.to_json())

# convert the object into a dict
webhooks_security_advisory_vulnerabilities_inner_dict = webhooks_security_advisory_vulnerabilities_inner_instance.to_dict()
# create an instance of WebhooksSecurityAdvisoryVulnerabilitiesInner from a dict
webhooks_security_advisory_vulnerabilities_inner_from_dict = WebhooksSecurityAdvisoryVulnerabilitiesInner.from_dict(webhooks_security_advisory_vulnerabilities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


