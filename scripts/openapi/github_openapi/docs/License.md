# License


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**name** | **str** |  | 
**node_id** | **str** |  | 
**spdx_id** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.license import License

# TODO update the JSON string below
json = "{}"
# create an instance of License from a JSON string
license_instance = License.from_json(json)
# print the JSON string representation of the object
print(License.to_json())

# convert the object into a dict
license_dict = license_instance.to_dict()
# create an instance of License from a dict
license_from_dict = License.from_dict(license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


