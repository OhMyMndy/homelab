# IssuesUpdateMilestoneRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the milestone. | [optional] 
**state** | **str** | The state of the milestone. Either &#x60;open&#x60; or &#x60;closed&#x60;. | [optional] [default to 'open']
**description** | **str** | A description of the milestone. | [optional] 
**due_on** | **datetime** | The milestone due date. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 

## Example

```python
from github_openapi.models.issues_update_milestone_request import IssuesUpdateMilestoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssuesUpdateMilestoneRequest from a JSON string
issues_update_milestone_request_instance = IssuesUpdateMilestoneRequest.from_json(json)
# print the JSON string representation of the object
print(IssuesUpdateMilestoneRequest.to_json())

# convert the object into a dict
issues_update_milestone_request_dict = issues_update_milestone_request_instance.to_dict()
# create an instance of IssuesUpdateMilestoneRequest from a dict
issues_update_milestone_request_from_dict = IssuesUpdateMilestoneRequest.from_dict(issues_update_milestone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


