# Label1


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
from github_openapi.models.label1 import Label1

# TODO update the JSON string below
json = "{}"
# create an instance of Label1 from a JSON string
label1_instance = Label1.from_json(json)
# print the JSON string representation of the object
print(Label1.to_json())

# convert the object into a dict
label1_dict = label1_instance.to_dict()
# create an instance of Label1 from a dict
label1_from_dict = Label1.from_dict(label1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


