# IssuesRemoveSubIssueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_issue_id** | **int** | The sub-issue to remove | 

## Example

```python
from github_openapi.models.issues_remove_sub_issue_request import IssuesRemoveSubIssueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssuesRemoveSubIssueRequest from a JSON string
issues_remove_sub_issue_request_instance = IssuesRemoveSubIssueRequest.from_json(json)
# print the JSON string representation of the object
print(IssuesRemoveSubIssueRequest.to_json())

# convert the object into a dict
issues_remove_sub_issue_request_dict = issues_remove_sub_issue_request_instance.to_dict()
# create an instance of IssuesRemoveSubIssueRequest from a dict
issues_remove_sub_issue_request_from_dict = IssuesRemoveSubIssueRequest.from_dict(issues_remove_sub_issue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


