# DependencyGraphSpdxSbomSbomPackagesInnerExternalRefsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_category** | **str** | The category of reference to an external resource this reference refers to. | 
**reference_locator** | **str** | A locator for the particular external resource this reference refers to. | 
**reference_type** | **str** | The category of reference to an external resource this reference refers to. | 

## Example

```python
from github_openapi.models.dependency_graph_spdx_sbom_sbom_packages_inner_external_refs_inner import DependencyGraphSpdxSbomSbomPackagesInnerExternalRefsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DependencyGraphSpdxSbomSbomPackagesInnerExternalRefsInner from a JSON string
dependency_graph_spdx_sbom_sbom_packages_inner_external_refs_inner_instance = DependencyGraphSpdxSbomSbomPackagesInnerExternalRefsInner.from_json(json)
# print the JSON string representation of the object
print(DependencyGraphSpdxSbomSbomPackagesInnerExternalRefsInner.to_json())

# convert the object into a dict
dependency_graph_spdx_sbom_sbom_packages_inner_external_refs_inner_dict = dependency_graph_spdx_sbom_sbom_packages_inner_external_refs_inner_instance.to_dict()
# create an instance of DependencyGraphSpdxSbomSbomPackagesInnerExternalRefsInner from a dict
dependency_graph_spdx_sbom_sbom_packages_inner_external_refs_inner_from_dict = DependencyGraphSpdxSbomSbomPackagesInnerExternalRefsInner.from_dict(dependency_graph_spdx_sbom_sbom_packages_inner_external_refs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


