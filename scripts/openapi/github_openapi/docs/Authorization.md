# Authorization

The authorization for an OAuth app, GitHub App, or a Personal Access Token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**url** | **str** |  | 
**scopes** | **List[str]** | A list of scopes that this authorization is in. | 
**token** | **str** |  | 
**token_last_eight** | **str** |  | 
**hashed_token** | **str** |  | 
**app** | [**AuthorizationApp**](AuthorizationApp.md) |  | 
**note** | **str** |  | 
**note_url** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**fingerprint** | **str** |  | 
**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | [optional] 
**installation** | [**NullableScopedInstallation**](NullableScopedInstallation.md) |  | [optional] 
**expires_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.authorization import Authorization

# TODO update the JSON string below
json = "{}"
# create an instance of Authorization from a JSON string
authorization_instance = Authorization.from_json(json)
# print the JSON string representation of the object
print(Authorization.to_json())

# convert the object into a dict
authorization_dict = authorization_instance.to_dict()
# create an instance of Authorization from a dict
authorization_from_dict = Authorization.from_dict(authorization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


