# ShortBranchCommit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.short_branch_commit import ShortBranchCommit

# TODO update the JSON string below
json = "{}"
# create an instance of ShortBranchCommit from a JSON string
short_branch_commit_instance = ShortBranchCommit.from_json(json)
# print the JSON string representation of the object
print(ShortBranchCommit.to_json())

# convert the object into a dict
short_branch_commit_dict = short_branch_commit_instance.to_dict()
# create an instance of ShortBranchCommit from a dict
short_branch_commit_from_dict = ShortBranchCommit.from_dict(short_branch_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


