# AuthenticatedSessionUserAgentOs

User agent os

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family** | **str** |  | 
**major** | **str** |  | 
**minor** | **str** |  | 
**patch** | **str** |  | 
**patch_minor** | **str** |  | 

## Example

```python
from authentik_openapi.models.authenticated_session_user_agent_os import AuthenticatedSessionUserAgentOs

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatedSessionUserAgentOs from a JSON string
authenticated_session_user_agent_os_instance = AuthenticatedSessionUserAgentOs.from_json(json)
# print the JSON string representation of the object
print(AuthenticatedSessionUserAgentOs.to_json())

# convert the object into a dict
authenticated_session_user_agent_os_dict = authenticated_session_user_agent_os_instance.to_dict()
# create an instance of AuthenticatedSessionUserAgentOs from a dict
authenticated_session_user_agent_os_from_dict = AuthenticatedSessionUserAgentOs.from_dict(authenticated_session_user_agent_os_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


