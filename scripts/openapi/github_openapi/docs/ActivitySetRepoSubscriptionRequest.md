# ActivitySetRepoSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscribed** | **bool** | Determines if notifications should be received from this repository. | [optional] 
**ignored** | **bool** | Determines if all notifications should be blocked from this repository. | [optional] 

## Example

```python
from github_openapi.models.activity_set_repo_subscription_request import ActivitySetRepoSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivitySetRepoSubscriptionRequest from a JSON string
activity_set_repo_subscription_request_instance = ActivitySetRepoSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(ActivitySetRepoSubscriptionRequest.to_json())

# convert the object into a dict
activity_set_repo_subscription_request_dict = activity_set_repo_subscription_request_instance.to_dict()
# create an instance of ActivitySetRepoSubscriptionRequest from a dict
activity_set_repo_subscription_request_from_dict = ActivitySetRepoSubscriptionRequest.from_dict(activity_set_repo_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


