# IssueLabelsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**node_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 

## Example

```python
from github_openapi.models.issue_labels_inner import IssueLabelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of IssueLabelsInner from a JSON string
issue_labels_inner_instance = IssueLabelsInner.from_json(json)
# print the JSON string representation of the object
print(IssueLabelsInner.to_json())

# convert the object into a dict
issue_labels_inner_dict = issue_labels_inner_instance.to_dict()
# create an instance of IssueLabelsInner from a dict
issue_labels_inner_from_dict = IssueLabelsInner.from_dict(issue_labels_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


