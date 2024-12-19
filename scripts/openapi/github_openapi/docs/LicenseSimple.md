# LicenseSimple

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
from github_openapi.models.license_simple import LicenseSimple

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseSimple from a JSON string
license_simple_instance = LicenseSimple.from_json(json)
# print the JSON string representation of the object
print(LicenseSimple.to_json())

# convert the object into a dict
license_simple_dict = license_simple_instance.to_dict()
# create an instance of LicenseSimple from a dict
license_simple_from_dict = LicenseSimple.from_dict(license_simple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


