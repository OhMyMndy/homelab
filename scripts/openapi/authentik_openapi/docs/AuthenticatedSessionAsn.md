# AuthenticatedSessionAsn

Get ASN Data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **int** |  | 
**as_org** | **str** |  | 
**network** | **str** |  | 

## Example

```python
from authentik_openapi.models.authenticated_session_asn import AuthenticatedSessionAsn

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatedSessionAsn from a JSON string
authenticated_session_asn_instance = AuthenticatedSessionAsn.from_json(json)
# print the JSON string representation of the object
print(AuthenticatedSessionAsn.to_json())

# convert the object into a dict
authenticated_session_asn_dict = authenticated_session_asn_instance.to_dict()
# create an instance of AuthenticatedSessionAsn from a dict
authenticated_session_asn_from_dict = AuthenticatedSessionAsn.from_dict(authenticated_session_asn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


