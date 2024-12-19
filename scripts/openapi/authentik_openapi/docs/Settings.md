# Settings

Settings Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatars** | **str** | Configure how authentik should show avatars for users. | [optional] 
**default_user_change_name** | **bool** | Enable the ability for users to change their name. | [optional] 
**default_user_change_email** | **bool** | Enable the ability for users to change their email address. | [optional] 
**default_user_change_username** | **bool** | Enable the ability for users to change their username. | [optional] 
**event_retention** | **str** | Events will be deleted after this duration.(Format: weeks&#x3D;3;days&#x3D;2;hours&#x3D;3,seconds&#x3D;2). | [optional] 
**footer_links** | **object** | The option configures the footer links on the flow executor pages. | [optional] 
**gdpr_compliance** | **bool** | When enabled, all the events caused by a user will be deleted upon the user&#39;s deletion. | [optional] 
**impersonation** | **bool** | Globally enable/disable impersonation. | [optional] 
**default_token_duration** | **str** | Default token duration | [optional] 
**default_token_length** | **int** | Default token length | [optional] 

## Example

```python
from authentik_openapi.models.settings import Settings

# TODO update the JSON string below
json = "{}"
# create an instance of Settings from a JSON string
settings_instance = Settings.from_json(json)
# print the JSON string representation of the object
print(Settings.to_json())

# convert the object into a dict
settings_dict = settings_instance.to_dict()
# create an instance of Settings from a dict
settings_from_dict = Settings.from_dict(settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


