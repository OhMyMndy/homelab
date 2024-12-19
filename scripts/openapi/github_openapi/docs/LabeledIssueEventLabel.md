# LabeledIssueEventLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**color** | **str** |  | 

## Example

```python
from github_openapi.models.labeled_issue_event_label import LabeledIssueEventLabel

# TODO update the JSON string below
json = "{}"
# create an instance of LabeledIssueEventLabel from a JSON string
labeled_issue_event_label_instance = LabeledIssueEventLabel.from_json(json)
# print the JSON string representation of the object
print(LabeledIssueEventLabel.to_json())

# convert the object into a dict
labeled_issue_event_label_dict = labeled_issue_event_label_instance.to_dict()
# create an instance of LabeledIssueEventLabel from a dict
labeled_issue_event_label_from_dict = LabeledIssueEventLabel.from_dict(labeled_issue_event_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


