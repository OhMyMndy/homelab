# PersonalAccessTokenRequestPermissionsAdded

New requested permissions, categorized by type of permission.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | **Dict[str, str]** |  | [optional] 
**repository** | **Dict[str, str]** |  | [optional] 
**other** | **Dict[str, str]** |  | [optional] 

## Example

```python
from github_openapi.models.personal_access_token_request_permissions_added import PersonalAccessTokenRequestPermissionsAdded

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalAccessTokenRequestPermissionsAdded from a JSON string
personal_access_token_request_permissions_added_instance = PersonalAccessTokenRequestPermissionsAdded.from_json(json)
# print the JSON string representation of the object
print(PersonalAccessTokenRequestPermissionsAdded.to_json())

# convert the object into a dict
personal_access_token_request_permissions_added_dict = personal_access_token_request_permissions_added_instance.to_dict()
# create an instance of PersonalAccessTokenRequestPermissionsAdded from a dict
personal_access_token_request_permissions_added_from_dict = PersonalAccessTokenRequestPermissionsAdded.from_dict(personal_access_token_request_permissions_added_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


