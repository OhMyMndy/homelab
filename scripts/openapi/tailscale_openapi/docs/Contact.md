# Contact

A tailnet contact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The contact&#39;s email address. | [optional] 
**fallback_email** | **str** | The email address used when contact&#39;s email address has not been verified. | [optional] 
**needs_verification** | **bool** | Indicates whether the contact&#39;s email address still needs to be verified. | [optional] 

## Example

```python
from tailscale_openapi.models.contact import Contact

# TODO update the JSON string below
json = "{}"
# create an instance of Contact from a JSON string
contact_instance = Contact.from_json(json)
# print the JSON string representation of the object
print(Contact.to_json())

# convert the object into a dict
contact_dict = contact_instance.to_dict()
# create an instance of Contact from a dict
contact_from_dict = Contact.from_dict(contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


