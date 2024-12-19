# WebhooksDeployKey

The [`deploy key`](https://docs.github.com/rest/deploy-keys/deploy-keys#get-a-deploy-key) resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_by** | **str** |  | [optional] 
**created_at** | **str** |  | 
**id** | **int** |  | 
**key** | **str** |  | 
**last_used** | **str** |  | [optional] 
**read_only** | **bool** |  | 
**title** | **str** |  | 
**url** | **str** |  | 
**verified** | **bool** |  | 
**enabled** | **bool** |  | [optional] 

## Example

```python
from github_openapi.models.webhooks_deploy_key import WebhooksDeployKey

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksDeployKey from a JSON string
webhooks_deploy_key_instance = WebhooksDeployKey.from_json(json)
# print the JSON string representation of the object
print(WebhooksDeployKey.to_json())

# convert the object into a dict
webhooks_deploy_key_dict = webhooks_deploy_key_instance.to_dict()
# create an instance of WebhooksDeployKey from a dict
webhooks_deploy_key_from_dict = WebhooksDeployKey.from_dict(webhooks_deploy_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


