# RepositoryAdvisoryCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | **str** | A short summary of the advisory. | 
**description** | **str** | A detailed description of what the advisory impacts. | 
**cve_id** | **str** | The Common Vulnerabilities and Exposures (CVE) ID. | [optional] 
**vulnerabilities** | [**List[RepositoryAdvisoryCreateVulnerabilitiesInner]**](RepositoryAdvisoryCreateVulnerabilitiesInner.md) | A product affected by the vulnerability detailed in a repository security advisory. | 
**cwe_ids** | **List[str]** | A list of Common Weakness Enumeration (CWE) IDs. | [optional] 
**credits** | [**List[RepositoryAdvisoryCreateCreditsInner]**](RepositoryAdvisoryCreateCreditsInner.md) | A list of users receiving credit for their participation in the security advisory. | [optional] 
**severity** | **str** | The severity of the advisory. You must choose between setting this field or &#x60;cvss_vector_string&#x60;. | [optional] 
**cvss_vector_string** | **str** | The CVSS vector that calculates the severity of the advisory. You must choose between setting this field or &#x60;severity&#x60;. | [optional] 
**start_private_fork** | **bool** | Whether to create a temporary private fork of the repository to collaborate on a fix. | [optional] [default to False]

## Example

```python
from github_openapi.models.repository_advisory_create import RepositoryAdvisoryCreate

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryAdvisoryCreate from a JSON string
repository_advisory_create_instance = RepositoryAdvisoryCreate.from_json(json)
# print the JSON string representation of the object
print(RepositoryAdvisoryCreate.to_json())

# convert the object into a dict
repository_advisory_create_dict = repository_advisory_create_instance.to_dict()
# create an instance of RepositoryAdvisoryCreate from a dict
repository_advisory_create_from_dict = RepositoryAdvisoryCreate.from_dict(repository_advisory_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


