# IssuesCreateRequestLabelsInnerOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**color** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.issues_create_request_labels_inner_one_of import IssuesCreateRequestLabelsInnerOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of IssuesCreateRequestLabelsInnerOneOf from a JSON string
issues_create_request_labels_inner_one_of_instance = IssuesCreateRequestLabelsInnerOneOf.from_json(json)
# print the JSON string representation of the object
print(IssuesCreateRequestLabelsInnerOneOf.to_json())

# convert the object into a dict
issues_create_request_labels_inner_one_of_dict = issues_create_request_labels_inner_one_of_instance.to_dict()
# create an instance of IssuesCreateRequestLabelsInnerOneOf from a dict
issues_create_request_labels_inner_one_of_from_dict = IssuesCreateRequestLabelsInnerOneOf.from_dict(issues_create_request_labels_inner_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


