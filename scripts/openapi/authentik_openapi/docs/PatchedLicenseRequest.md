# PatchedLicenseRequest

License Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_license_request import PatchedLicenseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedLicenseRequest from a JSON string
patched_license_request_instance = PatchedLicenseRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedLicenseRequest.to_json())

# convert the object into a dict
patched_license_request_dict = patched_license_request_instance.to_dict()
# create an instance of PatchedLicenseRequest from a dict
patched_license_request_from_dict = PatchedLicenseRequest.from_dict(patched_license_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


