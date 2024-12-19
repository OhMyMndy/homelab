# SAMLMetadata

SAML Provider Metadata serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **str** |  | [readonly] 
**download_url** | **str** |  | [readonly] 

## Example

```python
from authentik_openapi.models.saml_metadata import SAMLMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLMetadata from a JSON string
saml_metadata_instance = SAMLMetadata.from_json(json)
# print the JSON string representation of the object
print(SAMLMetadata.to_json())

# convert the object into a dict
saml_metadata_dict = saml_metadata_instance.to_dict()
# create an instance of SAMLMetadata from a dict
saml_metadata_from_dict = SAMLMetadata.from_dict(saml_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


