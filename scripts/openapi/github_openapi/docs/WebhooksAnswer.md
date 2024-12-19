# WebhooksAnswer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_association** | **str** | How the author is associated with the repository. | 
**body** | **str** |  | 
**child_comment_count** | **int** |  | 
**created_at** | **datetime** |  | 
**discussion_id** | **int** |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**node_id** | **str** |  | 
**parent_id** | **object** |  | 
**reactions** | [**Reactions**](Reactions.md) |  | [optional] 
**repository_url** | **str** |  | 
**updated_at** | **datetime** |  | 
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.webhooks_answer import WebhooksAnswer

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksAnswer from a JSON string
webhooks_answer_instance = WebhooksAnswer.from_json(json)
# print the JSON string representation of the object
print(WebhooksAnswer.to_json())

# convert the object into a dict
webhooks_answer_dict = webhooks_answer_instance.to_dict()
# create an instance of WebhooksAnswer from a dict
webhooks_answer_from_dict = WebhooksAnswer.from_dict(webhooks_answer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


