# FileCommitContentLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **str** |  | [optional] 
**git** | **str** |  | [optional] 
**html** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.file_commit_content_links import FileCommitContentLinks

# TODO update the JSON string below
json = "{}"
# create an instance of FileCommitContentLinks from a JSON string
file_commit_content_links_instance = FileCommitContentLinks.from_json(json)
# print the JSON string representation of the object
print(FileCommitContentLinks.to_json())

# convert the object into a dict
file_commit_content_links_dict = file_commit_content_links_instance.to_dict()
# create an instance of FileCommitContentLinks from a dict
file_commit_content_links_from_dict = FileCommitContentLinks.from_dict(file_commit_content_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


