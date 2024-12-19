# GistSimpleFilesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**raw_url** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**truncated** | **bool** |  | [optional] 
**content** | **str** |  | [optional] 
**encoding** | **str** | The encoding used for &#x60;content&#x60;. Currently, &#x60;\&quot;utf-8\&quot;&#x60; and &#x60;\&quot;base64\&quot;&#x60; are supported. | [optional] [default to 'utf-8']

## Example

```python
from github_openapi.models.gist_simple_files_value import GistSimpleFilesValue

# TODO update the JSON string below
json = "{}"
# create an instance of GistSimpleFilesValue from a JSON string
gist_simple_files_value_instance = GistSimpleFilesValue.from_json(json)
# print the JSON string representation of the object
print(GistSimpleFilesValue.to_json())

# convert the object into a dict
gist_simple_files_value_dict = gist_simple_files_value_instance.to_dict()
# create an instance of GistSimpleFilesValue from a dict
gist_simple_files_value_from_dict = GistSimpleFilesValue.from_dict(gist_simple_files_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


