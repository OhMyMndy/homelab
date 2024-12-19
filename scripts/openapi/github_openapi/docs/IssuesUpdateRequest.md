# IssuesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | [**IssuesUpdateRequestTitle**](IssuesUpdateRequestTitle.md) |  | [optional] 
**body** | **str** | The contents of the issue. | [optional] 
**assignee** | **str** | Username to assign to this issue. **This field is closing down.** | [optional] 
**state** | **str** | The open or closed state of the issue. | [optional] 
**state_reason** | **str** | The reason for the state change. Ignored unless &#x60;state&#x60; is changed. | [optional] 
**milestone** | [**IssuesUpdateRequestMilestone**](IssuesUpdateRequestMilestone.md) |  | [optional] 
**labels** | [**List[IssuesCreateRequestLabelsInner]**](IssuesCreateRequestLabelsInner.md) | Labels to associate with this issue. Pass one or more labels to _replace_ the set of labels on this issue. Send an empty array (&#x60;[]&#x60;) to clear all labels from the issue. Only users with push access can set labels for issues. Without push access to the repository, label changes are silently dropped. | [optional] 
**assignees** | **List[str]** | Usernames to assign to this issue. Pass one or more user logins to _replace_ the set of assignees on this issue. Send an empty array (&#x60;[]&#x60;) to clear all assignees from the issue. Only users with push access can set assignees for new issues. Without push access to the repository, assignee changes are silently dropped. | [optional] 

## Example

```python
from github_openapi.models.issues_update_request import IssuesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssuesUpdateRequest from a JSON string
issues_update_request_instance = IssuesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(IssuesUpdateRequest.to_json())

# convert the object into a dict
issues_update_request_dict = issues_update_request_instance.to_dict()
# create an instance of IssuesUpdateRequest from a dict
issues_update_request_from_dict = IssuesUpdateRequest.from_dict(issues_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


