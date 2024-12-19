# MigrationsUpdateImportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vcs_username** | **str** | The username to provide to the originating repository. | [optional] 
**vcs_password** | **str** | The password to provide to the originating repository. | [optional] 
**vcs** | **str** | The type of version control system you are migrating from. | [optional] 
**tfvc_project** | **str** | For a tfvc import, the name of the project that is being imported. | [optional] 

## Example

```python
from github_openapi.models.migrations_update_import_request import MigrationsUpdateImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationsUpdateImportRequest from a JSON string
migrations_update_import_request_instance = MigrationsUpdateImportRequest.from_json(json)
# print the JSON string representation of the object
print(MigrationsUpdateImportRequest.to_json())

# convert the object into a dict
migrations_update_import_request_dict = migrations_update_import_request_instance.to_dict()
# create an instance of MigrationsUpdateImportRequest from a dict
migrations_update_import_request_from_dict = MigrationsUpdateImportRequest.from_dict(migrations_update_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


