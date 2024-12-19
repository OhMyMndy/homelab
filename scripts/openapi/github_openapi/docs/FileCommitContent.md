# FileCommitContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**sha** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**git_url** | **str** |  | [optional] 
**download_url** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**links** | [**FileCommitContentLinks**](FileCommitContentLinks.md) |  | [optional] 

## Example

```python
from github_openapi.models.file_commit_content import FileCommitContent

# TODO update the JSON string below
json = "{}"
# create an instance of FileCommitContent from a JSON string
file_commit_content_instance = FileCommitContent.from_json(json)
# print the JSON string representation of the object
print(FileCommitContent.to_json())

# convert the object into a dict
file_commit_content_dict = file_commit_content_instance.to_dict()
# create an instance of FileCommitContent from a dict
file_commit_content_from_dict = FileCommitContent.from_dict(file_commit_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


