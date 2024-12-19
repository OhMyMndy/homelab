# WebhooksLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | 6-character hex code, without the leading #, identifying the color | 
**default** | **bool** |  | 
**description** | **str** |  | 
**id** | **int** |  | 
**name** | **str** | The name of the label. | 
**node_id** | **str** |  | 
**url** | **str** | URL for the label | 

## Example

```python
from github_openapi.models.webhooks_label import WebhooksLabel

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksLabel from a JSON string
webhooks_label_instance = WebhooksLabel.from_json(json)
# print the JSON string representation of the object
print(WebhooksLabel.to_json())

# convert the object into a dict
webhooks_label_dict = webhooks_label_instance.to_dict()
# create an instance of WebhooksLabel from a dict
webhooks_label_from_dict = WebhooksLabel.from_dict(webhooks_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


