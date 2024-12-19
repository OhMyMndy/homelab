# WebhookDeploymentReviewRequestedReviewersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reviewer** | [**User6**](User6.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.webhook_deployment_review_requested_reviewers_inner import WebhookDeploymentReviewRequestedReviewersInner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeploymentReviewRequestedReviewersInner from a JSON string
webhook_deployment_review_requested_reviewers_inner_instance = WebhookDeploymentReviewRequestedReviewersInner.from_json(json)
# print the JSON string representation of the object
print(WebhookDeploymentReviewRequestedReviewersInner.to_json())

# convert the object into a dict
webhook_deployment_review_requested_reviewers_inner_dict = webhook_deployment_review_requested_reviewers_inner_instance.to_dict()
# create an instance of WebhookDeploymentReviewRequestedReviewersInner from a dict
webhook_deployment_review_requested_reviewers_inner_from_dict = WebhookDeploymentReviewRequestedReviewersInner.from_dict(webhook_deployment_review_requested_reviewers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


