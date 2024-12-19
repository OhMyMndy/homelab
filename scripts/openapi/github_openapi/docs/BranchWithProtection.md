# BranchWithProtection

Branch With Protection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**commit** | [**Commit**](Commit.md) |  | 
**links** | [**BranchWithProtectionLinks**](BranchWithProtectionLinks.md) |  | 
**protected** | **bool** |  | 
**protection** | [**BranchProtection**](BranchProtection.md) |  | 
**protection_url** | **str** |  | 
**pattern** | **str** |  | [optional] 
**required_approving_review_count** | **int** |  | [optional] 

## Example

```python
from github_openapi.models.branch_with_protection import BranchWithProtection

# TODO update the JSON string below
json = "{}"
# create an instance of BranchWithProtection from a JSON string
branch_with_protection_instance = BranchWithProtection.from_json(json)
# print the JSON string representation of the object
print(BranchWithProtection.to_json())

# convert the object into a dict
branch_with_protection_dict = branch_with_protection_instance.to_dict()
# create an instance of BranchWithProtection from a dict
branch_with_protection_from_dict = BranchWithProtection.from_dict(branch_with_protection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


