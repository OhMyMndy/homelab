# AuthenticatedSessionUserAgentDevice

User agent device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand** | **str** |  | 
**family** | **str** |  | 
**model** | **str** |  | 

## Example

```python
from authentik_openapi.models.authenticated_session_user_agent_device import AuthenticatedSessionUserAgentDevice

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatedSessionUserAgentDevice from a JSON string
authenticated_session_user_agent_device_instance = AuthenticatedSessionUserAgentDevice.from_json(json)
# print the JSON string representation of the object
print(AuthenticatedSessionUserAgentDevice.to_json())

# convert the object into a dict
authenticated_session_user_agent_device_dict = authenticated_session_user_agent_device_instance.to_dict()
# create an instance of AuthenticatedSessionUserAgentDevice from a dict
authenticated_session_user_agent_device_from_dict = AuthenticatedSessionUserAgentDevice.from_dict(authenticated_session_user_agent_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


