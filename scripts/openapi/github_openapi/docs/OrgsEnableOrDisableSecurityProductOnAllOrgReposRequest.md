# OrgsEnableOrDisableSecurityProductOnAllOrgReposRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_suite** | **str** | CodeQL query suite to be used. If you specify the &#x60;query_suite&#x60; parameter, the default setup will be configured with this query suite only on all repositories that didn&#39;t have default setup already configured. It will not change the query suite on repositories that already have default setup configured. If you don&#39;t specify any &#x60;query_suite&#x60; in your request, the preferred query suite of the organization will be applied. | [optional] 

## Example

```python
from github_openapi.models.orgs_enable_or_disable_security_product_on_all_org_repos_request import OrgsEnableOrDisableSecurityProductOnAllOrgReposRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrgsEnableOrDisableSecurityProductOnAllOrgReposRequest from a JSON string
orgs_enable_or_disable_security_product_on_all_org_repos_request_instance = OrgsEnableOrDisableSecurityProductOnAllOrgReposRequest.from_json(json)
# print the JSON string representation of the object
print(OrgsEnableOrDisableSecurityProductOnAllOrgReposRequest.to_json())

# convert the object into a dict
orgs_enable_or_disable_security_product_on_all_org_repos_request_dict = orgs_enable_or_disable_security_product_on_all_org_repos_request_instance.to_dict()
# create an instance of OrgsEnableOrDisableSecurityProductOnAllOrgReposRequest from a dict
orgs_enable_or_disable_security_product_on_all_org_repos_request_from_dict = OrgsEnableOrDisableSecurityProductOnAllOrgReposRequest.from_dict(orgs_enable_or_disable_security_product_on_all_org_repos_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


