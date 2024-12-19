# NullableLicenseSimple

License Simple

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**name** | **str** |  | 
**url** | **str** |  | 
**spdx_id** | **str** |  | 
**node_id** | **str** |  | 
**html_url** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.nullable_license_simple import NullableLicenseSimple

# TODO update the JSON string below
json = "{}"
# create an instance of NullableLicenseSimple from a JSON string
nullable_license_simple_instance = NullableLicenseSimple.from_json(json)
# print the JSON string representation of the object
print(NullableLicenseSimple.to_json())

# convert the object into a dict
nullable_license_simple_dict = nullable_license_simple_instance.to_dict()
# create an instance of NullableLicenseSimple from a dict
nullable_license_simple_from_dict = NullableLicenseSimple.from_dict(nullable_license_simple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


