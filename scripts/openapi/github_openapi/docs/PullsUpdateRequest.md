# PullsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the pull request. | [optional] 
**body** | **str** | The contents of the pull request. | [optional] 
**state** | **str** | State of this Pull Request. Either &#x60;open&#x60; or &#x60;closed&#x60;. | [optional] 
**base** | **str** | The name of the branch you want your changes pulled into. This should be an existing branch on the current repository. You cannot update the base branch on a pull request to point to another repository. | [optional] 
**maintainer_can_modify** | **bool** | Indicates whether [maintainers can modify](https://docs.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/) the pull request. | [optional] 

## Example

```python
from github_openapi.models.pulls_update_request import PullsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PullsUpdateRequest from a JSON string
pulls_update_request_instance = PullsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PullsUpdateRequest.to_json())

# convert the object into a dict
pulls_update_request_dict = pulls_update_request_instance.to_dict()
# create an instance of PullsUpdateRequest from a dict
pulls_update_request_from_dict = PullsUpdateRequest.from_dict(pulls_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


