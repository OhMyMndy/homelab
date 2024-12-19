# FileCommitCommitAuthor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.file_commit_commit_author import FileCommitCommitAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of FileCommitCommitAuthor from a JSON string
file_commit_commit_author_instance = FileCommitCommitAuthor.from_json(json)
# print the JSON string representation of the object
print(FileCommitCommitAuthor.to_json())

# convert the object into a dict
file_commit_commit_author_dict = file_commit_commit_author_instance.to_dict()
# create an instance of FileCommitCommitAuthor from a dict
file_commit_commit_author_from_dict = FileCommitCommitAuthor.from_dict(file_commit_commit_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


