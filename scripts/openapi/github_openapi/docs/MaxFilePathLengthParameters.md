# MaxFilePathLengthParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_file_path_length** | **int** | The maximum amount of characters allowed in file paths | 

## Example

```python
from github_openapi.models.max_file_path_length_parameters import MaxFilePathLengthParameters

# TODO update the JSON string below
json = "{}"
# create an instance of MaxFilePathLengthParameters from a JSON string
max_file_path_length_parameters_instance = MaxFilePathLengthParameters.from_json(json)
# print the JSON string representation of the object
print(MaxFilePathLengthParameters.to_json())

# convert the object into a dict
max_file_path_length_parameters_dict = max_file_path_length_parameters_instance.to_dict()
# create an instance of MaxFilePathLengthParameters from a dict
max_file_path_length_parameters_from_dict = MaxFilePathLengthParameters.from_dict(max_file_path_length_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


