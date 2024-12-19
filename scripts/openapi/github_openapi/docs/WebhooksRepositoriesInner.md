# WebhooksRepositoriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | 
**id** | **int** | Unique identifier of the repository | 
**name** | **str** | The name of the repository. | 
**node_id** | **str** |  | 
**private** | **bool** | Whether the repository is private or public. | 

## Example

```python
from github_openapi.models.webhooks_repositories_inner import WebhooksRepositoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksRepositoriesInner from a JSON string
webhooks_repositories_inner_instance = WebhooksRepositoriesInner.from_json(json)
# print the JSON string representation of the object
print(WebhooksRepositoriesInner.to_json())

# convert the object into a dict
webhooks_repositories_inner_dict = webhooks_repositories_inner_instance.to_dict()
# create an instance of WebhooksRepositoriesInner from a dict
webhooks_repositories_inner_from_dict = WebhooksRepositoriesInner.from_dict(webhooks_repositories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


