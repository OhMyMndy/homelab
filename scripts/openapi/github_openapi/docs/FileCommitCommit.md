# FileCommitCommit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **str** |  | [optional] 
**node_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**author** | [**FileCommitCommitAuthor**](FileCommitCommitAuthor.md) |  | [optional] 
**committer** | [**FileCommitCommitAuthor**](FileCommitCommitAuthor.md) |  | [optional] 
**message** | **str** |  | [optional] 
**tree** | [**FileCommitCommitTree**](FileCommitCommitTree.md) |  | [optional] 
**parents** | [**List[FileCommitCommitParentsInner]**](FileCommitCommitParentsInner.md) |  | [optional] 
**verification** | [**FileCommitCommitVerification**](FileCommitCommitVerification.md) |  | [optional] 

## Example

```python
from github_openapi.models.file_commit_commit import FileCommitCommit

# TODO update the JSON string below
json = "{}"
# create an instance of FileCommitCommit from a JSON string
file_commit_commit_instance = FileCommitCommit.from_json(json)
# print the JSON string representation of the object
print(FileCommitCommit.to_json())

# convert the object into a dict
file_commit_commit_dict = file_commit_commit_instance.to_dict()
# create an instance of FileCommitCommit from a dict
file_commit_commit_from_dict = FileCommitCommit.from_dict(file_commit_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


