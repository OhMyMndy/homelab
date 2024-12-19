# AuthorizationApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**name** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.authorization_app import AuthorizationApp

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationApp from a JSON string
authorization_app_instance = AuthorizationApp.from_json(json)
# print the JSON string representation of the object
print(AuthorizationApp.to_json())

# convert the object into a dict
authorization_app_dict = authorization_app_instance.to_dict()
# create an instance of AuthorizationApp from a dict
authorization_app_from_dict = AuthorizationApp.from_dict(authorization_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


