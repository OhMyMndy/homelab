# CvssSeveritiesCvssV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vector_string** | **str** | The CVSS 3 vector string. | 
**score** | **float** | The CVSS 3 score. | [readonly] 

## Example

```python
from github_openapi.models.cvss_severities_cvss_v3 import CvssSeveritiesCvssV3

# TODO update the JSON string below
json = "{}"
# create an instance of CvssSeveritiesCvssV3 from a JSON string
cvss_severities_cvss_v3_instance = CvssSeveritiesCvssV3.from_json(json)
# print the JSON string representation of the object
print(CvssSeveritiesCvssV3.to_json())

# convert the object into a dict
cvss_severities_cvss_v3_dict = cvss_severities_cvss_v3_instance.to_dict()
# create an instance of CvssSeveritiesCvssV3 from a dict
cvss_severities_cvss_v3_from_dict = CvssSeveritiesCvssV3.from_dict(cvss_severities_cvss_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


