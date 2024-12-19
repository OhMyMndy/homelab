# PorterAuthor

Porter Author

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**remote_id** | **str** |  | 
**remote_name** | **str** |  | 
**email** | **str** |  | 
**name** | **str** |  | 
**url** | **str** |  | 
**import_url** | **str** |  | 

## Example

```python
from github_openapi.models.porter_author import PorterAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of PorterAuthor from a JSON string
porter_author_instance = PorterAuthor.from_json(json)
# print the JSON string representation of the object
print(PorterAuthor.to_json())

# convert the object into a dict
porter_author_dict = porter_author_instance.to_dict()
# create an instance of PorterAuthor from a dict
porter_author_from_dict = PorterAuthor.from_dict(porter_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


