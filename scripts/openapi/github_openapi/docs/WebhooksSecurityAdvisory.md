# WebhooksSecurityAdvisory

The details of the security advisory, including summary, description, and severity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cvss** | [**WebhooksSecurityAdvisoryCvss**](WebhooksSecurityAdvisoryCvss.md) |  | 
**cvss_severities** | [**CvssSeverities**](CvssSeverities.md) |  | [optional] 
**cwes** | [**List[WebhooksSecurityAdvisoryCwesInner]**](WebhooksSecurityAdvisoryCwesInner.md) |  | 
**description** | **str** |  | 
**ghsa_id** | **str** |  | 
**identifiers** | [**List[WebhooksSecurityAdvisoryIdentifiersInner]**](WebhooksSecurityAdvisoryIdentifiersInner.md) |  | 
**published_at** | **str** |  | 
**references** | [**List[WebhooksSecurityAdvisoryReferencesInner]**](WebhooksSecurityAdvisoryReferencesInner.md) |  | 
**severity** | **str** |  | 
**summary** | **str** |  | 
**updated_at** | **str** |  | 
**vulnerabilities** | [**List[WebhooksSecurityAdvisoryVulnerabilitiesInner]**](WebhooksSecurityAdvisoryVulnerabilitiesInner.md) |  | 
**withdrawn_at** | **str** |  | 

## Example

```python
from github_openapi.models.webhooks_security_advisory import WebhooksSecurityAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksSecurityAdvisory from a JSON string
webhooks_security_advisory_instance = WebhooksSecurityAdvisory.from_json(json)
# print the JSON string representation of the object
print(WebhooksSecurityAdvisory.to_json())

# convert the object into a dict
webhooks_security_advisory_dict = webhooks_security_advisory_instance.to_dict()
# create an instance of WebhooksSecurityAdvisory from a dict
webhooks_security_advisory_from_dict = WebhooksSecurityAdvisory.from_dict(webhooks_security_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


