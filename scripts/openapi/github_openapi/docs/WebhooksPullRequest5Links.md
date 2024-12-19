# WebhooksPullRequest5Links


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | [**Link**](Link.md) |  | 
**commits** | [**Link**](Link.md) |  | 
**html** | [**Link**](Link.md) |  | 
**issue** | [**Link**](Link.md) |  | 
**review_comment** | [**Link**](Link.md) |  | 
**review_comments** | [**Link**](Link.md) |  | 
**var_self** | [**Link**](Link.md) |  | 
**statuses** | [**Link**](Link.md) |  | 

## Example

```python
from github_openapi.models.webhooks_pull_request5_links import WebhooksPullRequest5Links

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksPullRequest5Links from a JSON string
webhooks_pull_request5_links_instance = WebhooksPullRequest5Links.from_json(json)
# print the JSON string representation of the object
print(WebhooksPullRequest5Links.to_json())

# convert the object into a dict
webhooks_pull_request5_links_dict = webhooks_pull_request5_links_instance.to_dict()
# create an instance of WebhooksPullRequest5Links from a dict
webhooks_pull_request5_links_from_dict = WebhooksPullRequest5Links.from_dict(webhooks_pull_request5_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


