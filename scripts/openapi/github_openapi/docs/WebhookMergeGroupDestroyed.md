# WebhookMergeGroupDestroyed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**reason** | **str** | Explains why the merge group is being destroyed. The group could have been merged, removed from the queue (dequeued), or invalidated by an earlier queue entry being dequeued (invalidated). | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**merge_group** | [**MergeGroup**](MergeGroup.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_merge_group_destroyed import WebhookMergeGroupDestroyed

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMergeGroupDestroyed from a JSON string
webhook_merge_group_destroyed_instance = WebhookMergeGroupDestroyed.from_json(json)
# print the JSON string representation of the object
print(WebhookMergeGroupDestroyed.to_json())

# convert the object into a dict
webhook_merge_group_destroyed_dict = webhook_merge_group_destroyed_instance.to_dict()
# create an instance of WebhookMergeGroupDestroyed from a dict
webhook_merge_group_destroyed_from_dict = WebhookMergeGroupDestroyed.from_dict(webhook_merge_group_destroyed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


