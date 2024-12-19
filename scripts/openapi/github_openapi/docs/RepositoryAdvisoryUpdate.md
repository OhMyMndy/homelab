# RepositoryAdvisoryUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | **str** | A short summary of the advisory. | [optional] 
**description** | **str** | A detailed description of what the advisory impacts. | [optional] 
**cve_id** | **str** | The Common Vulnerabilities and Exposures (CVE) ID. | [optional] 
**vulnerabilities** | [**List[RepositoryAdvisoryCreateVulnerabilitiesInner]**](RepositoryAdvisoryCreateVulnerabilitiesInner.md) | A product affected by the vulnerability detailed in a repository security advisory. | [optional] 
**cwe_ids** | **List[str]** | A list of Common Weakness Enumeration (CWE) IDs. | [optional] 
**credits** | [**List[RepositoryAdvisoryCreateCreditsInner]**](RepositoryAdvisoryCreateCreditsInner.md) | A list of users receiving credit for their participation in the security advisory. | [optional] 
**severity** | **str** | The severity of the advisory. You must choose between setting this field or &#x60;cvss_vector_string&#x60;. | [optional] 
**cvss_vector_string** | **str** | The CVSS vector that calculates the severity of the advisory. You must choose between setting this field or &#x60;severity&#x60;. | [optional] 
**state** | **str** | The state of the advisory. | [optional] 
**collaborating_users** | **List[str]** | A list of usernames who have been granted write access to the advisory. | [optional] 
**collaborating_teams** | **List[str]** | A list of team slugs which have been granted write access to the advisory. | [optional] 

## Example

```python
from github_openapi.models.repository_advisory_update import RepositoryAdvisoryUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryAdvisoryUpdate from a JSON string
repository_advisory_update_instance = RepositoryAdvisoryUpdate.from_json(json)
# print the JSON string representation of the object
print(RepositoryAdvisoryUpdate.to_json())

# convert the object into a dict
repository_advisory_update_dict = repository_advisory_update_instance.to_dict()
# create an instance of RepositoryAdvisoryUpdate from a dict
repository_advisory_update_from_dict = RepositoryAdvisoryUpdate.from_dict(repository_advisory_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


