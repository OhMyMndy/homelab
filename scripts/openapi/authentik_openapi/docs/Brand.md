# Brand

Brand Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_uuid** | **str** |  | [readonly] 
**domain** | **str** | Domain that activates this brand. Can be a superset, i.e. &#x60;a.b&#x60; for &#x60;aa.b&#x60; and &#x60;ba.b&#x60; | 
**default** | **bool** |  | [optional] 
**branding_title** | **str** |  | [optional] 
**branding_logo** | **str** |  | [optional] 
**branding_favicon** | **str** |  | [optional] 
**flow_authentication** | **str** |  | [optional] 
**flow_invalidation** | **str** |  | [optional] 
**flow_recovery** | **str** |  | [optional] 
**flow_unenrollment** | **str** |  | [optional] 
**flow_user_settings** | **str** |  | [optional] 
**flow_device_code** | **str** |  | [optional] 
**web_certificate** | **str** | Web Certificate used by the authentik Core webserver. | [optional] 
**attributes** | **object** |  | [optional] 

## Example

```python
from authentik_openapi.models.brand import Brand

# TODO update the JSON string below
json = "{}"
# create an instance of Brand from a JSON string
brand_instance = Brand.from_json(json)
# print the JSON string representation of the object
print(Brand.to_json())

# convert the object into a dict
brand_dict = brand_instance.to_dict()
# create an instance of Brand from a dict
brand_from_dict = Brand.from_dict(brand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


