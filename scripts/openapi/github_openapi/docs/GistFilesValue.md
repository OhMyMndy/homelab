# GistFilesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**raw_url** | **str** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from github_openapi.models.gist_files_value import GistFilesValue

# TODO update the JSON string below
json = "{}"
# create an instance of GistFilesValue from a JSON string
gist_files_value_instance = GistFilesValue.from_json(json)
# print the JSON string representation of the object
print(GistFilesValue.to_json())

# convert the object into a dict
gist_files_value_dict = gist_files_value_instance.to_dict()
# create an instance of GistFilesValue from a dict
gist_files_value_from_dict = GistFilesValue.from_dict(gist_files_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


