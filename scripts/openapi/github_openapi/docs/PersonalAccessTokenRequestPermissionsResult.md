# PersonalAccessTokenRequestPermissionsResult

Permissions requested, categorized by type of permission. This field incorporates `permissions_added` and `permissions_upgraded`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | **Dict[str, str]** |  | [optional] 
**repository** | **Dict[str, str]** |  | [optional] 
**other** | **Dict[str, str]** |  | [optional] 

## Example

```python
from github_openapi.models.personal_access_token_request_permissions_result import PersonalAccessTokenRequestPermissionsResult

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalAccessTokenRequestPermissionsResult from a JSON string
personal_access_token_request_permissions_result_instance = PersonalAccessTokenRequestPermissionsResult.from_json(json)
# print the JSON string representation of the object
print(PersonalAccessTokenRequestPermissionsResult.to_json())

# convert the object into a dict
personal_access_token_request_permissions_result_dict = personal_access_token_request_permissions_result_instance.to_dict()
# create an instance of PersonalAccessTokenRequestPermissionsResult from a dict
personal_access_token_request_permissions_result_from_dict = PersonalAccessTokenRequestPermissionsResult.from_dict(personal_access_token_request_permissions_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


