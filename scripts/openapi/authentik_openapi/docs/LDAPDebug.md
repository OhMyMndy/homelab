# LDAPDebug


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **List[Dict[str, object]]** |  | [readonly] 
**group** | **List[Dict[str, object]]** |  | [readonly] 
**membership** | **List[Dict[str, object]]** |  | [readonly] 

## Example

```python
from authentik_openapi.models.ldap_debug import LDAPDebug

# TODO update the JSON string below
json = "{}"
# create an instance of LDAPDebug from a JSON string
ldap_debug_instance = LDAPDebug.from_json(json)
# print the JSON string representation of the object
print(LDAPDebug.to_json())

# convert the object into a dict
ldap_debug_dict = ldap_debug_instance.to_dict()
# create an instance of LDAPDebug from a dict
ldap_debug_from_dict = LDAPDebug.from_dict(ldap_debug_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


