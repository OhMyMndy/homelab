# ActivitySetThreadSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignored** | **bool** | Whether to block all notifications from a thread. | [optional] [default to False]

## Example

```python
from github_openapi.models.activity_set_thread_subscription_request import ActivitySetThreadSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivitySetThreadSubscriptionRequest from a JSON string
activity_set_thread_subscription_request_instance = ActivitySetThreadSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(ActivitySetThreadSubscriptionRequest.to_json())

# convert the object into a dict
activity_set_thread_subscription_request_dict = activity_set_thread_subscription_request_instance.to_dict()
# create an instance of ActivitySetThreadSubscriptionRequest from a dict
activity_set_thread_subscription_request_from_dict = ActivitySetThreadSubscriptionRequest.from_dict(activity_set_thread_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


