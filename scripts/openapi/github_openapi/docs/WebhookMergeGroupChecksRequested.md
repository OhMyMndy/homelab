# WebhookMergeGroupChecksRequested


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**merge_group** | [**MergeGroup**](MergeGroup.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_merge_group_checks_requested import WebhookMergeGroupChecksRequested

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMergeGroupChecksRequested from a JSON string
webhook_merge_group_checks_requested_instance = WebhookMergeGroupChecksRequested.from_json(json)
# print the JSON string representation of the object
print(WebhookMergeGroupChecksRequested.to_json())

# convert the object into a dict
webhook_merge_group_checks_requested_dict = webhook_merge_group_checks_requested_instance.to_dict()
# create an instance of WebhookMergeGroupChecksRequested from a dict
webhook_merge_group_checks_requested_from_dict = WebhookMergeGroupChecksRequested.from_dict(webhook_merge_group_checks_requested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


