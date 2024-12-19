# GlobalAdvisory

A GitHub Security Advisory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ghsa_id** | **str** | The GitHub Security Advisory ID. | [readonly] 
**cve_id** | **str** | The Common Vulnerabilities and Exposures (CVE) ID. | [readonly] 
**url** | **str** | The API URL for the advisory. | [readonly] 
**html_url** | **str** | The URL for the advisory. | [readonly] 
**repository_advisory_url** | **str** | The API URL for the repository advisory. | [readonly] 
**summary** | **str** | A short summary of the advisory. | 
**description** | **str** | A detailed description of what the advisory entails. | 
**type** | **str** | The type of advisory. | [readonly] 
**severity** | **str** | The severity of the advisory. | 
**source_code_location** | **str** | The URL of the advisory&#39;s source code. | 
**identifiers** | [**List[GlobalAdvisoryIdentifiersInner]**](GlobalAdvisoryIdentifiersInner.md) |  | [readonly] 
**references** | **List[str]** |  | 
**published_at** | **datetime** | The date and time of when the advisory was published, in ISO 8601 format. | [readonly] 
**updated_at** | **datetime** | The date and time of when the advisory was last updated, in ISO 8601 format. | [readonly] 
**github_reviewed_at** | **datetime** | The date and time of when the advisory was reviewed by GitHub, in ISO 8601 format. | [readonly] 
**nvd_published_at** | **datetime** | The date and time when the advisory was published in the National Vulnerability Database, in ISO 8601 format. This field is only populated when the advisory is imported from the National Vulnerability Database. | [readonly] 
**withdrawn_at** | **datetime** | The date and time of when the advisory was withdrawn, in ISO 8601 format. | [readonly] 
**vulnerabilities** | [**List[Vulnerability]**](Vulnerability.md) | The products and respective version ranges affected by the advisory. | 
**cvss** | [**GlobalAdvisoryCvss**](GlobalAdvisoryCvss.md) |  | 
**cvss_severities** | [**CvssSeverities**](CvssSeverities.md) |  | [optional] 
**cwes** | [**List[GlobalAdvisoryCwesInner]**](GlobalAdvisoryCwesInner.md) |  | 
**epss** | [**GlobalAdvisoryEpss**](GlobalAdvisoryEpss.md) |  | [optional] 
**credits** | [**List[GlobalAdvisoryCreditsInner]**](GlobalAdvisoryCreditsInner.md) | The users who contributed to the advisory. | [readonly] 

## Example

```python
from github_openapi.models.global_advisory import GlobalAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalAdvisory from a JSON string
global_advisory_instance = GlobalAdvisory.from_json(json)
# print the JSON string representation of the object
print(GlobalAdvisory.to_json())

# convert the object into a dict
global_advisory_dict = global_advisory_instance.to_dict()
# create an instance of GlobalAdvisory from a dict
global_advisory_from_dict = GlobalAdvisory.from_dict(global_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


