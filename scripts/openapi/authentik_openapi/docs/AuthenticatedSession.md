# AuthenticatedSession

AuthenticatedSession Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**current** | **bool** | Check if session is currently active session | [readonly] 
**user_agent** | [**AuthenticatedSessionUserAgent**](AuthenticatedSessionUserAgent.md) |  | 
**geo_ip** | [**AuthenticatedSessionGeoIp**](AuthenticatedSessionGeoIp.md) |  | 
**asn** | [**AuthenticatedSessionAsn**](AuthenticatedSessionAsn.md) |  | 
**user** | **int** |  | 
**last_ip** | **str** |  | 
**last_user_agent** | **str** |  | [optional] 
**last_used** | **datetime** |  | [readonly] 
**expires** | **datetime** |  | [optional] 

## Example

```python
from authentik_openapi.models.authenticated_session import AuthenticatedSession

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatedSession from a JSON string
authenticated_session_instance = AuthenticatedSession.from_json(json)
# print the JSON string representation of the object
print(AuthenticatedSession.to_json())

# convert the object into a dict
authenticated_session_dict = authenticated_session_instance.to_dict()
# create an instance of AuthenticatedSession from a dict
authenticated_session_from_dict = AuthenticatedSession.from_dict(authenticated_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


