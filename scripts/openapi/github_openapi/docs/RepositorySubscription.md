# RepositorySubscription

Repository invitations let you manage who you collaborate with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscribed** | **bool** | Determines if notifications should be received from this repository. | 
**ignored** | **bool** | Determines if all notifications should be blocked from this repository. | 
**reason** | **str** |  | 
**created_at** | **datetime** |  | 
**url** | **str** |  | 
**repository_url** | **str** |  | 

## Example

```python
from github_openapi.models.repository_subscription import RepositorySubscription

# TODO update the JSON string below
json = "{}"
# create an instance of RepositorySubscription from a JSON string
repository_subscription_instance = RepositorySubscription.from_json(json)
# print the JSON string representation of the object
print(RepositorySubscription.to_json())

# convert the object into a dict
repository_subscription_dict = repository_subscription_instance.to_dict()
# create an instance of RepositorySubscription from a dict
repository_subscription_from_dict = RepositorySubscription.from_dict(repository_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


