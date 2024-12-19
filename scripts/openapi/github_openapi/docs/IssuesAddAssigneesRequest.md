# IssuesAddAssigneesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignees** | **List[str]** | Usernames of people to assign this issue to. _NOTE: Only users with push access can add assignees to an issue. Assignees are silently ignored otherwise._ | [optional] 

## Example

```python
from github_openapi.models.issues_add_assignees_request import IssuesAddAssigneesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssuesAddAssigneesRequest from a JSON string
issues_add_assignees_request_instance = IssuesAddAssigneesRequest.from_json(json)
# print the JSON string representation of the object
print(IssuesAddAssigneesRequest.to_json())

# convert the object into a dict
issues_add_assignees_request_dict = issues_add_assignees_request_instance.to_dict()
# create an instance of IssuesAddAssigneesRequest from a dict
issues_add_assignees_request_from_dict = IssuesAddAssigneesRequest.from_dict(issues_add_assignees_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


