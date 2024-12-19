# MigrationsStartImportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vcs_url** | **str** | The URL of the originating repository. | 
**vcs** | **str** | The originating VCS type. Without this parameter, the import job will take additional time to detect the VCS type before beginning the import. This detection step will be reflected in the response. | [optional] 
**vcs_username** | **str** | If authentication is required, the username to provide to &#x60;vcs_url&#x60;. | [optional] 
**vcs_password** | **str** | If authentication is required, the password to provide to &#x60;vcs_url&#x60;. | [optional] 
**tfvc_project** | **str** | For a tfvc import, the name of the project that is being imported. | [optional] 

## Example

```python
from github_openapi.models.migrations_start_import_request import MigrationsStartImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationsStartImportRequest from a JSON string
migrations_start_import_request_instance = MigrationsStartImportRequest.from_json(json)
# print the JSON string representation of the object
print(MigrationsStartImportRequest.to_json())

# convert the object into a dict
migrations_start_import_request_dict = migrations_start_import_request_instance.to_dict()
# create an instance of MigrationsStartImportRequest from a dict
migrations_start_import_request_from_dict = MigrationsStartImportRequest.from_dict(migrations_start_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


