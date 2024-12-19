# Label


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | 6-character hex code, without the leading #, identifying the color | 
**default** | **bool** |  | 
**description** | **str** |  | 
**id** | **int** |  | 
**name** | **str** | The name of the label. | 
**node_id** | **str** |  | 
**url** | **str** | URL for the label | 

## Example

```python
from github_openapi.models.label import Label

# TODO update the JSON string below
json = "{}"
# create an instance of Label from a JSON string
label_instance = Label.from_json(json)
# print the JSON string representation of the object
print(Label.to_json())

# convert the object into a dict
label_dict = label_instance.to_dict()
# create an instance of Label from a dict
label_from_dict = Label.from_dict(label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

