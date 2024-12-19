# Enterprise

An enterprise on GitHub.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A short description of the enterprise. | [optional] 
**html_url** | **str** |  | 
**website_url** | **str** | The enterprise&#39;s website URL. | [optional] 
**id** | **int** | Unique identifier of the enterprise | 
**node_id** | **str** |  | 
**name** | **str** | The name of the enterprise. | 
**slug** | **str** | The slug url identifier for the enterprise. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**avatar_url** | **str** |  | 

## Example

```python
from github_openapi.models.enterprise import Enterprise

# TODO update the JSON string below
json = "{}"
# create an instance of Enterprise from a JSON string
enterprise_instance = Enterprise.from_json(json)
# print the JSON string representation of the object
print(Enterprise.to_json())

# convert the object into a dict
enterprise_dict = enterprise_instance.to_dict()
# create an instance of Enterprise from a dict
enterprise_from_dict = Enterprise.from_dict(enterprise_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


