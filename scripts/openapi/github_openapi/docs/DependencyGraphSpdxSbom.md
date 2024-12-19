# DependencyGraphSpdxSbom

A schema for the SPDX JSON format returned by the Dependency Graph.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sbom** | [**DependencyGraphSpdxSbomSbom**](DependencyGraphSpdxSbomSbom.md) |  | 

## Example

```python
from github_openapi.models.dependency_graph_spdx_sbom import DependencyGraphSpdxSbom

# TODO update the JSON string below
json = "{}"
# create an instance of DependencyGraphSpdxSbom from a JSON string
dependency_graph_spdx_sbom_instance = DependencyGraphSpdxSbom.from_json(json)
# print the JSON string representation of the object
print(DependencyGraphSpdxSbom.to_json())

# convert the object into a dict
dependency_graph_spdx_sbom_dict = dependency_graph_spdx_sbom_instance.to_dict()
# create an instance of DependencyGraphSpdxSbom from a dict
dependency_graph_spdx_sbom_from_dict = DependencyGraphSpdxSbom.from_dict(dependency_graph_spdx_sbom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


