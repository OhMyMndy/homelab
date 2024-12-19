# WebhookReleaseEdited


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookReleaseEditedChanges**](WebhookReleaseEditedChanges.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**release** | [**WebhooksRelease**](WebhooksRelease.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_release_edited import WebhookReleaseEdited

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookReleaseEdited from a JSON string
webhook_release_edited_instance = WebhookReleaseEdited.from_json(json)
# print the JSON string representation of the object
print(WebhookReleaseEdited.to_json())

# convert the object into a dict
webhook_release_edited_dict = webhook_release_edited_instance.to_dict()
# create an instance of WebhookReleaseEdited from a dict
webhook_release_edited_from_dict = WebhookReleaseEdited.from_dict(webhook_release_edited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


