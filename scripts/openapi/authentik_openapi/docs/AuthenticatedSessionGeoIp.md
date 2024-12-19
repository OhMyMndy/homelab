# AuthenticatedSessionGeoIp

Get GeoIP Data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continent** | **str** |  | 
**country** | **str** |  | 
**lat** | **float** |  | 
**long** | **float** |  | 
**city** | **str** |  | 

## Example

```python
from authentik_openapi.models.authenticated_session_geo_ip import AuthenticatedSessionGeoIp

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatedSessionGeoIp from a JSON string
authenticated_session_geo_ip_instance = AuthenticatedSessionGeoIp.from_json(json)
# print the JSON string representation of the object
print(AuthenticatedSessionGeoIp.to_json())

# convert the object into a dict
authenticated_session_geo_ip_dict = authenticated_session_geo_ip_instance.to_dict()
# create an instance of AuthenticatedSessionGeoIp from a dict
authenticated_session_geo_ip_from_dict = AuthenticatedSessionGeoIp.from_dict(authenticated_session_geo_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


