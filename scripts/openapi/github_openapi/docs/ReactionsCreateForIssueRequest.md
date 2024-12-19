# ReactionsCreateForIssueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | The [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions) to add to the issue. | 

## Example

```python
from github_openapi.models.reactions_create_for_issue_request import ReactionsCreateForIssueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionsCreateForIssueRequest from a JSON string
reactions_create_for_issue_request_instance = ReactionsCreateForIssueRequest.from_json(json)
# print the JSON string representation of the object
print(ReactionsCreateForIssueRequest.to_json())

# convert the object into a dict
reactions_create_for_issue_request_dict = reactions_create_for_issue_request_instance.to_dict()
# create an instance of ReactionsCreateForIssueRequest from a dict
reactions_create_for_issue_request_from_dict = ReactionsCreateForIssueRequest.from_dict(reactions_create_for_issue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


