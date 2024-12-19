# AuthenticatedSessionUserAgentUserAgent

User agent browser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family** | **str** |  | 
**major** | **str** |  | 
**minor** | **str** |  | 
**patch** | **str** |  | 

## Example

```python
from authentik_openapi.models.authenticated_session_user_agent_user_agent import AuthenticatedSessionUserAgentUserAgent

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatedSessionUserAgentUserAgent from a JSON string
authenticated_session_user_agent_user_agent_instance = AuthenticatedSessionUserAgentUserAgent.from_json(json)
# print the JSON string representation of the object
print(AuthenticatedSessionUserAgentUserAgent.to_json())

# convert the object into a dict
authenticated_session_user_agent_user_agent_dict = authenticated_session_user_agent_user_agent_instance.to_dict()
# create an instance of AuthenticatedSessionUserAgentUserAgent from a dict
authenticated_session_user_agent_user_agent_from_dict = AuthenticatedSessionUserAgentUserAgent.from_dict(authenticated_session_user_agent_user_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


