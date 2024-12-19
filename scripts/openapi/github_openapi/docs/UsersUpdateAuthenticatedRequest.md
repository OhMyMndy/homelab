# UsersUpdateAuthenticatedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name of the user. | [optional] 
**email** | **str** | The publicly visible email address of the user. | [optional] 
**blog** | **str** | The new blog URL of the user. | [optional] 
**twitter_username** | **str** | The new Twitter username of the user. | [optional] 
**company** | **str** | The new company of the user. | [optional] 
**location** | **str** | The new location of the user. | [optional] 
**hireable** | **bool** | The new hiring availability of the user. | [optional] 
**bio** | **str** | The new short biography of the user. | [optional] 

## Example

```python
from github_openapi.models.users_update_authenticated_request import UsersUpdateAuthenticatedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUpdateAuthenticatedRequest from a JSON string
users_update_authenticated_request_instance = UsersUpdateAuthenticatedRequest.from_json(json)
# print the JSON string representation of the object
print(UsersUpdateAuthenticatedRequest.to_json())

# convert the object into a dict
users_update_authenticated_request_dict = users_update_authenticated_request_instance.to_dict()
# create an instance of UsersUpdateAuthenticatedRequest from a dict
users_update_authenticated_request_from_dict = UsersUpdateAuthenticatedRequest.from_dict(users_update_authenticated_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


