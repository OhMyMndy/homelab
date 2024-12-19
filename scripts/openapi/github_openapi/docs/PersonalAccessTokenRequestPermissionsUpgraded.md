# PersonalAccessTokenRequestPermissionsUpgraded

Requested permissions that elevate access for a previously approved request for access, categorized by type of permission.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | **Dict[str, str]** |  | [optional] 
**repository** | **Dict[str, str]** |  | [optional] 
**other** | **Dict[str, str]** |  | [optional] 

## Example

```python
from github_openapi.models.personal_access_token_request_permissions_upgraded import PersonalAccessTokenRequestPermissionsUpgraded

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalAccessTokenRequestPermissionsUpgraded from a JSON string
personal_access_token_request_permissions_upgraded_instance = PersonalAccessTokenRequestPermissionsUpgraded.from_json(json)
# print the JSON string representation of the object
print(PersonalAccessTokenRequestPermissionsUpgraded.to_json())

# convert the object into a dict
personal_access_token_request_permissions_upgraded_dict = personal_access_token_request_permissions_upgraded_instance.to_dict()
# create an instance of PersonalAccessTokenRequestPermissionsUpgraded from a dict
personal_access_token_request_permissions_upgraded_from_dict = PersonalAccessTokenRequestPermissionsUpgraded.from_dict(personal_access_token_request_permissions_upgraded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


