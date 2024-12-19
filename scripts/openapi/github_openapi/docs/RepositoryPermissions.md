# RepositoryPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin** | **bool** |  | 
**maintain** | **bool** |  | [optional] 
**pull** | **bool** |  | 
**push** | **bool** |  | 
**triage** | **bool** |  | [optional] 

## Example

```python
from github_openapi.models.repository_permissions import RepositoryPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryPermissions from a JSON string
repository_permissions_instance = RepositoryPermissions.from_json(json)
# print the JSON string representation of the object
print(RepositoryPermissions.to_json())

# convert the object into a dict
repository_permissions_dict = repository_permissions_instance.to_dict()
# create an instance of RepositoryPermissions from a dict
repository_permissions_from_dict = RepositoryPermissions.from_dict(repository_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


