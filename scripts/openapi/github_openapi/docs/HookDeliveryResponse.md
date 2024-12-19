# HookDeliveryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **Dict[str, object]** | The response headers received when the delivery was made. | 
**payload** | **Dict[str, object]** | The response payload received. | 

## Example

```python
from github_openapi.models.hook_delivery_response import HookDeliveryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HookDeliveryResponse from a JSON string
hook_delivery_response_instance = HookDeliveryResponse.from_json(json)
# print the JSON string representation of the object
print(HookDeliveryResponse.to_json())

# convert the object into a dict
hook_delivery_response_dict = hook_delivery_response_instance.to_dict()
# create an instance of HookDeliveryResponse from a dict
hook_delivery_response_from_dict = HookDeliveryResponse.from_dict(hook_delivery_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


