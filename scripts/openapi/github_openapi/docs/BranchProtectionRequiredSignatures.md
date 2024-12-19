# BranchProtectionRequiredSignatures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**enabled** | **bool** |  | 

## Example

```python
from github_openapi.models.branch_protection_required_signatures import BranchProtectionRequiredSignatures

# TODO update the JSON string below
json = "{}"
# create an instance of BranchProtectionRequiredSignatures from a JSON string
branch_protection_required_signatures_instance = BranchProtectionRequiredSignatures.from_json(json)
# print the JSON string representation of the object
print(BranchProtectionRequiredSignatures.to_json())

# convert the object into a dict
branch_protection_required_signatures_dict = branch_protection_required_signatures_instance.to_dict()
# create an instance of BranchProtectionRequiredSignatures from a dict
branch_protection_required_signatures_from_dict = BranchProtectionRequiredSignatures.from_dict(branch_protection_required_signatures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


