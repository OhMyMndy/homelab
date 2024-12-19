# DuoDeviceEnrollmentStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duo_response** | [**DuoResponseEnum**](DuoResponseEnum.md) |  | 

## Example

```python
from authentik_openapi.models.duo_device_enrollment_status import DuoDeviceEnrollmentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DuoDeviceEnrollmentStatus from a JSON string
duo_device_enrollment_status_instance = DuoDeviceEnrollmentStatus.from_json(json)
# print the JSON string representation of the object
print(DuoDeviceEnrollmentStatus.to_json())

# convert the object into a dict
duo_device_enrollment_status_dict = duo_device_enrollment_status_instance.to_dict()
# create an instance of DuoDeviceEnrollmentStatus from a dict
duo_device_enrollment_status_from_dict = DuoDeviceEnrollmentStatus.from_dict(duo_device_enrollment_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


