# WebhooksReview

The review that was affected.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**WebhooksReviewLinks**](WebhooksReviewLinks.md) |  | 
**author_association** | **str** | How the author is associated with the repository. | 
**body** | **str** | The text of the review. | 
**commit_id** | **str** | A commit SHA for the review. | 
**html_url** | **str** |  | 
**id** | **int** | Unique identifier of the review | 
**node_id** | **str** |  | 
**pull_request_url** | **str** |  | 
**state** | **str** |  | 
**submitted_at** | **datetime** |  | 
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.webhooks_review import WebhooksReview

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksReview from a JSON string
webhooks_review_instance = WebhooksReview.from_json(json)
# print the JSON string representation of the object
print(WebhooksReview.to_json())

# convert the object into a dict
webhooks_review_dict = webhooks_review_instance.to_dict()
# create an instance of WebhooksReview from a dict
webhooks_review_from_dict = WebhooksReview.from_dict(webhooks_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


