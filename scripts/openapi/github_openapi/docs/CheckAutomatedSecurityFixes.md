# CheckAutomatedSecurityFixes

Check Automated Security Fixes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether automated security fixes are enabled for the repository. | 
**paused** | **bool** | Whether automated security fixes are paused for the repository. | 

## Example

```python
from github_openapi.models.check_automated_security_fixes import CheckAutomatedSecurityFixes

# TODO update the JSON string below
json = "{}"
# create an instance of CheckAutomatedSecurityFixes from a JSON string
check_automated_security_fixes_instance = CheckAutomatedSecurityFixes.from_json(json)
# print the JSON string representation of the object
print(CheckAutomatedSecurityFixes.to_json())

# convert the object into a dict
check_automated_security_fixes_dict = check_automated_security_fixes_instance.to_dict()
# create an instance of CheckAutomatedSecurityFixes from a dict
check_automated_security_fixes_from_dict = CheckAutomatedSecurityFixes.from_dict(check_automated_security_fixes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


