# MaxFileSizeParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_file_size** | **int** | The maximum file size allowed in megabytes. This limit does not apply to Git Large File Storage (Git LFS). | 

## Example

```python
from github_openapi.models.max_file_size_parameters import MaxFileSizeParameters

# TODO update the JSON string below
json = "{}"
# create an instance of MaxFileSizeParameters from a JSON string
max_file_size_parameters_instance = MaxFileSizeParameters.from_json(json)
# print the JSON string representation of the object
print(MaxFileSizeParameters.to_json())

# convert the object into a dict
max_file_size_parameters_dict = max_file_size_parameters_instance.to_dict()
# create an instance of MaxFileSizeParameters from a dict
max_file_size_parameters_from_dict = MaxFileSizeParameters.from_dict(max_file_size_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


