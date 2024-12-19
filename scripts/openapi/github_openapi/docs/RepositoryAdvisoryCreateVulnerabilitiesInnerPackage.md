# RepositoryAdvisoryCreateVulnerabilitiesInnerPackage

The name of the package affected by the vulnerability.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ecosystem** | [**SecurityAdvisoryEcosystems**](SecurityAdvisoryEcosystems.md) |  | 
**name** | **str** | The unique package name within its ecosystem. | [optional] 

## Example

```python
from github_openapi.models.repository_advisory_create_vulnerabilities_inner_package import RepositoryAdvisoryCreateVulnerabilitiesInnerPackage

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryAdvisoryCreateVulnerabilitiesInnerPackage from a JSON string
repository_advisory_create_vulnerabilities_inner_package_instance = RepositoryAdvisoryCreateVulnerabilitiesInnerPackage.from_json(json)
# print the JSON string representation of the object
print(RepositoryAdvisoryCreateVulnerabilitiesInnerPackage.to_json())

# convert the object into a dict
repository_advisory_create_vulnerabilities_inner_package_dict = repository_advisory_create_vulnerabilities_inner_package_instance.to_dict()
# create an instance of RepositoryAdvisoryCreateVulnerabilitiesInnerPackage from a dict
repository_advisory_create_vulnerabilities_inner_package_from_dict = RepositoryAdvisoryCreateVulnerabilitiesInnerPackage.from_dict(repository_advisory_create_vulnerabilities_inner_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


