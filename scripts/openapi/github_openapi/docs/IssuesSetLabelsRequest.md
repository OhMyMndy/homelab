# IssuesSetLabelsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | [**List[IssuesSetLabelsRequestOneOf1LabelsInner]**](IssuesSetLabelsRequestOneOf1LabelsInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.issues_set_labels_request import IssuesSetLabelsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssuesSetLabelsRequest from a JSON string
issues_set_labels_request_instance = IssuesSetLabelsRequest.from_json(json)
# print the JSON string representation of the object
print(IssuesSetLabelsRequest.to_json())

# convert the object into a dict
issues_set_labels_request_dict = issues_set_labels_request_instance.to_dict()
# create an instance of IssuesSetLabelsRequest from a dict
issues_set_labels_request_from_dict = IssuesSetLabelsRequest.from_dict(issues_set_labels_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


