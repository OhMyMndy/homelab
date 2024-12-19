# FooterLink

Links returned in Config API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [readonly] 
**name** | **str** |  | [readonly] 

## Example

```python
from authentik_openapi.models.footer_link import FooterLink

# TODO update the JSON string below
json = "{}"
# create an instance of FooterLink from a JSON string
footer_link_instance = FooterLink.from_json(json)
# print the JSON string representation of the object
print(FooterLink.to_json())

# convert the object into a dict
footer_link_dict = footer_link_instance.to_dict()
# create an instance of FooterLink from a dict
footer_link_from_dict = FooterLink.from_dict(footer_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


