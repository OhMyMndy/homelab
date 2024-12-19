# GistsUpdateRequestFilesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | The new content of the file. | [optional] 
**filename** | **str** | The new filename for the file. | [optional] 

## Example

```python
from github_openapi.models.gists_update_request_files_value import GistsUpdateRequestFilesValue

# TODO update the JSON string below
json = "{}"
# create an instance of GistsUpdateRequestFilesValue from a JSON string
gists_update_request_files_value_instance = GistsUpdateRequestFilesValue.from_json(json)
# print the JSON string representation of the object
print(GistsUpdateRequestFilesValue.to_json())

# convert the object into a dict
gists_update_request_files_value_dict = gists_update_request_files_value_instance.to_dict()
# create an instance of GistsUpdateRequestFilesValue from a dict
gists_update_request_files_value_from_dict = GistsUpdateRequestFilesValue.from_dict(gists_update_request_files_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


