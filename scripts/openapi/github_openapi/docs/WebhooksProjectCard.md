# WebhooksProjectCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after_id** | **int** |  | [optional] 
**archived** | **bool** | Whether or not the card is archived | 
**column_id** | **int** |  | 
**column_url** | **str** |  | 
**content_url** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**creator** | [**User2**](User2.md) |  | 
**id** | **int** | The project card&#39;s ID | 
**node_id** | **str** |  | 
**note** | **str** |  | 
**project_url** | **str** |  | 
**updated_at** | **datetime** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.webhooks_project_card import WebhooksProjectCard

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksProjectCard from a JSON string
webhooks_project_card_instance = WebhooksProjectCard.from_json(json)
# print the JSON string representation of the object
print(WebhooksProjectCard.to_json())

# convert the object into a dict
webhooks_project_card_dict = webhooks_project_card_instance.to_dict()
# create an instance of WebhooksProjectCard from a dict
webhooks_project_card_from_dict = WebhooksProjectCard.from_dict(webhooks_project_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


