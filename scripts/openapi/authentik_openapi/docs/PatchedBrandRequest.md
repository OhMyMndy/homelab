# PatchedBrandRequest

Brand Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain that activates this brand. Can be a superset, i.e. &#x60;a.b&#x60; for &#x60;aa.b&#x60; and &#x60;ba.b&#x60; | [optional] 
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
from authentik_openapi.models.patched_brand_request import PatchedBrandRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedBrandRequest from a JSON string
patched_brand_request_instance = PatchedBrandRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedBrandRequest.to_json())

# convert the object into a dict
patched_brand_request_dict = patched_brand_request_instance.to_dict()
# create an instance of PatchedBrandRequest from a dict
patched_brand_request_from_dict = PatchedBrandRequest.from_dict(patched_brand_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


