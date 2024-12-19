# IssuesReprioritizeSubIssueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_issue_id** | **int** | The id of the sub-issue to reprioritize | 
**after_id** | **int** | The id of the sub-issue to be prioritized after (either positional argument after OR before should be specified). | [optional] 
**before_id** | **int** | The id of the sub-issue to be prioritized before (either positional argument after OR before should be specified). | [optional] 

## Example

```python
from github_openapi.models.issues_reprioritize_sub_issue_request import IssuesReprioritizeSubIssueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssuesReprioritizeSubIssueRequest from a JSON string
issues_reprioritize_sub_issue_request_instance = IssuesReprioritizeSubIssueRequest.from_json(json)
# print the JSON string representation of the object
print(IssuesReprioritizeSubIssueRequest.to_json())

# convert the object into a dict
issues_reprioritize_sub_issue_request_dict = issues_reprioritize_sub_issue_request_instance.to_dict()
# create an instance of IssuesReprioritizeSubIssueRequest from a dict
issues_reprioritize_sub_issue_request_from_dict = IssuesReprioritizeSubIssueRequest.from_dict(issues_reprioritize_sub_issue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


