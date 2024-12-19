# WebhookRegistryPackagePublishedRegistryPackageOwner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_url** | **str** |  | 
**events_url** | **str** |  | 
**followers_url** | **str** |  | 
**following_url** | **str** |  | 
**gists_url** | **str** |  | 
**gravatar_id** | **str** |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**login** | **str** |  | 
**node_id** | **str** |  | 
**organizations_url** | **str** |  | 
**received_events_url** | **str** |  | 
**repos_url** | **str** |  | 
**site_admin** | **bool** |  | 
**starred_url** | **str** |  | 
**subscriptions_url** | **str** |  | 
**type** | **str** |  | 
**url** | **str** |  | 
**user_view_type** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.webhook_registry_package_published_registry_package_owner import WebhookRegistryPackagePublishedRegistryPackageOwner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRegistryPackagePublishedRegistryPackageOwner from a JSON string
webhook_registry_package_published_registry_package_owner_instance = WebhookRegistryPackagePublishedRegistryPackageOwner.from_json(json)
# print the JSON string representation of the object
print(WebhookRegistryPackagePublishedRegistryPackageOwner.to_json())

# convert the object into a dict
webhook_registry_package_published_registry_package_owner_dict = webhook_registry_package_published_registry_package_owner_instance.to_dict()
# create an instance of WebhookRegistryPackagePublishedRegistryPackageOwner from a dict
webhook_registry_package_published_registry_package_owner_from_dict = WebhookRegistryPackagePublishedRegistryPackageOwner.from_dict(webhook_registry_package_published_registry_package_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


