# WebhooksComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_association** | **str** | How the author is associated with the repository. | 
**body** | **str** |  | 
**child_comment_count** | **int** |  | 
**created_at** | **str** |  | 
**discussion_id** | **int** |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**node_id** | **str** |  | 
**parent_id** | **int** |  | 
**reactions** | [**Reactions**](Reactions.md) |  | 
**repository_url** | **str** |  | 
**updated_at** | **str** |  | 
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.webhooks_comment import WebhooksComment

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksComment from a JSON string
webhooks_comment_instance = WebhooksComment.from_json(json)
# print the JSON string representation of the object
print(WebhooksComment.to_json())

# convert the object into a dict
webhooks_comment_dict = webhooks_comment_instance.to_dict()
# create an instance of WebhooksComment from a dict
webhooks_comment_from_dict = WebhooksComment.from_dict(webhooks_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


