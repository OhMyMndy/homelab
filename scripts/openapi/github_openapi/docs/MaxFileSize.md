# MaxFileSize

Prevent commits that exceed a specified file size limit from being pushed to the commit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**parameters** | [**MaxFileSizeParameters**](MaxFileSizeParameters.md) |  | [optional] 

## Example

```python
from github_openapi.models.max_file_size import MaxFileSize

# TODO update the JSON string below
json = "{}"
# create an instance of MaxFileSize from a JSON string
max_file_size_instance = MaxFileSize.from_json(json)
# print the JSON string representation of the object
print(MaxFileSize.to_json())

# convert the object into a dict
max_file_size_dict = max_file_size_instance.to_dict()
# create an instance of MaxFileSize from a dict
max_file_size_from_dict = MaxFileSize.from_dict(max_file_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


