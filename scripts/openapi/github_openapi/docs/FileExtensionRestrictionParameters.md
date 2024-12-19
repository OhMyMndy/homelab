# FileExtensionRestrictionParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restricted_file_extensions** | **List[str]** | The file extensions that are restricted from being pushed to the commit graph. | 

## Example

```python
from github_openapi.models.file_extension_restriction_parameters import FileExtensionRestrictionParameters

# TODO update the JSON string below
json = "{}"
# create an instance of FileExtensionRestrictionParameters from a JSON string
file_extension_restriction_parameters_instance = FileExtensionRestrictionParameters.from_json(json)
# print the JSON string representation of the object
print(FileExtensionRestrictionParameters.to_json())

# convert the object into a dict
file_extension_restriction_parameters_dict = file_extension_restriction_parameters_instance.to_dict()
# create an instance of FileExtensionRestrictionParameters from a dict
file_extension_restriction_parameters_from_dict = FileExtensionRestrictionParameters.from_dict(file_extension_restriction_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


