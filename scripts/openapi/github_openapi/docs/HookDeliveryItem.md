# HookDeliveryItem

Delivery made by a webhook, without request and response information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the webhook delivery. | 
**guid** | **str** | Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event). | 
**delivered_at** | **datetime** | Time when the webhook delivery occurred. | 
**redelivery** | **bool** | Whether the webhook delivery is a redelivery. | 
**duration** | **float** | Time spent delivering. | 
**status** | **str** | Describes the response returned after attempting the delivery. | 
**status_code** | **int** | Status code received when delivery was made. | 
**event** | **str** | The event that triggered the delivery. | 
**action** | **str** | The type of activity for the event that triggered the delivery. | 
**installation_id** | **int** | The id of the GitHub App installation associated with this event. | 
**repository_id** | **int** | The id of the repository associated with this event. | 
**throttled_at** | **datetime** | Time when the webhook delivery was throttled. | [optional] 

## Example

```python
from github_openapi.models.hook_delivery_item import HookDeliveryItem

# TODO update the JSON string below
json = "{}"
# create an instance of HookDeliveryItem from a JSON string
hook_delivery_item_instance = HookDeliveryItem.from_json(json)
# print the JSON string representation of the object
print(HookDeliveryItem.to_json())

# convert the object into a dict
hook_delivery_item_dict = hook_delivery_item_instance.to_dict()
# create an instance of HookDeliveryItem from a dict
hook_delivery_item_from_dict = HookDeliveryItem.from_dict(hook_delivery_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


