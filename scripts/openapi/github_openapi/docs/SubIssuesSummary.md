# SubIssuesSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**completed** | **int** |  | 
**percent_completed** | **int** |  | 

## Example

```python
from github_openapi.models.sub_issues_summary import SubIssuesSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SubIssuesSummary from a JSON string
sub_issues_summary_instance = SubIssuesSummary.from_json(json)
# print the JSON string representation of the object
print(SubIssuesSummary.to_json())

# convert the object into a dict
sub_issues_summary_dict = sub_issues_summary_instance.to_dict()
# create an instance of SubIssuesSummary from a dict
sub_issues_summary_from_dict = SubIssuesSummary.from_dict(sub_issues_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


