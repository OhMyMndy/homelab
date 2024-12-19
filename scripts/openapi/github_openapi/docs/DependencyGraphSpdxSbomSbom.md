# DependencyGraphSpdxSbomSbom


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spdxid** | **str** | The SPDX identifier for the SPDX document. | 
**spdx_version** | **str** | The version of the SPDX specification that this document conforms to. | 
**comment** | **str** | An optional comment about the SPDX document. | [optional] 
**creation_info** | [**DependencyGraphSpdxSbomSbomCreationInfo**](DependencyGraphSpdxSbomSbomCreationInfo.md) |  | 
**name** | **str** | The name of the SPDX document. | 
**data_license** | **str** | The license under which the SPDX document is licensed. | 
**document_namespace** | **str** | The namespace for the SPDX document. | 
**packages** | [**List[DependencyGraphSpdxSbomSbomPackagesInner]**](DependencyGraphSpdxSbomSbomPackagesInner.md) |  | 
**relationships** | [**List[DependencyGraphSpdxSbomSbomRelationshipsInner]**](DependencyGraphSpdxSbomSbomRelationshipsInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.dependency_graph_spdx_sbom_sbom import DependencyGraphSpdxSbomSbom

# TODO update the JSON string below
json = "{}"
# create an instance of DependencyGraphSpdxSbomSbom from a JSON string
dependency_graph_spdx_sbom_sbom_instance = DependencyGraphSpdxSbomSbom.from_json(json)
# print the JSON string representation of the object
print(DependencyGraphSpdxSbomSbom.to_json())

# convert the object into a dict
dependency_graph_spdx_sbom_sbom_dict = dependency_graph_spdx_sbom_sbom_instance.to_dict()
# create an instance of DependencyGraphSpdxSbomSbom from a dict
dependency_graph_spdx_sbom_sbom_from_dict = DependencyGraphSpdxSbomSbom.from_dict(dependency_graph_spdx_sbom_sbom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


