# PendingDeploymentReviewersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DeploymentReviewerType**](DeploymentReviewerType.md) |  | [optional] 
**reviewer** | [**PendingDeploymentReviewersInnerReviewer**](PendingDeploymentReviewersInnerReviewer.md) |  | [optional] 

## Example

```python
from github_openapi.models.pending_deployment_reviewers_inner import PendingDeploymentReviewersInner

# TODO update the JSON string below
json = "{}"
# create an instance of PendingDeploymentReviewersInner from a JSON string
pending_deployment_reviewers_inner_instance = PendingDeploymentReviewersInner.from_json(json)
# print the JSON string representation of the object
print(PendingDeploymentReviewersInner.to_json())

# convert the object into a dict
pending_deployment_reviewers_inner_dict = pending_deployment_reviewers_inner_instance.to_dict()
# create an instance of PendingDeploymentReviewersInner from a dict
pending_deployment_reviewers_inner_from_dict = PendingDeploymentReviewersInner.from_dict(pending_deployment_reviewers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


