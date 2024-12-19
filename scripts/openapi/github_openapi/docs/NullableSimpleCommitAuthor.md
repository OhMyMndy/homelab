# NullableSimpleCommitAuthor

Information about the Git author

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the commit&#39;s author | 
**email** | **str** | Git email address of the commit&#39;s author | 

## Example

```python
from github_openapi.models.nullable_simple_commit_author import NullableSimpleCommitAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of NullableSimpleCommitAuthor from a JSON string
nullable_simple_commit_author_instance = NullableSimpleCommitAuthor.from_json(json)
# print the JSON string representation of the object
print(NullableSimpleCommitAuthor.to_json())

# convert the object into a dict
nullable_simple_commit_author_dict = nullable_simple_commit_author_instance.to_dict()
# create an instance of NullableSimpleCommitAuthor from a dict
nullable_simple_commit_author_from_dict = NullableSimpleCommitAuthor.from_dict(nullable_simple_commit_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


