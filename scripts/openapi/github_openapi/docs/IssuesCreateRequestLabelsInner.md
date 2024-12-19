# IssuesCreateRequestLabelsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**color** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.issues_create_request_labels_inner import IssuesCreateRequestLabelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of IssuesCreateRequestLabelsInner from a JSON string
issues_create_request_labels_inner_instance = IssuesCreateRequestLabelsInner.from_json(json)
# print the JSON string representation of the object
print(IssuesCreateRequestLabelsInner.to_json())

# convert the object into a dict
issues_create_request_labels_inner_dict = issues_create_request_labels_inner_instance.to_dict()
# create an instance of IssuesCreateRequestLabelsInner from a dict
issues_create_request_labels_inner_from_dict = IssuesCreateRequestLabelsInner.from_dict(issues_create_request_labels_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


