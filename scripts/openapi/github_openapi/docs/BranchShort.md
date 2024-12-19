# BranchShort

Branch Short

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**commit** | [**BranchShortCommit**](BranchShortCommit.md) |  | 
**protected** | **bool** |  | 

## Example

```python
from github_openapi.models.branch_short import BranchShort

# TODO update the JSON string below
json = "{}"
# create an instance of BranchShort from a JSON string
branch_short_instance = BranchShort.from_json(json)
# print the JSON string representation of the object
print(BranchShort.to_json())

# convert the object into a dict
branch_short_dict = branch_short_instance.to_dict()
# create an instance of BranchShort from a dict
branch_short_from_dict = BranchShort.from_dict(branch_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


