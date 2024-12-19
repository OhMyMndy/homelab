# RepositoryAdvisoryCreateVulnerabilitiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package** | [**RepositoryAdvisoryCreateVulnerabilitiesInnerPackage**](RepositoryAdvisoryCreateVulnerabilitiesInnerPackage.md) |  | 
**vulnerable_version_range** | **str** | The range of the package versions affected by the vulnerability. | [optional] 
**patched_versions** | **str** | The package version(s) that resolve the vulnerability. | [optional] 
**vulnerable_functions** | **List[str]** | The functions in the package that are affected. | [optional] 

## Example

```python
from github_openapi.models.repository_advisory_create_vulnerabilities_inner import RepositoryAdvisoryCreateVulnerabilitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryAdvisoryCreateVulnerabilitiesInner from a JSON string
repository_advisory_create_vulnerabilities_inner_instance = RepositoryAdvisoryCreateVulnerabilitiesInner.from_json(json)
# print the JSON string representation of the object
print(RepositoryAdvisoryCreateVulnerabilitiesInner.to_json())

# convert the object into a dict
repository_advisory_create_vulnerabilities_inner_dict = repository_advisory_create_vulnerabilities_inner_instance.to_dict()
# create an instance of RepositoryAdvisoryCreateVulnerabilitiesInner from a dict
repository_advisory_create_vulnerabilities_inner_from_dict = RepositoryAdvisoryCreateVulnerabilitiesInner.from_dict(repository_advisory_create_vulnerabilities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


