# CvssSeverities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cvss_v3** | [**CvssSeveritiesCvssV3**](CvssSeveritiesCvssV3.md) |  | [optional] 
**cvss_v4** | [**CvssSeveritiesCvssV4**](CvssSeveritiesCvssV4.md) |  | [optional] 

## Example

```python
from github_openapi.models.cvss_severities import CvssSeverities

# TODO update the JSON string below
json = "{}"
# create an instance of CvssSeverities from a JSON string
cvss_severities_instance = CvssSeverities.from_json(json)
# print the JSON string representation of the object
print(CvssSeverities.to_json())

# convert the object into a dict
cvss_severities_dict = cvss_severities_instance.to_dict()
# create an instance of CvssSeverities from a dict
cvss_severities_from_dict = CvssSeverities.from_dict(cvss_severities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


