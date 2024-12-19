# UserConsent

UserConsent Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**expires** | **datetime** |  | [optional] 
**expiring** | **bool** |  | [optional] 
**user** | [**User**](User.md) |  | 
**application** | [**Application**](Application.md) |  | 
**permissions** | **str** |  | [optional] [default to '']

## Example

```python
from authentik_openapi.models.user_consent import UserConsent

# TODO update the JSON string below
json = "{}"
# create an instance of UserConsent from a JSON string
user_consent_instance = UserConsent.from_json(json)
# print the JSON string representation of the object
print(UserConsent.to_json())

# convert the object into a dict
user_consent_dict = user_consent_instance.to_dict()
# create an instance of UserConsent from a dict
user_consent_from_dict = UserConsent.from_dict(user_consent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


