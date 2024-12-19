# PagesHttpsCertificate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | 
**description** | **str** |  | 
**domains** | **List[str]** | Array of the domain set and its alternate name (if it is configured) | 
**expires_at** | **date** |  | [optional] 

## Example

```python
from github_openapi.models.pages_https_certificate import PagesHttpsCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of PagesHttpsCertificate from a JSON string
pages_https_certificate_instance = PagesHttpsCertificate.from_json(json)
# print the JSON string representation of the object
print(PagesHttpsCertificate.to_json())

# convert the object into a dict
pages_https_certificate_dict = pages_https_certificate_instance.to_dict()
# create an instance of PagesHttpsCertificate from a dict
pages_https_certificate_from_dict = PagesHttpsCertificate.from_dict(pages_https_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


