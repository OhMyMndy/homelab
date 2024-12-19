# ServiceConnectionState

Serializer for Service connection state

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**healthy** | **bool** |  | [readonly] 
**version** | **str** |  | [readonly] 

## Example

```python
from authentik_openapi.models.service_connection_state import ServiceConnectionState

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceConnectionState from a JSON string
service_connection_state_instance = ServiceConnectionState.from_json(json)
# print the JSON string representation of the object
print(ServiceConnectionState.to_json())

# convert the object into a dict
service_connection_state_dict = service_connection_state_instance.to_dict()
# create an instance of ServiceConnectionState from a dict
service_connection_state_from_dict = ServiceConnectionState.from_dict(service_connection_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


