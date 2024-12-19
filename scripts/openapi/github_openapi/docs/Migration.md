# Migration

A migration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**owner** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**guid** | **str** |  | 
**state** | **str** |  | 
**lock_repositories** | **bool** |  | 
**exclude_metadata** | **bool** |  | 
**exclude_git_data** | **bool** |  | 
**exclude_attachments** | **bool** |  | 
**exclude_releases** | **bool** |  | 
**exclude_owner_projects** | **bool** |  | 
**org_metadata_only** | **bool** |  | 
**repositories** | [**List[Repository]**](Repository.md) | The repositories included in the migration. Only returned for export migrations. | 
**url** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**node_id** | **str** |  | 
**archive_url** | **str** |  | [optional] 
**exclude** | **List[str]** | Exclude related items from being returned in the response in order to improve performance of the request. The array can include any of: &#x60;\&quot;repositories\&quot;&#x60;. | [optional] 

## Example

```python
from github_openapi.models.migration import Migration

# TODO update the JSON string below
json = "{}"
# create an instance of Migration from a JSON string
migration_instance = Migration.from_json(json)
# print the JSON string representation of the object
print(Migration.to_json())

# convert the object into a dict
migration_dict = migration_instance.to_dict()
# create an instance of Migration from a dict
migration_from_dict = Migration.from_dict(migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


