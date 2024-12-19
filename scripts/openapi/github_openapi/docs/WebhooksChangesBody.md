# WebhooksChangesBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The previous version of the body. | 

## Example

```python
from github_openapi.models.webhooks_changes_body import WebhooksChangesBody

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksChangesBody from a JSON string
webhooks_changes_body_instance = WebhooksChangesBody.from_json(json)
# print the JSON string representation of the object
print(WebhooksChangesBody.to_json())

# convert the object into a dict
webhooks_changes_body_dict = webhooks_changes_body_instance.to_dict()
# create an instance of WebhooksChangesBody from a dict
webhooks_changes_body_from_dict = WebhooksChangesBody.from_dict(webhooks_changes_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


