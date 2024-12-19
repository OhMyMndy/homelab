# License

License Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_uuid** | **str** |  | [readonly] 
**name** | **str** |  | [readonly] 
**key** | **str** |  | 
**expiry** | **datetime** |  | [readonly] 
**internal_users** | **int** |  | [readonly] 
**external_users** | **int** |  | [readonly] 

## Example

```python
from authentik_openapi.models.license import License

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


