# ReviewCustomGatesCommentRequired


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_name** | **str** | The name of the environment to approve or reject. | 
**comment** | **str** | Comment associated with the pending deployment protection rule. **Required when state is not provided.** | 

## Example

```python
from github_openapi.models.review_custom_gates_comment_required import ReviewCustomGatesCommentRequired

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewCustomGatesCommentRequired from a JSON string
review_custom_gates_comment_required_instance = ReviewCustomGatesCommentRequired.from_json(json)
# print the JSON string representation of the object
print(ReviewCustomGatesCommentRequired.to_json())

# convert the object into a dict
review_custom_gates_comment_required_dict = review_custom_gates_comment_required_instance.to_dict()
# create an instance of ReviewCustomGatesCommentRequired from a dict
review_custom_gates_comment_required_from_dict = ReviewCustomGatesCommentRequired.from_dict(review_custom_gates_comment_required_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


