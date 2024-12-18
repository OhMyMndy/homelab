# UpdateContactRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The contact&#39;s email address. | 

## Example

```python
from tailscale_openapi.models.update_contact_request import UpdateContactRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateContactRequest from a JSON string
update_contact_request_instance = UpdateContactRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateContactRequest.to_json())

# convert the object into a dict
update_contact_request_dict = update_contact_request_instance.to_dict()
# create an instance of UpdateContactRequest from a dict
update_contact_request_from_dict = UpdateContactRequest.from_dict(update_contact_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


