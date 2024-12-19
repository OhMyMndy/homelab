# LicenseContent

License Content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**path** | **str** |  | 
**sha** | **str** |  | 
**size** | **int** |  | 
**url** | **str** |  | 
**html_url** | **str** |  | 
**git_url** | **str** |  | 
**download_url** | **str** |  | 
**type** | **str** |  | 
**content** | **str** |  | 
**encoding** | **str** |  | 
**links** | [**ContentTreeEntriesInnerLinks**](ContentTreeEntriesInnerLinks.md) |  | 
**license** | [**NullableLicenseSimple**](NullableLicenseSimple.md) |  | 

## Example

```python
from github_openapi.models.license_content import LicenseContent

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseContent from a JSON string
license_content_instance = LicenseContent.from_json(json)
# print the JSON string representation of the object
print(LicenseContent.to_json())

# convert the object into a dict
license_content_dict = license_content_instance.to_dict()
# create an instance of LicenseContent from a dict
license_content_from_dict = LicenseContent.from_dict(license_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


