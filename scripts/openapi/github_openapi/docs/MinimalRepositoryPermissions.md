# MinimalRepositoryPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin** | **bool** |  | [optional] 
**maintain** | **bool** |  | [optional] 
**push** | **bool** |  | [optional] 
**triage** | **bool** |  | [optional] 
**pull** | **bool** |  | [optional] 

## Example

```python
from github_openapi.models.minimal_repository_permissions import MinimalRepositoryPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of MinimalRepositoryPermissions from a JSON string
minimal_repository_permissions_instance = MinimalRepositoryPermissions.from_json(json)
# print the JSON string representation of the object
print(MinimalRepositoryPermissions.to_json())

# convert the object into a dict
minimal_repository_permissions_dict = minimal_repository_permissions_instance.to_dict()
# create an instance of MinimalRepositoryPermissions from a dict
minimal_repository_permissions_from_dict = MinimalRepositoryPermissions.from_dict(minimal_repository_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


