# WebhooksReviewersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reviewer** | [**User**](User.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.webhooks_reviewers_inner import WebhooksReviewersInner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksReviewersInner from a JSON string
webhooks_reviewers_inner_instance = WebhooksReviewersInner.from_json(json)
# print the JSON string representation of the object
print(WebhooksReviewersInner.to_json())

# convert the object into a dict
webhooks_reviewers_inner_dict = webhooks_reviewers_inner_instance.to_dict()
# create an instance of WebhooksReviewersInner from a dict
webhooks_reviewers_inner_from_dict = WebhooksReviewersInner.from_dict(webhooks_reviewers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


