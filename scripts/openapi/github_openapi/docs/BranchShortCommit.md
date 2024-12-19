# BranchShortCommit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.branch_short_commit import BranchShortCommit

# TODO update the JSON string below
json = "{}"
# create an instance of BranchShortCommit from a JSON string
branch_short_commit_instance = BranchShortCommit.from_json(json)
# print the JSON string representation of the object
print(BranchShortCommit.to_json())

# convert the object into a dict
branch_short_commit_dict = branch_short_commit_instance.to_dict()
# create an instance of BranchShortCommit from a dict
branch_short_commit_from_dict = BranchShortCommit.from_dict(branch_short_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


