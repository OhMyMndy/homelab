# FileCommitCommitParentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**sha** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.file_commit_commit_parents_inner import FileCommitCommitParentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FileCommitCommitParentsInner from a JSON string
file_commit_commit_parents_inner_instance = FileCommitCommitParentsInner.from_json(json)
# print the JSON string representation of the object
print(FileCommitCommitParentsInner.to_json())

# convert the object into a dict
file_commit_commit_parents_inner_dict = file_commit_commit_parents_inner_instance.to_dict()
# create an instance of FileCommitCommitParentsInner from a dict
file_commit_commit_parents_inner_from_dict = FileCommitCommitParentsInner.from_dict(file_commit_commit_parents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


