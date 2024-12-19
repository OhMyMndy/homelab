# IssueEventLabel

Issue Event Label

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**color** | **str** |  | 

## Example

```python
from github_openapi.models.issue_event_label import IssueEventLabel

# TODO update the JSON string below
json = "{}"
# create an instance of IssueEventLabel from a JSON string
issue_event_label_instance = IssueEventLabel.from_json(json)
# print the JSON string representation of the object
print(IssueEventLabel.to_json())

# convert the object into a dict
issue_event_label_dict = issue_event_label_instance.to_dict()
# create an instance of IssueEventLabel from a dict
issue_event_label_from_dict = IssueEventLabel.from_dict(issue_event_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


