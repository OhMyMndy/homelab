# IssuesLockRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lock_reason** | **str** | The reason for locking the issue or pull request conversation. Lock will fail if you don&#39;t use one of these reasons:    * &#x60;off-topic&#x60;    * &#x60;too heated&#x60;    * &#x60;resolved&#x60;    * &#x60;spam&#x60; | [optional] 

## Example

```python
from github_openapi.models.issues_lock_request import IssuesLockRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssuesLockRequest from a JSON string
issues_lock_request_instance = IssuesLockRequest.from_json(json)
# print the JSON string representation of the object
print(IssuesLockRequest.to_json())

# convert the object into a dict
issues_lock_request_dict = issues_lock_request_instance.to_dict()
# create an instance of IssuesLockRequest from a dict
issues_lock_request_from_dict = IssuesLockRequest.from_dict(issues_lock_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


