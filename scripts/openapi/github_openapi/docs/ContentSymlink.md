# ContentSymlink

An object describing a symlink

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**target** | **str** |  | 
**size** | **int** |  | 
**name** | **str** |  | 
**path** | **str** |  | 
**sha** | **str** |  | 
**url** | **str** |  | 
**git_url** | **str** |  | 
**html_url** | **str** |  | 
**download_url** | **str** |  | 
**links** | [**ContentTreeEntriesInnerLinks**](ContentTreeEntriesInnerLinks.md) |  | 

## Example

```python
from github_openapi.models.content_symlink import ContentSymlink

# TODO update the JSON string below
json = "{}"
# create an instance of ContentSymlink from a JSON string
content_symlink_instance = ContentSymlink.from_json(json)
# print the JSON string representation of the object
print(ContentSymlink.to_json())

# convert the object into a dict
content_symlink_dict = content_symlink_instance.to_dict()
# create an instance of ContentSymlink from a dict
content_symlink_from_dict = ContentSymlink.from_dict(content_symlink_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


