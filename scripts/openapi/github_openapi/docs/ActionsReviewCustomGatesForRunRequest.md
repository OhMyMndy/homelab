# ActionsReviewCustomGatesForRunRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_name** | **str** | The name of the environment to approve or reject. | 
**comment** | **str** | Optional comment to include with the review. | 
**state** | **str** | Whether to approve or reject deployment to the specified environments. | 

## Example

```python
from github_openapi.models.actions_review_custom_gates_for_run_request import ActionsReviewCustomGatesForRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsReviewCustomGatesForRunRequest from a JSON string
actions_review_custom_gates_for_run_request_instance = ActionsReviewCustomGatesForRunRequest.from_json(json)
# print the JSON string representation of the object
print(ActionsReviewCustomGatesForRunRequest.to_json())

# convert the object into a dict
actions_review_custom_gates_for_run_request_dict = actions_review_custom_gates_for_run_request_instance.to_dict()
# create an instance of ActionsReviewCustomGatesForRunRequest from a dict
actions_review_custom_gates_for_run_request_from_dict = ActionsReviewCustomGatesForRunRequest.from_dict(actions_review_custom_gates_for_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


