# PagesHealthCheckDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 
**nameservers** | **str** |  | [optional] 
**dns_resolves** | **bool** |  | [optional] 
**is_proxied** | **bool** |  | [optional] 
**is_cloudflare_ip** | **bool** |  | [optional] 
**is_fastly_ip** | **bool** |  | [optional] 
**is_old_ip_address** | **bool** |  | [optional] 
**is_a_record** | **bool** |  | [optional] 
**has_cname_record** | **bool** |  | [optional] 
**has_mx_records_present** | **bool** |  | [optional] 
**is_valid_domain** | **bool** |  | [optional] 
**is_apex_domain** | **bool** |  | [optional] 
**should_be_a_record** | **bool** |  | [optional] 
**is_cname_to_github_user_domain** | **bool** |  | [optional] 
**is_cname_to_pages_dot_github_dot_com** | **bool** |  | [optional] 
**is_cname_to_fastly** | **bool** |  | [optional] 
**is_pointed_to_github_pages_ip** | **bool** |  | [optional] 
**is_non_github_pages_ip_present** | **bool** |  | [optional] 
**is_pages_domain** | **bool** |  | [optional] 
**is_served_by_pages** | **bool** |  | [optional] 
**is_valid** | **bool** |  | [optional] 
**reason** | **str** |  | [optional] 
**responds_to_https** | **bool** |  | [optional] 
**enforces_https** | **bool** |  | [optional] 
**https_error** | **str** |  | [optional] 
**is_https_eligible** | **bool** |  | [optional] 
**caa_error** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.pages_health_check_domain import PagesHealthCheckDomain

# TODO update the JSON string below
json = "{}"
# create an instance of PagesHealthCheckDomain from a JSON string
pages_health_check_domain_instance = PagesHealthCheckDomain.from_json(json)
# print the JSON string representation of the object
print(PagesHealthCheckDomain.to_json())

# convert the object into a dict
pages_health_check_domain_dict = pages_health_check_domain_instance.to_dict()
# create an instance of PagesHealthCheckDomain from a dict
pages_health_check_domain_from_dict = PagesHealthCheckDomain.from_dict(pages_health_check_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


