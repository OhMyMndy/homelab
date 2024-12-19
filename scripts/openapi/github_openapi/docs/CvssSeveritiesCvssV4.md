# CvssSeveritiesCvssV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vector_string** | **str** | The CVSS 4 vector string. | 
**score** | **float** | The CVSS 4 score. | [readonly] 

## Example

```python
from github_openapi.models.cvss_severities_cvss_v4 import CvssSeveritiesCvssV4

# TODO update the JSON string below
json = "{}"
# create an instance of CvssSeveritiesCvssV4 from a JSON string
cvss_severities_cvss_v4_instance = CvssSeveritiesCvssV4.from_json(json)
# print the JSON string representation of the object
print(CvssSeveritiesCvssV4.to_json())

# convert the object into a dict
cvss_severities_cvss_v4_dict = cvss_severities_cvss_v4_instance.to_dict()
# create an instance of CvssSeveritiesCvssV4 from a dict
cvss_severities_cvss_v4_from_dict = CvssSeveritiesCvssV4.from_dict(cvss_severities_cvss_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


