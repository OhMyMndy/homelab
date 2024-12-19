# NullableSimpleCommitCommitter

Information about the Git committer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the commit&#39;s committer | 
**email** | **str** | Git email address of the commit&#39;s committer | 

## Example

```python
from github_openapi.models.nullable_simple_commit_committer import NullableSimpleCommitCommitter

# TODO update the JSON string below
json = "{}"
# create an instance of NullableSimpleCommitCommitter from a JSON string
nullable_simple_commit_committer_instance = NullableSimpleCommitCommitter.from_json(json)
# print the JSON string representation of the object
print(NullableSimpleCommitCommitter.to_json())

# convert the object into a dict
nullable_simple_commit_committer_dict = nullable_simple_commit_committer_instance.to_dict()
# create an instance of NullableSimpleCommitCommitter from a dict
nullable_simple_commit_committer_from_dict = NullableSimpleCommitCommitter.from_dict(nullable_simple_commit_committer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


