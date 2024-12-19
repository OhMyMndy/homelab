# ConsentPermission

Permission used for consent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from authentik_openapi.models.consent_permission import ConsentPermission

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentPermission from a JSON string
consent_permission_instance = ConsentPermission.from_json(json)
# print the JSON string representation of the object
print(ConsentPermission.to_json())

# convert the object into a dict
consent_permission_dict = consent_permission_instance.to_dict()
# create an instance of ConsentPermission from a dict
consent_permission_from_dict = ConsentPermission.from_dict(consent_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


