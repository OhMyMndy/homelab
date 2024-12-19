# IssuesAddLabelsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | [**List[IssuesSetLabelsRequestOneOf1LabelsInner]**](IssuesSetLabelsRequestOneOf1LabelsInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.issues_add_labels_request import IssuesAddLabelsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssuesAddLabelsRequest from a JSON string
issues_add_labels_request_instance = IssuesAddLabelsRequest.from_json(json)
# print the JSON string representation of the object
print(IssuesAddLabelsRequest.to_json())

# convert the object into a dict
issues_add_labels_request_dict = issues_add_labels_request_instance.to_dict()
# create an instance of IssuesAddLabelsRequest from a dict
issues_add_labels_request_from_dict = IssuesAddLabelsRequest.from_dict(issues_add_labels_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


