# ProtectedBranchRequiredStatusCheck

Protected Branch Required Status Check

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**enforcement_level** | **str** |  | [optional] 
**contexts** | **List[str]** |  | 
**checks** | [**List[ProtectedBranchRequiredStatusCheckChecksInner]**](ProtectedBranchRequiredStatusCheckChecksInner.md) |  | 
**contexts_url** | **str** |  | [optional] 
**strict** | **bool** |  | [optional] 

## Example

```python
from github_openapi.models.protected_branch_required_status_check import ProtectedBranchRequiredStatusCheck

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectedBranchRequiredStatusCheck from a JSON string
protected_branch_required_status_check_instance = ProtectedBranchRequiredStatusCheck.from_json(json)
# print the JSON string representation of the object
print(ProtectedBranchRequiredStatusCheck.to_json())

# convert the object into a dict
protected_branch_required_status_check_dict = protected_branch_required_status_check_instance.to_dict()
# create an instance of ProtectedBranchRequiredStatusCheck from a dict
protected_branch_required_status_check_from_dict = ProtectedBranchRequiredStatusCheck.from_dict(protected_branch_required_status_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


