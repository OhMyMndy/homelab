# ActionsReviewPendingDeploymentsForRunRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_ids** | **List[int]** | The list of environment ids to approve or reject | 
**state** | **str** | Whether to approve or reject deployment to the specified environments. | 
**comment** | **str** | A comment to accompany the deployment review | 

## Example

```python
from github_openapi.models.actions_review_pending_deployments_for_run_request import ActionsReviewPendingDeploymentsForRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsReviewPendingDeploymentsForRunRequest from a JSON string
actions_review_pending_deployments_for_run_request_instance = ActionsReviewPendingDeploymentsForRunRequest.from_json(json)
# print the JSON string representation of the object
print(ActionsReviewPendingDeploymentsForRunRequest.to_json())

# convert the object into a dict
actions_review_pending_deployments_for_run_request_dict = actions_review_pending_deployments_for_run_request_instance.to_dict()
# create an instance of ActionsReviewPendingDeploymentsForRunRequest from a dict
actions_review_pending_deployments_for_run_request_from_dict = ActionsReviewPendingDeploymentsForRunRequest.from_dict(actions_review_pending_deployments_for_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


