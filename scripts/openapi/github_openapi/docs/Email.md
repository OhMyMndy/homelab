# Email

Email

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**primary** | **bool** |  | 
**verified** | **bool** |  | 
**visibility** | **str** |  | 

## Example

```python
from github_openapi.models.email import Email

# TODO update the JSON string below
json = "{}"
# create an instance of Email from a JSON string
email_instance = Email.from_json(json)
# print the JSON string representation of the object
print(Email.to_json())

# convert the object into a dict
email_dict = email_instance.to_dict()
# create an instance of Email from a dict
email_from_dict = Email.from_dict(email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


