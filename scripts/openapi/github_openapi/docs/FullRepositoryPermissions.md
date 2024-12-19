# FullRepositoryPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin** | **bool** |  | 
**maintain** | **bool** |  | [optional] 
**push** | **bool** |  | 
**triage** | **bool** |  | [optional] 
**pull** | **bool** |  | 

## Example

```python
from github_openapi.models.full_repository_permissions import FullRepositoryPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of FullRepositoryPermissions from a JSON string
full_repository_permissions_instance = FullRepositoryPermissions.from_json(json)
# print the JSON string representation of the object
print(FullRepositoryPermissions.to_json())

# convert the object into a dict
full_repository_permissions_dict = full_repository_permissions_instance.to_dict()
# create an instance of FullRepositoryPermissions from a dict
full_repository_permissions_from_dict = FullRepositoryPermissions.from_dict(full_repository_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


