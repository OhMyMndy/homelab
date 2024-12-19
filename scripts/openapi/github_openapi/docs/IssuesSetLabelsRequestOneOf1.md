# IssuesSetLabelsRequestOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | [**List[IssuesSetLabelsRequestOneOf1LabelsInner]**](IssuesSetLabelsRequestOneOf1LabelsInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.issues_set_labels_request_one_of1 import IssuesSetLabelsRequestOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of IssuesSetLabelsRequestOneOf1 from a JSON string
issues_set_labels_request_one_of1_instance = IssuesSetLabelsRequestOneOf1.from_json(json)
# print the JSON string representation of the object
print(IssuesSetLabelsRequestOneOf1.to_json())

# convert the object into a dict
issues_set_labels_request_one_of1_dict = issues_set_labels_request_one_of1_instance.to_dict()
# create an instance of IssuesSetLabelsRequestOneOf1 from a dict
issues_set_labels_request_one_of1_from_dict = IssuesSetLabelsRequestOneOf1.from_dict(issues_set_labels_request_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


