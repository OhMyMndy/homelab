# GpgKeyEmailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 

## Example

```python
from github_openapi.models.gpg_key_emails_inner import GpgKeyEmailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GpgKeyEmailsInner from a JSON string
gpg_key_emails_inner_instance = GpgKeyEmailsInner.from_json(json)
# print the JSON string representation of the object
print(GpgKeyEmailsInner.to_json())

# convert the object into a dict
gpg_key_emails_inner_dict = gpg_key_emails_inner_instance.to_dict()
# create an instance of GpgKeyEmailsInner from a dict
gpg_key_emails_inner_from_dict = GpgKeyEmailsInner.from_dict(gpg_key_emails_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


