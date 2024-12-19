# WebhooksProjectChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived_at** | [**WebhooksProjectChangesArchivedAt**](WebhooksProjectChangesArchivedAt.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhooks_project_changes import WebhooksProjectChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksProjectChanges from a JSON string
webhooks_project_changes_instance = WebhooksProjectChanges.from_json(json)
# print the JSON string representation of the object
print(WebhooksProjectChanges.to_json())

# convert the object into a dict
webhooks_project_changes_dict = webhooks_project_changes_instance.to_dict()
# create an instance of WebhooksProjectChanges from a dict
webhooks_project_changes_from_dict = WebhooksProjectChanges.from_dict(webhooks_project_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


