# FilePathRestriction

Prevent commits that include changes in specified file paths from being pushed to the commit graph.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**parameters** | [**FilePathRestrictionParameters**](FilePathRestrictionParameters.md) |  | [optional] 

## Example

```python
from github_openapi.models.file_path_restriction import FilePathRestriction

# TODO update the JSON string below
json = "{}"
# create an instance of FilePathRestriction from a JSON string
file_path_restriction_instance = FilePathRestriction.from_json(json)
# print the JSON string representation of the object
print(FilePathRestriction.to_json())

# convert the object into a dict
file_path_restriction_dict = file_path_restriction_instance.to_dict()
# create an instance of FilePathRestriction from a dict
file_path_restriction_from_dict = FilePathRestriction.from_dict(file_path_restriction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


