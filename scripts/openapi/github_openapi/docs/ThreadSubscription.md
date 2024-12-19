# ThreadSubscription

Thread Subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscribed** | **bool** |  | 
**ignored** | **bool** |  | 
**reason** | **str** |  | 
**created_at** | **datetime** |  | 
**url** | **str** |  | 
**thread_url** | **str** |  | [optional] 
**repository_url** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.thread_subscription import ThreadSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadSubscription from a JSON string
thread_subscription_instance = ThreadSubscription.from_json(json)
# print the JSON string representation of the object
print(ThreadSubscription.to_json())

# convert the object into a dict
thread_subscription_dict = thread_subscription_instance.to_dict()
# create an instance of ThreadSubscription from a dict
thread_subscription_from_dict = ThreadSubscription.from_dict(thread_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


