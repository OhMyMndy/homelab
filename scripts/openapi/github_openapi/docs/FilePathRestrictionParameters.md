# FilePathRestrictionParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restricted_file_paths** | **List[str]** | The file paths that are restricted from being pushed to the commit graph. | 

## Example

```python
from github_openapi.models.file_path_restriction_parameters import FilePathRestrictionParameters

# TODO update the JSON string below
json = "{}"
# create an instance of FilePathRestrictionParameters from a JSON string
file_path_restriction_parameters_instance = FilePathRestrictionParameters.from_json(json)
# print the JSON string representation of the object
print(FilePathRestrictionParameters.to_json())

# convert the object into a dict
file_path_restriction_parameters_dict = file_path_restriction_parameters_instance.to_dict()
# create an instance of FilePathRestrictionParameters from a dict
file_path_restriction_parameters_from_dict = FilePathRestrictionParameters.from_dict(file_path_restriction_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


