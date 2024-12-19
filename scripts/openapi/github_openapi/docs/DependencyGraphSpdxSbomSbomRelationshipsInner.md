# DependencyGraphSpdxSbomSbomRelationshipsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationship_type** | **str** | The type of relationship between the two SPDX elements. | [optional] 
**spdx_element_id** | **str** | The SPDX identifier of the package that is the source of the relationship. | [optional] 
**related_spdx_element** | **str** | The SPDX identifier of the package that is the target of the relationship. | [optional] 

## Example

```python
from github_openapi.models.dependency_graph_spdx_sbom_sbom_relationships_inner import DependencyGraphSpdxSbomSbomRelationshipsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DependencyGraphSpdxSbomSbomRelationshipsInner from a JSON string
dependency_graph_spdx_sbom_sbom_relationships_inner_instance = DependencyGraphSpdxSbomSbomRelationshipsInner.from_json(json)
# print the JSON string representation of the object
print(DependencyGraphSpdxSbomSbomRelationshipsInner.to_json())

# convert the object into a dict
dependency_graph_spdx_sbom_sbom_relationships_inner_dict = dependency_graph_spdx_sbom_sbom_relationships_inner_instance.to_dict()
# create an instance of DependencyGraphSpdxSbomSbomRelationshipsInner from a dict
dependency_graph_spdx_sbom_sbom_relationships_inner_from_dict = DependencyGraphSpdxSbomSbomRelationshipsInner.from_dict(dependency_graph_spdx_sbom_sbom_relationships_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


