# IssuesAddLabelsRequestOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **List[str]** | The names of the labels to add to the issue&#39;s existing labels. You can pass an empty array to remove all labels. Alternatively, you can pass a single label as a &#x60;string&#x60; or an &#x60;array&#x60; of labels directly, but GitHub recommends passing an object with the &#x60;labels&#x60; key. You can also replace all of the labels for an issue. For more information, see \&quot;[Set labels for an issue](https://docs.github.com/rest/issues/labels#set-labels-for-an-issue).\&quot; | [optional] 

## Example

```python
from github_openapi.models.issues_add_labels_request_one_of import IssuesAddLabelsRequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of IssuesAddLabelsRequestOneOf from a JSON string
issues_add_labels_request_one_of_instance = IssuesAddLabelsRequestOneOf.from_json(json)
# print the JSON string representation of the object
print(IssuesAddLabelsRequestOneOf.to_json())

# convert the object into a dict
issues_add_labels_request_one_of_dict = issues_add_labels_request_one_of_instance.to_dict()
# create an instance of IssuesAddLabelsRequestOneOf from a dict
issues_add_labels_request_one_of_from_dict = IssuesAddLabelsRequestOneOf.from_dict(issues_add_labels_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


