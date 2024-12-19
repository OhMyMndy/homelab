# MigrationsStartForAuthenticatedUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lock_repositories** | **bool** | Lock the repositories being migrated at the start of the migration | [optional] 
**exclude_metadata** | **bool** | Indicates whether metadata should be excluded and only git source should be included for the migration. | [optional] 
**exclude_git_data** | **bool** | Indicates whether the repository git data should be excluded from the migration. | [optional] 
**exclude_attachments** | **bool** | Do not include attachments in the migration | [optional] 
**exclude_releases** | **bool** | Do not include releases in the migration | [optional] 
**exclude_owner_projects** | **bool** | Indicates whether projects owned by the organization or users should be excluded. | [optional] 
**org_metadata_only** | **bool** | Indicates whether this should only include organization metadata (repositories array should be empty and will ignore other flags). | [optional] [default to False]
**exclude** | **List[str]** | Exclude attributes from the API response to improve performance | [optional] 
**repositories** | **List[str]** |  | 

## Example

```python
from github_openapi.models.migrations_start_for_authenticated_user_request import MigrationsStartForAuthenticatedUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationsStartForAuthenticatedUserRequest from a JSON string
migrations_start_for_authenticated_user_request_instance = MigrationsStartForAuthenticatedUserRequest.from_json(json)
# print the JSON string representation of the object
print(MigrationsStartForAuthenticatedUserRequest.to_json())

# convert the object into a dict
migrations_start_for_authenticated_user_request_dict = migrations_start_for_authenticated_user_request_instance.to_dict()
# create an instance of MigrationsStartForAuthenticatedUserRequest from a dict
migrations_start_for_authenticated_user_request_from_dict = MigrationsStartForAuthenticatedUserRequest.from_dict(migrations_start_for_authenticated_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


