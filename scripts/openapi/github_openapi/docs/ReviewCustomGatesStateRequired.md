# ReviewCustomGatesStateRequired


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_name** | **str** | The name of the environment to approve or reject. | 
**state** | **str** | Whether to approve or reject deployment to the specified environments. | 
**comment** | **str** | Optional comment to include with the review. | [optional] 

## Example

```python
from github_openapi.models.review_custom_gates_state_required import ReviewCustomGatesStateRequired

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewCustomGatesStateRequired from a JSON string
review_custom_gates_state_required_instance = ReviewCustomGatesStateRequired.from_json(json)
# print the JSON string representation of the object
print(ReviewCustomGatesStateRequired.to_json())

# convert the object into a dict
review_custom_gates_state_required_dict = review_custom_gates_state_required_instance.to_dict()
# create an instance of ReviewCustomGatesStateRequired from a dict
review_custom_gates_state_required_from_dict = ReviewCustomGatesStateRequired.from_dict(review_custom_gates_state_required_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


