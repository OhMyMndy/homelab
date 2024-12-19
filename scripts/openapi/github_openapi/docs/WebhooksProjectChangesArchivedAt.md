# WebhooksProjectChangesArchivedAt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** |  | [optional] 
**to** | **datetime** |  | [optional] 

## Example

```python
from github_openapi.models.webhooks_project_changes_archived_at import WebhooksProjectChangesArchivedAt

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksProjectChangesArchivedAt from a JSON string
webhooks_project_changes_archived_at_instance = WebhooksProjectChangesArchivedAt.from_json(json)
# print the JSON string representation of the object
print(WebhooksProjectChangesArchivedAt.to_json())

# convert the object into a dict
webhooks_project_changes_archived_at_dict = webhooks_project_changes_archived_at_instance.to_dict()
# create an instance of WebhooksProjectChangesArchivedAt from a dict
webhooks_project_changes_archived_at_from_dict = WebhooksProjectChangesArchivedAt.from_dict(webhooks_project_changes_archived_at_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


