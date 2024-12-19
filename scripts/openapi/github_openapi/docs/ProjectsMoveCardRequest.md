# ProjectsMoveCardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | The position of the card in a column. Can be one of: &#x60;top&#x60;, &#x60;bottom&#x60;, or &#x60;after:&lt;card_id&gt;&#x60; to place after the specified card. | 
**column_id** | **int** | The unique identifier of the column the card should be moved to | [optional] 

## Example

```python
from github_openapi.models.projects_move_card_request import ProjectsMoveCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsMoveCardRequest from a JSON string
projects_move_card_request_instance = ProjectsMoveCardRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectsMoveCardRequest.to_json())

# convert the object into a dict
projects_move_card_request_dict = projects_move_card_request_instance.to_dict()
# create an instance of ProjectsMoveCardRequest from a dict
projects_move_card_request_from_dict = ProjectsMoveCardRequest.from_dict(projects_move_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


