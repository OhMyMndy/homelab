# DependencyGraphDiffInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_type** | **str** |  | 
**manifest** | **str** |  | 
**ecosystem** | **str** |  | 
**name** | **str** |  | 
**version** | **str** |  | 
**package_url** | **str** |  | 
**license** | **str** |  | 
**source_repository_url** | **str** |  | 
**vulnerabilities** | [**List[DependencyGraphDiffInnerVulnerabilitiesInner]**](DependencyGraphDiffInnerVulnerabilitiesInner.md) |  | 
**scope** | **str** | Where the dependency is utilized. &#x60;development&#x60; means that the dependency is only utilized in the development environment. &#x60;runtime&#x60; means that the dependency is utilized at runtime and in the development environment. | 

## Example

```python
from github_openapi.models.dependency_graph_diff_inner import DependencyGraphDiffInner

# TODO update the JSON string below
json = "{}"
# create an instance of DependencyGraphDiffInner from a JSON string
dependency_graph_diff_inner_instance = DependencyGraphDiffInner.from_json(json)
# print the JSON string representation of the object
print(DependencyGraphDiffInner.to_json())

# convert the object into a dict
dependency_graph_diff_inner_dict = dependency_graph_diff_inner_instance.to_dict()
# create an instance of DependencyGraphDiffInner from a dict
dependency_graph_diff_inner_from_dict = DependencyGraphDiffInner.from_dict(dependency_graph_diff_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


