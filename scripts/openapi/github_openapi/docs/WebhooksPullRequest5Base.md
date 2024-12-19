# WebhooksPullRequest5Base


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**ref** | **str** |  | 
**repo** | [**Repository**](Repository.md) |  | 
**sha** | **str** |  | 
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.webhooks_pull_request5_base import WebhooksPullRequest5Base

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksPullRequest5Base from a JSON string
webhooks_pull_request5_base_instance = WebhooksPullRequest5Base.from_json(json)
# print the JSON string representation of the object
print(WebhooksPullRequest5Base.to_json())

# convert the object into a dict
webhooks_pull_request5_base_dict = webhooks_pull_request5_base_instance.to_dict()
# create an instance of WebhooksPullRequest5Base from a dict
webhooks_pull_request5_base_from_dict = WebhooksPullRequest5Base.from_dict(webhooks_pull_request5_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


