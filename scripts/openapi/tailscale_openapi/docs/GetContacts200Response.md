# GetContacts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**Contact**](Contact.md) |  | [optional] 
**support** | [**Contact**](Contact.md) |  | [optional] 
**security** | [**Contact**](Contact.md) |  | [optional] 

## Example

```python
from tailscale_openapi.models.get_contacts200_response import GetContacts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetContacts200Response from a JSON string
get_contacts200_response_instance = GetContacts200Response.from_json(json)
# print the JSON string representation of the object
print(GetContacts200Response.to_json())

# convert the object into a dict
get_contacts200_response_dict = get_contacts200_response_instance.to_dict()
# create an instance of GetContacts200Response from a dict
get_contacts200_response_from_dict = GetContacts200Response.from_dict(get_contacts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


