# HookDeliveryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **Dict[str, object]** | The request headers sent with the webhook delivery. | 
**payload** | **Dict[str, object]** | The webhook payload. | 

## Example

```python
from github_openapi.models.hook_delivery_request import HookDeliveryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HookDeliveryRequest from a JSON string
hook_delivery_request_instance = HookDeliveryRequest.from_json(json)
# print the JSON string representation of the object
print(HookDeliveryRequest.to_json())

# convert the object into a dict
hook_delivery_request_dict = hook_delivery_request_instance.to_dict()
# create an instance of HookDeliveryRequest from a dict
hook_delivery_request_from_dict = HookDeliveryRequest.from_dict(hook_delivery_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


