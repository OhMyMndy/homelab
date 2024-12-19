# BaseGistFilesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**raw_url** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**encoding** | **str** | The encoding used for &#x60;content&#x60;. Currently, &#x60;\&quot;utf-8\&quot;&#x60; and &#x60;\&quot;base64\&quot;&#x60; are supported. | [optional] [default to 'utf-8']

## Example

```python
from github_openapi.models.base_gist_files_value import BaseGistFilesValue

# TODO update the JSON string below
json = "{}"
# create an instance of BaseGistFilesValue from a JSON string
base_gist_files_value_instance = BaseGistFilesValue.from_json(json)
# print the JSON string representation of the object
print(BaseGistFilesValue.to_json())

# convert the object into a dict
base_gist_files_value_dict = base_gist_files_value_instance.to_dict()
# create an instance of BaseGistFilesValue from a dict
base_gist_files_value_from_dict = BaseGistFilesValue.from_dict(base_gist_files_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


