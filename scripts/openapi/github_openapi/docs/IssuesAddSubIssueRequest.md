# IssuesAddSubIssueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_issue_id** | **int** | The sub-issue to add | 
**replace_parent** | **bool** | Option that, when true, instructs the operation to replace the sub-issues current parent issue | [optional] 

## Example

```python
from github_openapi.models.issues_add_sub_issue_request import IssuesAddSubIssueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssuesAddSubIssueRequest from a JSON string
issues_add_sub_issue_request_instance = IssuesAddSubIssueRequest.from_json(json)
# print the JSON string representation of the object
print(IssuesAddSubIssueRequest.to_json())

# convert the object into a dict
issues_add_sub_issue_request_dict = issues_add_sub_issue_request_instance.to_dict()
# create an instance of IssuesAddSubIssueRequest from a dict
issues_add_sub_issue_request_from_dict = IssuesAddSubIssueRequest.from_dict(issues_add_sub_issue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


