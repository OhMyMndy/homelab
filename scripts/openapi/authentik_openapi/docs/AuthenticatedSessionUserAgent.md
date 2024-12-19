# AuthenticatedSessionUserAgent

Get parsed user agent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | [**AuthenticatedSessionUserAgentDevice**](AuthenticatedSessionUserAgentDevice.md) |  | 
**os** | [**AuthenticatedSessionUserAgentOs**](AuthenticatedSessionUserAgentOs.md) |  | 
**user_agent** | [**AuthenticatedSessionUserAgentUserAgent**](AuthenticatedSessionUserAgentUserAgent.md) |  | 
**string** | **str** |  | 

## Example

```python
from authentik_openapi.models.authenticated_session_user_agent import AuthenticatedSessionUserAgent

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatedSessionUserAgent from a JSON string
authenticated_session_user_agent_instance = AuthenticatedSessionUserAgent.from_json(json)
# print the JSON string representation of the object
print(AuthenticatedSessionUserAgent.to_json())

# convert the object into a dict
authenticated_session_user_agent_dict = authenticated_session_user_agent_instance.to_dict()
# create an instance of AuthenticatedSessionUserAgent from a dict
authenticated_session_user_agent_from_dict = AuthenticatedSessionUserAgent.from_dict(authenticated_session_user_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


