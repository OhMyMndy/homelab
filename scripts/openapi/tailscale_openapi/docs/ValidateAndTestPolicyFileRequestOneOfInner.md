# ValidateAndTestPolicyFileRequestOneOfInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src** | **str** | Specifies the user identity to test, which can be  a [user&#39;s email address](https://tailscale.com/kb/1337/acl-syntax#reference-users), a [group](https://tailscale.com/kb/1337/acl-syntax#groups), a [tag](https://tailscale.com/kb/1068/acl-tags), or a [host](https://tailscale.com/kb/1337/acl-syntax#hosts) that maps to an IP address. The test case runs from the perspective of a device authenticated with the provided identity.  | 
**src_posture_attrs** | [**Dict[str, ValidateAndTestPolicyFileRequestOneOfInnerSrcPostureAttrsValue]**](ValidateAndTestPolicyFileRequestOneOfInnerSrcPostureAttrsValue.md) | Specifies the [device posture attributes](https://tailscale.com/kb/1337/acl-syntax#proto-1) as key-value pairs to use when evaluating posture conditions in access rules. You only need to use this field if the access rules contain  [device posture conditions](https://tailscale.com/kb/1288/device-posture#device-posture-conditions).  | [optional] 
**proto** | **str** | Specifies the IP protocol for &#x60;accept&#x60; and &#x60;deny&#x60; rules, similar to the &#x60;proto&#x60; field in [ACL rules](https://tailscale.com/kb/1337/acl-syntax#acls). When omitted, the test checks for either TCP or UDP access.  | [optional] 
**accept** | **List[str]** | Specifies destinations to accept. Each destination in the list is of the form &#x60;host:port&#x60; where &#x60;port&#x60; is a single numeric port and &#x60;host&#x60; is in the format described in the [acl syntax](https://tailscale.com/kb/1337/acl-syntax#accept-and-deny-destinations) documentation.  Sources in &#x60;src&#x60; and &#x60;destinations&#x60; must refer to specific entities and do not support &#x60;*&#x60; wildcards. For example, an &#x60;accept&#x60; destination cannot be &#x60;tags:*&#x60;.  | [optional] 
**deny** | **List[str]** | Specifies destinations to deny. Each destination in the list is of the form &#x60;host:port&#x60; where &#x60;port&#x60; is a single numeric port and &#x60;host&#x60; is in the format described in the [acl syntax](https://tailscale.com/kb/1337/acl-syntax#accept-and-deny-destinations) documentation.  Sources in &#x60;src&#x60; and &#x60;destinations&#x60; must refer to specific entities and do not support &#x60;*&#x60; wildcards. For example, a &#x60;deny&#x60; destination cannot be &#x60;tags:*&#x60;.  | [optional] 

## Example

```python
from tailscale_openapi.models.validate_and_test_policy_file_request_one_of_inner import ValidateAndTestPolicyFileRequestOneOfInner

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateAndTestPolicyFileRequestOneOfInner from a JSON string
validate_and_test_policy_file_request_one_of_inner_instance = ValidateAndTestPolicyFileRequestOneOfInner.from_json(json)
# print the JSON string representation of the object
print(ValidateAndTestPolicyFileRequestOneOfInner.to_json())

# convert the object into a dict
validate_and_test_policy_file_request_one_of_inner_dict = validate_and_test_policy_file_request_one_of_inner_instance.to_dict()
# create an instance of ValidateAndTestPolicyFileRequestOneOfInner from a dict
validate_and_test_policy_file_request_one_of_inner_from_dict = ValidateAndTestPolicyFileRequestOneOfInner.from_dict(validate_and_test_policy_file_request_one_of_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


