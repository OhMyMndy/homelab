# ReposCreateCommitStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state of the status. | 
**target_url** | **str** | The target URL to associate with this status. This URL will be linked from the GitHub UI to allow users to easily see the source of the status.   For example, if your continuous integration system is posting build status, you would want to provide the deep link for the build output for this specific SHA:   &#x60;http://ci.example.com/user/repo/build/sha&#x60; | [optional] 
**description** | **str** | A short description of the status. | [optional] 
**context** | **str** | A string label to differentiate this status from the status of other systems. This field is case-insensitive. | [optional] [default to 'default']

## Example

```python
from github_openapi.models.repos_create_commit_status_request import ReposCreateCommitStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateCommitStatusRequest from a JSON string
repos_create_commit_status_request_instance = ReposCreateCommitStatusRequest.from_json(json)
# print the JSON string representation of the object
print(ReposCreateCommitStatusRequest.to_json())

# convert the object into a dict
repos_create_commit_status_request_dict = repos_create_commit_status_request_instance.to_dict()
# create an instance of ReposCreateCommitStatusRequest from a dict
repos_create_commit_status_request_from_dict = ReposCreateCommitStatusRequest.from_dict(repos_create_commit_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


