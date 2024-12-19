# FileExtensionRestriction

Prevent commits that include files with specified file extensions from being pushed to the commit graph.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**parameters** | [**FileExtensionRestrictionParameters**](FileExtensionRestrictionParameters.md) |  | [optional] 

## Example

```python
from github_openapi.models.file_extension_restriction import FileExtensionRestriction

# TODO update the JSON string below
json = "{}"
# create an instance of FileExtensionRestriction from a JSON string
file_extension_restriction_instance = FileExtensionRestriction.from_json(json)
# print the JSON string representation of the object
print(FileExtensionRestriction.to_json())

# convert the object into a dict
file_extension_restriction_dict = file_extension_restriction_instance.to_dict()
# create an instance of FileExtensionRestriction from a dict
file_extension_restriction_from_dict = FileExtensionRestriction.from_dict(file_extension_restriction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


