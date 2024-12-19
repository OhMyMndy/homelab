# NullableScopedInstallation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**AppPermissions**](AppPermissions.md) |  | 
**repository_selection** | **str** | Describe whether all repositories have been selected or there&#39;s a selection involved | 
**single_file_name** | **str** |  | 
**has_multiple_single_files** | **bool** |  | [optional] 
**single_file_paths** | **List[str]** |  | [optional] 
**repositories_url** | **str** |  | 
**account** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.nullable_scoped_installation import NullableScopedInstallation

# TODO update the JSON string below
json = "{}"
# create an instance of NullableScopedInstallation from a JSON string
nullable_scoped_installation_instance = NullableScopedInstallation.from_json(json)
# print the JSON string representation of the object
print(NullableScopedInstallation.to_json())

# convert the object into a dict
nullable_scoped_installation_dict = nullable_scoped_installation_instance.to_dict()
# create an instance of NullableScopedInstallation from a dict
nullable_scoped_installation_from_dict = NullableScopedInstallation.from_dict(nullable_scoped_installation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


