# DependencyGraphSpdxSbomSbomPackagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spdxid** | **str** | A unique SPDX identifier for the package. | [optional] 
**name** | **str** | The name of the package. | [optional] 
**version_info** | **str** | The version of the package. If the package does not have an exact version specified, a version range is given. | [optional] 
**download_location** | **str** | The location where the package can be downloaded, or NOASSERTION if this has not been determined. | [optional] 
**files_analyzed** | **bool** | Whether the package&#39;s file content has been subjected to analysis during the creation of the SPDX document. | [optional] 
**license_concluded** | **str** | The license of the package as determined while creating the SPDX document. | [optional] 
**license_declared** | **str** | The license of the package as declared by its author, or NOASSERTION if this information was not available when the SPDX document was created. | [optional] 
**supplier** | **str** | The distribution source of this package, or NOASSERTION if this was not determined. | [optional] 
**copyright_text** | **str** | The copyright holders of the package, and any dates present with those notices, if available. | [optional] 
**external_refs** | [**List[DependencyGraphSpdxSbomSbomPackagesInnerExternalRefsInner]**](DependencyGraphSpdxSbomSbomPackagesInnerExternalRefsInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.dependency_graph_spdx_sbom_sbom_packages_inner import DependencyGraphSpdxSbomSbomPackagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DependencyGraphSpdxSbomSbomPackagesInner from a JSON string
dependency_graph_spdx_sbom_sbom_packages_inner_instance = DependencyGraphSpdxSbomSbomPackagesInner.from_json(json)
# print the JSON string representation of the object
print(DependencyGraphSpdxSbomSbomPackagesInner.to_json())

# convert the object into a dict
dependency_graph_spdx_sbom_sbom_packages_inner_dict = dependency_graph_spdx_sbom_sbom_packages_inner_instance.to_dict()
# create an instance of DependencyGraphSpdxSbomSbomPackagesInner from a dict
dependency_graph_spdx_sbom_sbom_packages_inner_from_dict = DependencyGraphSpdxSbomSbomPackagesInner.from_dict(dependency_graph_spdx_sbom_sbom_packages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


