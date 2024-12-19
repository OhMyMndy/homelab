# NullableSimpleCommit

A commit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | SHA for the commit | 
**tree_id** | **str** | SHA for the commit&#39;s tree | 
**message** | **str** | Message describing the purpose of the commit | 
**timestamp** | **datetime** | Timestamp of the commit | 
**author** | [**NullableSimpleCommitAuthor**](NullableSimpleCommitAuthor.md) |  | 
**committer** | [**NullableSimpleCommitCommitter**](NullableSimpleCommitCommitter.md) |  | 

## Example

```python
from github_openapi.models.nullable_simple_commit import NullableSimpleCommit

# TODO update the JSON string below
json = "{}"
# create an instance of NullableSimpleCommit from a JSON string
nullable_simple_commit_instance = NullableSimpleCommit.from_json(json)
# print the JSON string representation of the object
print(NullableSimpleCommit.to_json())

# convert the object into a dict
nullable_simple_commit_dict = nullable_simple_commit_instance.to_dict()
# create an instance of NullableSimpleCommit from a dict
nullable_simple_commit_from_dict = NullableSimpleCommit.from_dict(nullable_simple_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


