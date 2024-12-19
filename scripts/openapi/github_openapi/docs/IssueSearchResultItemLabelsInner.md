# IssueSearchResultItemLabelsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**node_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.issue_search_result_item_labels_inner import IssueSearchResultItemLabelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of IssueSearchResultItemLabelsInner from a JSON string
issue_search_result_item_labels_inner_instance = IssueSearchResultItemLabelsInner.from_json(json)
# print the JSON string representation of the object
print(IssueSearchResultItemLabelsInner.to_json())

# convert the object into a dict
issue_search_result_item_labels_inner_dict = issue_search_result_item_labels_inner_instance.to_dict()
# create an instance of IssueSearchResultItemLabelsInner from a dict
issue_search_result_item_labels_inner_from_dict = IssueSearchResultItemLabelsInner.from_dict(issue_search_result_item_labels_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


