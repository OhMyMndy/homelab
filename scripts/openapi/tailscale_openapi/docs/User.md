# User

Representation of a user within a tailnet. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the user. Supply this value wherever {userId} is indicated in an endpoint.  | [optional] 
**display_name** | **str** | The name of the user.  | [optional] 
**login_name** | **str** | The emailish login name of the user.  | [optional] 
**profile_pic_url** | **str** | The profile pic URL for the user.  | [optional] 
**tailnet_id** | **str** | The tailnet that owns the user.  | [optional] 
**created** | **datetime** | The time the user joined their tailnet.  | [optional] 
**type** | **str** | The type of relation this user has to the tailnet associated with the request.  | [optional] 
**role** | **str** | The role of the user. Learn more about [user roles](kb/1138/user-roles).  | [optional] 
**status** | **str** | The status of the user.  | [optional] 
**device_count** | **float** | Number of devices the user owns.  | [optional] 
**last_seen** | **datetime** | The later of either: - The last time any of the user&#39;s nodes were connected to the network. - The last time the user authenticated to any tailscale service, including the admin panel.  | [optional] 
**currently_connected** | **bool** | &#x60;true&#x60; when the user has a node currently connected to the control server.  | [optional] 

## Example

```python
from tailscale_openapi.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


