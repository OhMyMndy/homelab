# GlobalAdvisoryCwesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cwe_id** | **str** | The Common Weakness Enumeration (CWE) identifier. | 
**name** | **str** | The name of the CWE. | [readonly] 

## Example

```python
from github_openapi.models.global_advisory_cwes_inner import GlobalAdvisoryCwesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalAdvisoryCwesInner from a JSON string
global_advisory_cwes_inner_instance = GlobalAdvisoryCwesInner.from_json(json)
# print the JSON string representation of the object
print(GlobalAdvisoryCwesInner.to_json())

# convert the object into a dict
global_advisory_cwes_inner_dict = global_advisory_cwes_inner_instance.to_dict()
# create an instance of GlobalAdvisoryCwesInner from a dict
global_advisory_cwes_inner_from_dict = GlobalAdvisoryCwesInner.from_dict(global_advisory_cwes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


