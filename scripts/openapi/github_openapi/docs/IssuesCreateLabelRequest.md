# IssuesCreateLabelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the label. Emoji can be added to label names, using either native emoji or colon-style markup. For example, typing &#x60;:strawberry:&#x60; will render the emoji ![:strawberry:](https://github.githubassets.com/images/icons/emoji/unicode/1f353.png \&quot;:strawberry:\&quot;). For a full list of available emoji and codes, see \&quot;[Emoji cheat sheet](https://github.com/ikatyang/emoji-cheat-sheet).\&quot; | 
**color** | **str** | The [hexadecimal color code](http://www.color-hex.com/) for the label, without the leading &#x60;#&#x60;. | [optional] 
**description** | **str** | A short description of the label. Must be 100 characters or fewer. | [optional] 

## Example

```python
from github_openapi.models.issues_create_label_request import IssuesCreateLabelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssuesCreateLabelRequest from a JSON string
issues_create_label_request_instance = IssuesCreateLabelRequest.from_json(json)
# print the JSON string representation of the object
print(IssuesCreateLabelRequest.to_json())

# convert the object into a dict
issues_create_label_request_dict = issues_create_label_request_instance.to_dict()
# create an instance of IssuesCreateLabelRequest from a dict
issues_create_label_request_from_dict = IssuesCreateLabelRequest.from_dict(issues_create_label_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


