# DependencyGraphSpdxSbomSbomCreationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **str** | The date and time the SPDX document was created. | 
**creators** | **List[str]** | The tools that were used to generate the SPDX document. | 

## Example

```python
from github_openapi.models.dependency_graph_spdx_sbom_sbom_creation_info import DependencyGraphSpdxSbomSbomCreationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DependencyGraphSpdxSbomSbomCreationInfo from a JSON string
dependency_graph_spdx_sbom_sbom_creation_info_instance = DependencyGraphSpdxSbomSbomCreationInfo.from_json(json)
# print the JSON string representation of the object
print(DependencyGraphSpdxSbomSbomCreationInfo.to_json())

# convert the object into a dict
dependency_graph_spdx_sbom_sbom_creation_info_dict = dependency_graph_spdx_sbom_sbom_creation_info_instance.to_dict()
# create an instance of DependencyGraphSpdxSbomSbomCreationInfo from a dict
dependency_graph_spdx_sbom_sbom_creation_info_from_dict = DependencyGraphSpdxSbomSbomCreationInfo.from_dict(dependency_graph_spdx_sbom_sbom_creation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


