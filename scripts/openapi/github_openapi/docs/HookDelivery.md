# HookDelivery

Delivery made by a webhook.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the delivery. | 
**guid** | **str** | Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event). | 
**delivered_at** | **datetime** | Time when the delivery was delivered. | 
**redelivery** | **bool** | Whether the delivery is a redelivery. | 
**duration** | **float** | Time spent delivering. | 
**status** | **str** | Description of the status of the attempted delivery | 
**status_code** | **int** | Status code received when delivery was made. | 
**event** | **str** | The event that triggered the delivery. | 
**action** | **str** | The type of activity for the event that triggered the delivery. | 
**installation_id** | **int** | The id of the GitHub App installation associated with this event. | 
**repository_id** | **int** | The id of the repository associated with this event. | 
**throttled_at** | **datetime** | Time when the webhook delivery was throttled. | [optional] 
**url** | **str** | The URL target of the delivery. | [optional] 
**request** | [**HookDeliveryRequest**](HookDeliveryRequest.md) |  | 
**response** | [**HookDeliveryResponse**](HookDeliveryResponse.md) |  | 

## Example

```python
from github_openapi.models.hook_delivery import HookDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of HookDelivery from a JSON string
hook_delivery_instance = HookDelivery.from_json(json)
# print the JSON string representation of the object
print(HookDelivery.to_json())

# convert the object into a dict
hook_delivery_dict = hook_delivery_instance.to_dict()
# create an instance of HookDelivery from a dict
hook_delivery_from_dict = HookDelivery.from_dict(hook_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


