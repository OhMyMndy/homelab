# MaxFilePathLength

Prevent commits that include file paths that exceed a specified character limit from being pushed to the commit graph.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**parameters** | [**MaxFilePathLengthParameters**](MaxFilePathLengthParameters.md) |  | [optional] 

## Example

```python
from github_openapi.models.max_file_path_length import MaxFilePathLength

# TODO update the JSON string below
json = "{}"
# create an instance of MaxFilePathLength from a JSON string
max_file_path_length_instance = MaxFilePathLength.from_json(json)
# print the JSON string representation of the object
print(MaxFilePathLength.to_json())

# convert the object into a dict
max_file_path_length_dict = max_file_path_length_instance.to_dict()
# create an instance of MaxFilePathLength from a dict
max_file_path_length_from_dict = MaxFilePathLength.from_dict(max_file_path_length_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


