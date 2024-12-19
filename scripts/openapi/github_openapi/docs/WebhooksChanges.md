# WebhooksChanges

The changes to the comment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**WebhooksChangesBody**](WebhooksChangesBody.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhooks_changes import WebhooksChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksChanges from a JSON string
webhooks_changes_instance = WebhooksChanges.from_json(json)
# print the JSON string representation of the object
print(WebhooksChanges.to_json())

# convert the object into a dict
webhooks_changes_dict = webhooks_changes_instance.to_dict()
# create an instance of WebhooksChanges from a dict
webhooks_changes_from_dict = WebhooksChanges.from_dict(webhooks_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


