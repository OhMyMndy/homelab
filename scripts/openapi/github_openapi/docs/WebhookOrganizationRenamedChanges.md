# WebhookOrganizationRenamedChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | [**WebhookOrganizationRenamedChangesLogin**](WebhookOrganizationRenamedChangesLogin.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_organization_renamed_changes import WebhookOrganizationRenamedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookOrganizationRenamedChanges from a JSON string
webhook_organization_renamed_changes_instance = WebhookOrganizationRenamedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookOrganizationRenamedChanges.to_json())

# convert the object into a dict
webhook_organization_renamed_changes_dict = webhook_organization_renamed_changes_instance.to_dict()
# create an instance of WebhookOrganizationRenamedChanges from a dict
webhook_organization_renamed_changes_from_dict = WebhookOrganizationRenamedChanges.from_dict(webhook_organization_renamed_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


