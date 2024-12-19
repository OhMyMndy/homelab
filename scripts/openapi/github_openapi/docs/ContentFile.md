# ContentFile

Content File

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**encoding** | **str** |  | 
**size** | **int** |  | 
**name** | **str** |  | 
**path** | **str** |  | 
**content** | **str** |  | 
**sha** | **str** |  | 
**url** | **str** |  | 
**git_url** | **str** |  | 
**html_url** | **str** |  | 
**download_url** | **str** |  | 
**links** | [**ContentTreeEntriesInnerLinks**](ContentTreeEntriesInnerLinks.md) |  | 
**target** | **str** |  | [optional] 
**submodule_git_url** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.content_file import ContentFile

# TODO update the JSON string below
json = "{}"
# create an instance of ContentFile from a JSON string
content_file_instance = ContentFile.from_json(json)
# print the JSON string representation of the object
print(ContentFile.to_json())

# convert the object into a dict
content_file_dict = content_file_instance.to_dict()
# create an instance of ContentFile from a dict
content_file_from_dict = ContentFile.from_dict(content_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


