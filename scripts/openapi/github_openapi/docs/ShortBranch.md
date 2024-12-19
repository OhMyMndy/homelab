# ShortBranch

Short Branch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**commit** | [**ShortBranchCommit**](ShortBranchCommit.md) |  | 
**protected** | **bool** |  | 
**protection** | [**BranchProtection**](BranchProtection.md) |  | [optional] 
**protection_url** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.short_branch import ShortBranch

# TODO update the JSON string below
json = "{}"
# create an instance of ShortBranch from a JSON string
short_branch_instance = ShortBranch.from_json(json)
# print the JSON string representation of the object
print(ShortBranch.to_json())

# convert the object into a dict
short_branch_dict = short_branch_instance.to_dict()
# create an instance of ShortBranch from a dict
short_branch_from_dict = ShortBranch.from_dict(short_branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


