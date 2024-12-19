# DependencyGraphDiffInnerVulnerabilitiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**severity** | **str** |  | 
**advisory_ghsa_id** | **str** |  | 
**advisory_summary** | **str** |  | 
**advisory_url** | **str** |  | 

## Example

```python
from github_openapi.models.dependency_graph_diff_inner_vulnerabilities_inner import DependencyGraphDiffInnerVulnerabilitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DependencyGraphDiffInnerVulnerabilitiesInner from a JSON string
dependency_graph_diff_inner_vulnerabilities_inner_instance = DependencyGraphDiffInnerVulnerabilitiesInner.from_json(json)
# print the JSON string representation of the object
print(DependencyGraphDiffInnerVulnerabilitiesInner.to_json())

# convert the object into a dict
dependency_graph_diff_inner_vulnerabilities_inner_dict = dependency_graph_diff_inner_vulnerabilities_inner_instance.to_dict()
# create an instance of DependencyGraphDiffInnerVulnerabilitiesInner from a dict
dependency_graph_diff_inner_vulnerabilities_inner_from_dict = DependencyGraphDiffInnerVulnerabilitiesInner.from_dict(dependency_graph_diff_inner_vulnerabilities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


