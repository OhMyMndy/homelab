# IssuesCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | [**IssuesCreateRequestTitle**](IssuesCreateRequestTitle.md) |  | 
**body** | **str** | The contents of the issue. | [optional] 
**assignee** | **str** | Login for the user that this issue should be assigned to. _NOTE: Only users with push access can set the assignee for new issues. The assignee is silently dropped otherwise. **This field is closing down.**_ | [optional] 
**milestone** | [**IssuesCreateRequestMilestone**](IssuesCreateRequestMilestone.md) |  | [optional] 
**labels** | [**List[IssuesCreateRequestLabelsInner]**](IssuesCreateRequestLabelsInner.md) | Labels to associate with this issue. _NOTE: Only users with push access can set labels for new issues. Labels are silently dropped otherwise._ | [optional] 
**assignees** | **List[str]** | Logins for Users to assign to this issue. _NOTE: Only users with push access can set assignees for new issues. Assignees are silently dropped otherwise._ | [optional] 

## Example

```python
from github_openapi.models.issues_create_request import IssuesCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssuesCreateRequest from a JSON string
issues_create_request_instance = IssuesCreateRequest.from_json(json)
# print the JSON string representation of the object
print(IssuesCreateRequest.to_json())

# convert the object into a dict
issues_create_request_dict = issues_create_request_instance.to_dict()
# create an instance of IssuesCreateRequest from a dict
issues_create_request_from_dict = IssuesCreateRequest.from_dict(issues_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


