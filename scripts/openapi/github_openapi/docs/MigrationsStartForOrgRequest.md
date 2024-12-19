# MigrationsStartForOrgRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repositories** | **List[str]** | A list of arrays indicating which repositories should be migrated. | 
**lock_repositories** | **bool** | Indicates whether repositories should be locked (to prevent manipulation) while migrating data. | [optional] [default to False]
**exclude_metadata** | **bool** | Indicates whether metadata should be excluded and only git source should be included for the migration. | [optional] [default to False]
**exclude_git_data** | **bool** | Indicates whether the repository git data should be excluded from the migration. | [optional] [default to False]
**exclude_attachments** | **bool** | Indicates whether attachments should be excluded from the migration (to reduce migration archive file size). | [optional] [default to False]
**exclude_releases** | **bool** | Indicates whether releases should be excluded from the migration (to reduce migration archive file size). | [optional] [default to False]
**exclude_owner_projects** | **bool** | Indicates whether projects owned by the organization or users should be excluded. from the migration. | [optional] [default to False]
**org_metadata_only** | **bool** | Indicates whether this should only include organization metadata (repositories array should be empty and will ignore other flags). | [optional] [default to False]
**exclude** | **List[str]** | Exclude related items from being returned in the response in order to improve performance of the request. | [optional] 

## Example

```python
from github_openapi.models.migrations_start_for_org_request import MigrationsStartForOrgRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationsStartForOrgRequest from a JSON string
migrations_start_for_org_request_instance = MigrationsStartForOrgRequest.from_json(json)
# print the JSON string representation of the object
print(MigrationsStartForOrgRequest.to_json())

# convert the object into a dict
migrations_start_for_org_request_dict = migrations_start_for_org_request_instance.to_dict()
# create an instance of MigrationsStartForOrgRequest from a dict
migrations_start_for_org_request_from_dict = MigrationsStartForOrgRequest.from_dict(migrations_start_for_org_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


