# IssueLabelsInnerOneOf


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
from github_openapi.models.issue_labels_inner_one_of import IssueLabelsInnerOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of IssueLabelsInnerOneOf from a JSON string
issue_labels_inner_one_of_instance = IssueLabelsInnerOneOf.from_json(json)
# print the JSON string representation of the object
print(IssueLabelsInnerOneOf.to_json())

# convert the object into a dict
issue_labels_inner_one_of_dict = issue_labels_inner_one_of_instance.to_dict()
# create an instance of IssueLabelsInnerOneOf from a dict
issue_labels_inner_one_of_from_dict = IssueLabelsInnerOneOf.from_dict(issue_labels_inner_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


