# IssuesRemoveAssigneesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignees** | **List[str]** | Usernames of assignees to remove from an issue. _NOTE: Only users with push access can remove assignees from an issue. Assignees are silently ignored otherwise._ | [optional] 

## Example

```python
from github_openapi.models.issues_remove_assignees_request import IssuesRemoveAssigneesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssuesRemoveAssigneesRequest from a JSON string
issues_remove_assignees_request_instance = IssuesRemoveAssigneesRequest.from_json(json)
# print the JSON string representation of the object
print(IssuesRemoveAssigneesRequest.to_json())

# convert the object into a dict
issues_remove_assignees_request_dict = issues_remove_assignees_request_instance.to_dict()
# create an instance of IssuesRemoveAssigneesRequest from a dict
issues_remove_assignees_request_from_dict = IssuesRemoveAssigneesRequest.from_dict(issues_remove_assignees_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


