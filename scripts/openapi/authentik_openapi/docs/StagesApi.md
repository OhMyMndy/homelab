# authentik_openapi.StagesApi

All URIs are relative to *https://auth.home.ohmymndy.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stages_all_destroy**](StagesApi.md#stages_all_destroy) | **DELETE** /stages/all/{stage_uuid}/ | 
[**stages_all_list**](StagesApi.md#stages_all_list) | **GET** /stages/all/ | 
[**stages_all_retrieve**](StagesApi.md#stages_all_retrieve) | **GET** /stages/all/{stage_uuid}/ | 
[**stages_all_types_list**](StagesApi.md#stages_all_types_list) | **GET** /stages/all/types/ | 
[**stages_all_used_by_list**](StagesApi.md#stages_all_used_by_list) | **GET** /stages/all/{stage_uuid}/used_by/ | 
[**stages_all_user_settings_list**](StagesApi.md#stages_all_user_settings_list) | **GET** /stages/all/user_settings/ | 
[**stages_authenticator_duo_create**](StagesApi.md#stages_authenticator_duo_create) | **POST** /stages/authenticator/duo/ | 
[**stages_authenticator_duo_destroy**](StagesApi.md#stages_authenticator_duo_destroy) | **DELETE** /stages/authenticator/duo/{stage_uuid}/ | 
[**stages_authenticator_duo_enrollment_status_create**](StagesApi.md#stages_authenticator_duo_enrollment_status_create) | **POST** /stages/authenticator/duo/{stage_uuid}/enrollment_status/ | 
[**stages_authenticator_duo_import_device_manual_create**](StagesApi.md#stages_authenticator_duo_import_device_manual_create) | **POST** /stages/authenticator/duo/{stage_uuid}/import_device_manual/ | 
[**stages_authenticator_duo_import_devices_automatic_create**](StagesApi.md#stages_authenticator_duo_import_devices_automatic_create) | **POST** /stages/authenticator/duo/{stage_uuid}/import_devices_automatic/ | 
[**stages_authenticator_duo_list**](StagesApi.md#stages_authenticator_duo_list) | **GET** /stages/authenticator/duo/ | 
[**stages_authenticator_duo_partial_update**](StagesApi.md#stages_authenticator_duo_partial_update) | **PATCH** /stages/authenticator/duo/{stage_uuid}/ | 
[**stages_authenticator_duo_retrieve**](StagesApi.md#stages_authenticator_duo_retrieve) | **GET** /stages/authenticator/duo/{stage_uuid}/ | 
[**stages_authenticator_duo_update**](StagesApi.md#stages_authenticator_duo_update) | **PUT** /stages/authenticator/duo/{stage_uuid}/ | 
[**stages_authenticator_duo_used_by_list**](StagesApi.md#stages_authenticator_duo_used_by_list) | **GET** /stages/authenticator/duo/{stage_uuid}/used_by/ | 
[**stages_authenticator_sms_create**](StagesApi.md#stages_authenticator_sms_create) | **POST** /stages/authenticator/sms/ | 
[**stages_authenticator_sms_destroy**](StagesApi.md#stages_authenticator_sms_destroy) | **DELETE** /stages/authenticator/sms/{stage_uuid}/ | 
[**stages_authenticator_sms_list**](StagesApi.md#stages_authenticator_sms_list) | **GET** /stages/authenticator/sms/ | 
[**stages_authenticator_sms_partial_update**](StagesApi.md#stages_authenticator_sms_partial_update) | **PATCH** /stages/authenticator/sms/{stage_uuid}/ | 
[**stages_authenticator_sms_retrieve**](StagesApi.md#stages_authenticator_sms_retrieve) | **GET** /stages/authenticator/sms/{stage_uuid}/ | 
[**stages_authenticator_sms_update**](StagesApi.md#stages_authenticator_sms_update) | **PUT** /stages/authenticator/sms/{stage_uuid}/ | 
[**stages_authenticator_sms_used_by_list**](StagesApi.md#stages_authenticator_sms_used_by_list) | **GET** /stages/authenticator/sms/{stage_uuid}/used_by/ | 
[**stages_authenticator_static_create**](StagesApi.md#stages_authenticator_static_create) | **POST** /stages/authenticator/static/ | 
[**stages_authenticator_static_destroy**](StagesApi.md#stages_authenticator_static_destroy) | **DELETE** /stages/authenticator/static/{stage_uuid}/ | 
[**stages_authenticator_static_list**](StagesApi.md#stages_authenticator_static_list) | **GET** /stages/authenticator/static/ | 
[**stages_authenticator_static_partial_update**](StagesApi.md#stages_authenticator_static_partial_update) | **PATCH** /stages/authenticator/static/{stage_uuid}/ | 
[**stages_authenticator_static_retrieve**](StagesApi.md#stages_authenticator_static_retrieve) | **GET** /stages/authenticator/static/{stage_uuid}/ | 
[**stages_authenticator_static_update**](StagesApi.md#stages_authenticator_static_update) | **PUT** /stages/authenticator/static/{stage_uuid}/ | 
[**stages_authenticator_static_used_by_list**](StagesApi.md#stages_authenticator_static_used_by_list) | **GET** /stages/authenticator/static/{stage_uuid}/used_by/ | 
[**stages_authenticator_totp_create**](StagesApi.md#stages_authenticator_totp_create) | **POST** /stages/authenticator/totp/ | 
[**stages_authenticator_totp_destroy**](StagesApi.md#stages_authenticator_totp_destroy) | **DELETE** /stages/authenticator/totp/{stage_uuid}/ | 
[**stages_authenticator_totp_list**](StagesApi.md#stages_authenticator_totp_list) | **GET** /stages/authenticator/totp/ | 
[**stages_authenticator_totp_partial_update**](StagesApi.md#stages_authenticator_totp_partial_update) | **PATCH** /stages/authenticator/totp/{stage_uuid}/ | 
[**stages_authenticator_totp_retrieve**](StagesApi.md#stages_authenticator_totp_retrieve) | **GET** /stages/authenticator/totp/{stage_uuid}/ | 
[**stages_authenticator_totp_update**](StagesApi.md#stages_authenticator_totp_update) | **PUT** /stages/authenticator/totp/{stage_uuid}/ | 
[**stages_authenticator_totp_used_by_list**](StagesApi.md#stages_authenticator_totp_used_by_list) | **GET** /stages/authenticator/totp/{stage_uuid}/used_by/ | 
[**stages_authenticator_validate_create**](StagesApi.md#stages_authenticator_validate_create) | **POST** /stages/authenticator/validate/ | 
[**stages_authenticator_validate_destroy**](StagesApi.md#stages_authenticator_validate_destroy) | **DELETE** /stages/authenticator/validate/{stage_uuid}/ | 
[**stages_authenticator_validate_list**](StagesApi.md#stages_authenticator_validate_list) | **GET** /stages/authenticator/validate/ | 
[**stages_authenticator_validate_partial_update**](StagesApi.md#stages_authenticator_validate_partial_update) | **PATCH** /stages/authenticator/validate/{stage_uuid}/ | 
[**stages_authenticator_validate_retrieve**](StagesApi.md#stages_authenticator_validate_retrieve) | **GET** /stages/authenticator/validate/{stage_uuid}/ | 
[**stages_authenticator_validate_update**](StagesApi.md#stages_authenticator_validate_update) | **PUT** /stages/authenticator/validate/{stage_uuid}/ | 
[**stages_authenticator_validate_used_by_list**](StagesApi.md#stages_authenticator_validate_used_by_list) | **GET** /stages/authenticator/validate/{stage_uuid}/used_by/ | 
[**stages_authenticator_webauthn_create**](StagesApi.md#stages_authenticator_webauthn_create) | **POST** /stages/authenticator/webauthn/ | 
[**stages_authenticator_webauthn_destroy**](StagesApi.md#stages_authenticator_webauthn_destroy) | **DELETE** /stages/authenticator/webauthn/{stage_uuid}/ | 
[**stages_authenticator_webauthn_device_types_list**](StagesApi.md#stages_authenticator_webauthn_device_types_list) | **GET** /stages/authenticator/webauthn_device_types/ | 
[**stages_authenticator_webauthn_device_types_retrieve**](StagesApi.md#stages_authenticator_webauthn_device_types_retrieve) | **GET** /stages/authenticator/webauthn_device_types/{aaguid}/ | 
[**stages_authenticator_webauthn_list**](StagesApi.md#stages_authenticator_webauthn_list) | **GET** /stages/authenticator/webauthn/ | 
[**stages_authenticator_webauthn_partial_update**](StagesApi.md#stages_authenticator_webauthn_partial_update) | **PATCH** /stages/authenticator/webauthn/{stage_uuid}/ | 
[**stages_authenticator_webauthn_retrieve**](StagesApi.md#stages_authenticator_webauthn_retrieve) | **GET** /stages/authenticator/webauthn/{stage_uuid}/ | 
[**stages_authenticator_webauthn_update**](StagesApi.md#stages_authenticator_webauthn_update) | **PUT** /stages/authenticator/webauthn/{stage_uuid}/ | 
[**stages_authenticator_webauthn_used_by_list**](StagesApi.md#stages_authenticator_webauthn_used_by_list) | **GET** /stages/authenticator/webauthn/{stage_uuid}/used_by/ | 
[**stages_captcha_create**](StagesApi.md#stages_captcha_create) | **POST** /stages/captcha/ | 
[**stages_captcha_destroy**](StagesApi.md#stages_captcha_destroy) | **DELETE** /stages/captcha/{stage_uuid}/ | 
[**stages_captcha_list**](StagesApi.md#stages_captcha_list) | **GET** /stages/captcha/ | 
[**stages_captcha_partial_update**](StagesApi.md#stages_captcha_partial_update) | **PATCH** /stages/captcha/{stage_uuid}/ | 
[**stages_captcha_retrieve**](StagesApi.md#stages_captcha_retrieve) | **GET** /stages/captcha/{stage_uuid}/ | 
[**stages_captcha_update**](StagesApi.md#stages_captcha_update) | **PUT** /stages/captcha/{stage_uuid}/ | 
[**stages_captcha_used_by_list**](StagesApi.md#stages_captcha_used_by_list) | **GET** /stages/captcha/{stage_uuid}/used_by/ | 
[**stages_consent_create**](StagesApi.md#stages_consent_create) | **POST** /stages/consent/ | 
[**stages_consent_destroy**](StagesApi.md#stages_consent_destroy) | **DELETE** /stages/consent/{stage_uuid}/ | 
[**stages_consent_list**](StagesApi.md#stages_consent_list) | **GET** /stages/consent/ | 
[**stages_consent_partial_update**](StagesApi.md#stages_consent_partial_update) | **PATCH** /stages/consent/{stage_uuid}/ | 
[**stages_consent_retrieve**](StagesApi.md#stages_consent_retrieve) | **GET** /stages/consent/{stage_uuid}/ | 
[**stages_consent_update**](StagesApi.md#stages_consent_update) | **PUT** /stages/consent/{stage_uuid}/ | 
[**stages_consent_used_by_list**](StagesApi.md#stages_consent_used_by_list) | **GET** /stages/consent/{stage_uuid}/used_by/ | 
[**stages_deny_create**](StagesApi.md#stages_deny_create) | **POST** /stages/deny/ | 
[**stages_deny_destroy**](StagesApi.md#stages_deny_destroy) | **DELETE** /stages/deny/{stage_uuid}/ | 
[**stages_deny_list**](StagesApi.md#stages_deny_list) | **GET** /stages/deny/ | 
[**stages_deny_partial_update**](StagesApi.md#stages_deny_partial_update) | **PATCH** /stages/deny/{stage_uuid}/ | 
[**stages_deny_retrieve**](StagesApi.md#stages_deny_retrieve) | **GET** /stages/deny/{stage_uuid}/ | 
[**stages_deny_update**](StagesApi.md#stages_deny_update) | **PUT** /stages/deny/{stage_uuid}/ | 
[**stages_deny_used_by_list**](StagesApi.md#stages_deny_used_by_list) | **GET** /stages/deny/{stage_uuid}/used_by/ | 
[**stages_dummy_create**](StagesApi.md#stages_dummy_create) | **POST** /stages/dummy/ | 
[**stages_dummy_destroy**](StagesApi.md#stages_dummy_destroy) | **DELETE** /stages/dummy/{stage_uuid}/ | 
[**stages_dummy_list**](StagesApi.md#stages_dummy_list) | **GET** /stages/dummy/ | 
[**stages_dummy_partial_update**](StagesApi.md#stages_dummy_partial_update) | **PATCH** /stages/dummy/{stage_uuid}/ | 
[**stages_dummy_retrieve**](StagesApi.md#stages_dummy_retrieve) | **GET** /stages/dummy/{stage_uuid}/ | 
[**stages_dummy_update**](StagesApi.md#stages_dummy_update) | **PUT** /stages/dummy/{stage_uuid}/ | 
[**stages_dummy_used_by_list**](StagesApi.md#stages_dummy_used_by_list) | **GET** /stages/dummy/{stage_uuid}/used_by/ | 
[**stages_email_create**](StagesApi.md#stages_email_create) | **POST** /stages/email/ | 
[**stages_email_destroy**](StagesApi.md#stages_email_destroy) | **DELETE** /stages/email/{stage_uuid}/ | 
[**stages_email_list**](StagesApi.md#stages_email_list) | **GET** /stages/email/ | 
[**stages_email_partial_update**](StagesApi.md#stages_email_partial_update) | **PATCH** /stages/email/{stage_uuid}/ | 
[**stages_email_retrieve**](StagesApi.md#stages_email_retrieve) | **GET** /stages/email/{stage_uuid}/ | 
[**stages_email_templates_list**](StagesApi.md#stages_email_templates_list) | **GET** /stages/email/templates/ | 
[**stages_email_update**](StagesApi.md#stages_email_update) | **PUT** /stages/email/{stage_uuid}/ | 
[**stages_email_used_by_list**](StagesApi.md#stages_email_used_by_list) | **GET** /stages/email/{stage_uuid}/used_by/ | 
[**stages_identification_create**](StagesApi.md#stages_identification_create) | **POST** /stages/identification/ | 
[**stages_identification_destroy**](StagesApi.md#stages_identification_destroy) | **DELETE** /stages/identification/{stage_uuid}/ | 
[**stages_identification_list**](StagesApi.md#stages_identification_list) | **GET** /stages/identification/ | 
[**stages_identification_partial_update**](StagesApi.md#stages_identification_partial_update) | **PATCH** /stages/identification/{stage_uuid}/ | 
[**stages_identification_retrieve**](StagesApi.md#stages_identification_retrieve) | **GET** /stages/identification/{stage_uuid}/ | 
[**stages_identification_update**](StagesApi.md#stages_identification_update) | **PUT** /stages/identification/{stage_uuid}/ | 
[**stages_identification_used_by_list**](StagesApi.md#stages_identification_used_by_list) | **GET** /stages/identification/{stage_uuid}/used_by/ | 
[**stages_invitation_invitations_create**](StagesApi.md#stages_invitation_invitations_create) | **POST** /stages/invitation/invitations/ | 
[**stages_invitation_invitations_destroy**](StagesApi.md#stages_invitation_invitations_destroy) | **DELETE** /stages/invitation/invitations/{invite_uuid}/ | 
[**stages_invitation_invitations_list**](StagesApi.md#stages_invitation_invitations_list) | **GET** /stages/invitation/invitations/ | 
[**stages_invitation_invitations_partial_update**](StagesApi.md#stages_invitation_invitations_partial_update) | **PATCH** /stages/invitation/invitations/{invite_uuid}/ | 
[**stages_invitation_invitations_retrieve**](StagesApi.md#stages_invitation_invitations_retrieve) | **GET** /stages/invitation/invitations/{invite_uuid}/ | 
[**stages_invitation_invitations_update**](StagesApi.md#stages_invitation_invitations_update) | **PUT** /stages/invitation/invitations/{invite_uuid}/ | 
[**stages_invitation_invitations_used_by_list**](StagesApi.md#stages_invitation_invitations_used_by_list) | **GET** /stages/invitation/invitations/{invite_uuid}/used_by/ | 
[**stages_invitation_stages_create**](StagesApi.md#stages_invitation_stages_create) | **POST** /stages/invitation/stages/ | 
[**stages_invitation_stages_destroy**](StagesApi.md#stages_invitation_stages_destroy) | **DELETE** /stages/invitation/stages/{stage_uuid}/ | 
[**stages_invitation_stages_list**](StagesApi.md#stages_invitation_stages_list) | **GET** /stages/invitation/stages/ | 
[**stages_invitation_stages_partial_update**](StagesApi.md#stages_invitation_stages_partial_update) | **PATCH** /stages/invitation/stages/{stage_uuid}/ | 
[**stages_invitation_stages_retrieve**](StagesApi.md#stages_invitation_stages_retrieve) | **GET** /stages/invitation/stages/{stage_uuid}/ | 
[**stages_invitation_stages_update**](StagesApi.md#stages_invitation_stages_update) | **PUT** /stages/invitation/stages/{stage_uuid}/ | 
[**stages_invitation_stages_used_by_list**](StagesApi.md#stages_invitation_stages_used_by_list) | **GET** /stages/invitation/stages/{stage_uuid}/used_by/ | 
[**stages_password_create**](StagesApi.md#stages_password_create) | **POST** /stages/password/ | 
[**stages_password_destroy**](StagesApi.md#stages_password_destroy) | **DELETE** /stages/password/{stage_uuid}/ | 
[**stages_password_list**](StagesApi.md#stages_password_list) | **GET** /stages/password/ | 
[**stages_password_partial_update**](StagesApi.md#stages_password_partial_update) | **PATCH** /stages/password/{stage_uuid}/ | 
[**stages_password_retrieve**](StagesApi.md#stages_password_retrieve) | **GET** /stages/password/{stage_uuid}/ | 
[**stages_password_update**](StagesApi.md#stages_password_update) | **PUT** /stages/password/{stage_uuid}/ | 
[**stages_password_used_by_list**](StagesApi.md#stages_password_used_by_list) | **GET** /stages/password/{stage_uuid}/used_by/ | 
[**stages_prompt_prompts_create**](StagesApi.md#stages_prompt_prompts_create) | **POST** /stages/prompt/prompts/ | 
[**stages_prompt_prompts_destroy**](StagesApi.md#stages_prompt_prompts_destroy) | **DELETE** /stages/prompt/prompts/{prompt_uuid}/ | 
[**stages_prompt_prompts_list**](StagesApi.md#stages_prompt_prompts_list) | **GET** /stages/prompt/prompts/ | 
[**stages_prompt_prompts_partial_update**](StagesApi.md#stages_prompt_prompts_partial_update) | **PATCH** /stages/prompt/prompts/{prompt_uuid}/ | 
[**stages_prompt_prompts_preview_create**](StagesApi.md#stages_prompt_prompts_preview_create) | **POST** /stages/prompt/prompts/preview/ | 
[**stages_prompt_prompts_retrieve**](StagesApi.md#stages_prompt_prompts_retrieve) | **GET** /stages/prompt/prompts/{prompt_uuid}/ | 
[**stages_prompt_prompts_update**](StagesApi.md#stages_prompt_prompts_update) | **PUT** /stages/prompt/prompts/{prompt_uuid}/ | 
[**stages_prompt_prompts_used_by_list**](StagesApi.md#stages_prompt_prompts_used_by_list) | **GET** /stages/prompt/prompts/{prompt_uuid}/used_by/ | 
[**stages_prompt_stages_create**](StagesApi.md#stages_prompt_stages_create) | **POST** /stages/prompt/stages/ | 
[**stages_prompt_stages_destroy**](StagesApi.md#stages_prompt_stages_destroy) | **DELETE** /stages/prompt/stages/{stage_uuid}/ | 
[**stages_prompt_stages_list**](StagesApi.md#stages_prompt_stages_list) | **GET** /stages/prompt/stages/ | 
[**stages_prompt_stages_partial_update**](StagesApi.md#stages_prompt_stages_partial_update) | **PATCH** /stages/prompt/stages/{stage_uuid}/ | 
[**stages_prompt_stages_retrieve**](StagesApi.md#stages_prompt_stages_retrieve) | **GET** /stages/prompt/stages/{stage_uuid}/ | 
[**stages_prompt_stages_update**](StagesApi.md#stages_prompt_stages_update) | **PUT** /stages/prompt/stages/{stage_uuid}/ | 
[**stages_prompt_stages_used_by_list**](StagesApi.md#stages_prompt_stages_used_by_list) | **GET** /stages/prompt/stages/{stage_uuid}/used_by/ | 
[**stages_source_create**](StagesApi.md#stages_source_create) | **POST** /stages/source/ | 
[**stages_source_destroy**](StagesApi.md#stages_source_destroy) | **DELETE** /stages/source/{stage_uuid}/ | 
[**stages_source_list**](StagesApi.md#stages_source_list) | **GET** /stages/source/ | 
[**stages_source_partial_update**](StagesApi.md#stages_source_partial_update) | **PATCH** /stages/source/{stage_uuid}/ | 
[**stages_source_retrieve**](StagesApi.md#stages_source_retrieve) | **GET** /stages/source/{stage_uuid}/ | 
[**stages_source_update**](StagesApi.md#stages_source_update) | **PUT** /stages/source/{stage_uuid}/ | 
[**stages_source_used_by_list**](StagesApi.md#stages_source_used_by_list) | **GET** /stages/source/{stage_uuid}/used_by/ | 
[**stages_user_delete_create**](StagesApi.md#stages_user_delete_create) | **POST** /stages/user_delete/ | 
[**stages_user_delete_destroy**](StagesApi.md#stages_user_delete_destroy) | **DELETE** /stages/user_delete/{stage_uuid}/ | 
[**stages_user_delete_list**](StagesApi.md#stages_user_delete_list) | **GET** /stages/user_delete/ | 
[**stages_user_delete_partial_update**](StagesApi.md#stages_user_delete_partial_update) | **PATCH** /stages/user_delete/{stage_uuid}/ | 
[**stages_user_delete_retrieve**](StagesApi.md#stages_user_delete_retrieve) | **GET** /stages/user_delete/{stage_uuid}/ | 
[**stages_user_delete_update**](StagesApi.md#stages_user_delete_update) | **PUT** /stages/user_delete/{stage_uuid}/ | 
[**stages_user_delete_used_by_list**](StagesApi.md#stages_user_delete_used_by_list) | **GET** /stages/user_delete/{stage_uuid}/used_by/ | 
[**stages_user_login_create**](StagesApi.md#stages_user_login_create) | **POST** /stages/user_login/ | 
[**stages_user_login_destroy**](StagesApi.md#stages_user_login_destroy) | **DELETE** /stages/user_login/{stage_uuid}/ | 
[**stages_user_login_list**](StagesApi.md#stages_user_login_list) | **GET** /stages/user_login/ | 
[**stages_user_login_partial_update**](StagesApi.md#stages_user_login_partial_update) | **PATCH** /stages/user_login/{stage_uuid}/ | 
[**stages_user_login_retrieve**](StagesApi.md#stages_user_login_retrieve) | **GET** /stages/user_login/{stage_uuid}/ | 
[**stages_user_login_update**](StagesApi.md#stages_user_login_update) | **PUT** /stages/user_login/{stage_uuid}/ | 
[**stages_user_login_used_by_list**](StagesApi.md#stages_user_login_used_by_list) | **GET** /stages/user_login/{stage_uuid}/used_by/ | 
[**stages_user_logout_create**](StagesApi.md#stages_user_logout_create) | **POST** /stages/user_logout/ | 
[**stages_user_logout_destroy**](StagesApi.md#stages_user_logout_destroy) | **DELETE** /stages/user_logout/{stage_uuid}/ | 
[**stages_user_logout_list**](StagesApi.md#stages_user_logout_list) | **GET** /stages/user_logout/ | 
[**stages_user_logout_partial_update**](StagesApi.md#stages_user_logout_partial_update) | **PATCH** /stages/user_logout/{stage_uuid}/ | 
[**stages_user_logout_retrieve**](StagesApi.md#stages_user_logout_retrieve) | **GET** /stages/user_logout/{stage_uuid}/ | 
[**stages_user_logout_update**](StagesApi.md#stages_user_logout_update) | **PUT** /stages/user_logout/{stage_uuid}/ | 
[**stages_user_logout_used_by_list**](StagesApi.md#stages_user_logout_used_by_list) | **GET** /stages/user_logout/{stage_uuid}/used_by/ | 
[**stages_user_write_create**](StagesApi.md#stages_user_write_create) | **POST** /stages/user_write/ | 
[**stages_user_write_destroy**](StagesApi.md#stages_user_write_destroy) | **DELETE** /stages/user_write/{stage_uuid}/ | 
[**stages_user_write_list**](StagesApi.md#stages_user_write_list) | **GET** /stages/user_write/ | 
[**stages_user_write_partial_update**](StagesApi.md#stages_user_write_partial_update) | **PATCH** /stages/user_write/{stage_uuid}/ | 
[**stages_user_write_retrieve**](StagesApi.md#stages_user_write_retrieve) | **GET** /stages/user_write/{stage_uuid}/ | 
[**stages_user_write_update**](StagesApi.md#stages_user_write_update) | **PUT** /stages/user_write/{stage_uuid}/ | 
[**stages_user_write_used_by_list**](StagesApi.md#stages_user_write_used_by_list) | **GET** /stages/user_write/{stage_uuid}/used_by/ | 


# **stages_all_destroy**
> stages_all_destroy(stage_uuid)



Stage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this stage.

    try:
        api_instance.stages_all_destroy(stage_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_all_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this stage. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_all_list**
> PaginatedStageList stages_all_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)



Stage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_stage_list import PaginatedStageList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.stages_all_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of StagesApi->stages_all_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_all_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedStageList**](PaginatedStageList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_all_retrieve**
> Stage stages_all_retrieve(stage_uuid)



Stage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.stage import Stage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this stage.

    try:
        api_response = api_instance.stages_all_retrieve(stage_uuid)
        print("The response of StagesApi->stages_all_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_all_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this stage. | 

### Return type

[**Stage**](Stage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_all_types_list**
> List[TypeCreate] stages_all_types_list()



Get all creatable types

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.type_create import TypeCreate
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)

    try:
        api_response = api_instance.stages_all_types_list()
        print("The response of StagesApi->stages_all_types_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_all_types_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TypeCreate]**](TypeCreate.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_all_used_by_list**
> List[UsedBy] stages_all_used_by_list(stage_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this stage.

    try:
        api_response = api_instance.stages_all_used_by_list(stage_uuid)
        print("The response of StagesApi->stages_all_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_all_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this stage. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_all_user_settings_list**
> List[UserSetting] stages_all_user_settings_list()



Get all stages the user can configure

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_setting import UserSetting
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)

    try:
        api_response = api_instance.stages_all_user_settings_list()
        print("The response of StagesApi->stages_all_user_settings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_all_user_settings_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UserSetting]**](UserSetting.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_duo_create**
> AuthenticatorDuoStage stages_authenticator_duo_create(authenticator_duo_stage_request)



AuthenticatorDuoStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_duo_stage import AuthenticatorDuoStage
from authentik_openapi.models.authenticator_duo_stage_request import AuthenticatorDuoStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    authenticator_duo_stage_request = authentik_openapi.AuthenticatorDuoStageRequest() # AuthenticatorDuoStageRequest | 

    try:
        api_response = api_instance.stages_authenticator_duo_create(authenticator_duo_stage_request)
        print("The response of StagesApi->stages_authenticator_duo_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_duo_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_duo_stage_request** | [**AuthenticatorDuoStageRequest**](AuthenticatorDuoStageRequest.md)|  | 

### Return type

[**AuthenticatorDuoStage**](AuthenticatorDuoStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_duo_destroy**
> stages_authenticator_duo_destroy(stage_uuid)



AuthenticatorDuoStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Duo Authenticator Setup Stage.

    try:
        api_instance.stages_authenticator_duo_destroy(stage_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_duo_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Duo Authenticator Setup Stage. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_duo_enrollment_status_create**
> DuoDeviceEnrollmentStatus stages_authenticator_duo_enrollment_status_create(stage_uuid)



Check enrollment status of user details in current session

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.duo_device_enrollment_status import DuoDeviceEnrollmentStatus
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Duo Authenticator Setup Stage.

    try:
        api_response = api_instance.stages_authenticator_duo_enrollment_status_create(stage_uuid)
        print("The response of StagesApi->stages_authenticator_duo_enrollment_status_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_duo_enrollment_status_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Duo Authenticator Setup Stage. | 

### Return type

[**DuoDeviceEnrollmentStatus**](DuoDeviceEnrollmentStatus.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_duo_import_device_manual_create**
> stages_authenticator_duo_import_device_manual_create(stage_uuid, authenticator_duo_stage_manual_device_import_request)



Import duo devices into authentik

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_duo_stage_manual_device_import_request import AuthenticatorDuoStageManualDeviceImportRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Duo Authenticator Setup Stage.
    authenticator_duo_stage_manual_device_import_request = authentik_openapi.AuthenticatorDuoStageManualDeviceImportRequest() # AuthenticatorDuoStageManualDeviceImportRequest | 

    try:
        api_instance.stages_authenticator_duo_import_device_manual_create(stage_uuid, authenticator_duo_stage_manual_device_import_request)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_duo_import_device_manual_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Duo Authenticator Setup Stage. | 
 **authenticator_duo_stage_manual_device_import_request** | [**AuthenticatorDuoStageManualDeviceImportRequest**](AuthenticatorDuoStageManualDeviceImportRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Enrollment successful |  -  |
**400** | Bad request |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_duo_import_devices_automatic_create**
> AuthenticatorDuoStageDeviceImportResponse stages_authenticator_duo_import_devices_automatic_create(stage_uuid)



Import duo devices into authentik

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_duo_stage_device_import_response import AuthenticatorDuoStageDeviceImportResponse
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Duo Authenticator Setup Stage.

    try:
        api_response = api_instance.stages_authenticator_duo_import_devices_automatic_create(stage_uuid)
        print("The response of StagesApi->stages_authenticator_duo_import_devices_automatic_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_duo_import_devices_automatic_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Duo Authenticator Setup Stage. | 

### Return type

[**AuthenticatorDuoStageDeviceImportResponse**](AuthenticatorDuoStageDeviceImportResponse.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_duo_list**
> PaginatedAuthenticatorDuoStageList stages_authenticator_duo_list(api_hostname=api_hostname, client_id=client_id, configure_flow=configure_flow, name=name, ordering=ordering, page=page, page_size=page_size, search=search)



AuthenticatorDuoStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_authenticator_duo_stage_list import PaginatedAuthenticatorDuoStageList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    api_hostname = 'api_hostname_example' # str |  (optional)
    client_id = 'client_id_example' # str |  (optional)
    configure_flow = 'configure_flow_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.stages_authenticator_duo_list(api_hostname=api_hostname, client_id=client_id, configure_flow=configure_flow, name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of StagesApi->stages_authenticator_duo_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_duo_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_hostname** | **str**|  | [optional] 
 **client_id** | **str**|  | [optional] 
 **configure_flow** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedAuthenticatorDuoStageList**](PaginatedAuthenticatorDuoStageList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_duo_partial_update**
> AuthenticatorDuoStage stages_authenticator_duo_partial_update(stage_uuid, patched_authenticator_duo_stage_request=patched_authenticator_duo_stage_request)



AuthenticatorDuoStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_duo_stage import AuthenticatorDuoStage
from authentik_openapi.models.patched_authenticator_duo_stage_request import PatchedAuthenticatorDuoStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Duo Authenticator Setup Stage.
    patched_authenticator_duo_stage_request = authentik_openapi.PatchedAuthenticatorDuoStageRequest() # PatchedAuthenticatorDuoStageRequest |  (optional)

    try:
        api_response = api_instance.stages_authenticator_duo_partial_update(stage_uuid, patched_authenticator_duo_stage_request=patched_authenticator_duo_stage_request)
        print("The response of StagesApi->stages_authenticator_duo_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_duo_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Duo Authenticator Setup Stage. | 
 **patched_authenticator_duo_stage_request** | [**PatchedAuthenticatorDuoStageRequest**](PatchedAuthenticatorDuoStageRequest.md)|  | [optional] 

### Return type

[**AuthenticatorDuoStage**](AuthenticatorDuoStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_duo_retrieve**
> AuthenticatorDuoStage stages_authenticator_duo_retrieve(stage_uuid)



AuthenticatorDuoStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_duo_stage import AuthenticatorDuoStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Duo Authenticator Setup Stage.

    try:
        api_response = api_instance.stages_authenticator_duo_retrieve(stage_uuid)
        print("The response of StagesApi->stages_authenticator_duo_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_duo_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Duo Authenticator Setup Stage. | 

### Return type

[**AuthenticatorDuoStage**](AuthenticatorDuoStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_duo_update**
> AuthenticatorDuoStage stages_authenticator_duo_update(stage_uuid, authenticator_duo_stage_request)



AuthenticatorDuoStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_duo_stage import AuthenticatorDuoStage
from authentik_openapi.models.authenticator_duo_stage_request import AuthenticatorDuoStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Duo Authenticator Setup Stage.
    authenticator_duo_stage_request = authentik_openapi.AuthenticatorDuoStageRequest() # AuthenticatorDuoStageRequest | 

    try:
        api_response = api_instance.stages_authenticator_duo_update(stage_uuid, authenticator_duo_stage_request)
        print("The response of StagesApi->stages_authenticator_duo_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_duo_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Duo Authenticator Setup Stage. | 
 **authenticator_duo_stage_request** | [**AuthenticatorDuoStageRequest**](AuthenticatorDuoStageRequest.md)|  | 

### Return type

[**AuthenticatorDuoStage**](AuthenticatorDuoStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_duo_used_by_list**
> List[UsedBy] stages_authenticator_duo_used_by_list(stage_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Duo Authenticator Setup Stage.

    try:
        api_response = api_instance.stages_authenticator_duo_used_by_list(stage_uuid)
        print("The response of StagesApi->stages_authenticator_duo_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_duo_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Duo Authenticator Setup Stage. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_sms_create**
> AuthenticatorSMSStage stages_authenticator_sms_create(authenticator_sms_stage_request)



AuthenticatorSMSStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_sms_stage import AuthenticatorSMSStage
from authentik_openapi.models.authenticator_sms_stage_request import AuthenticatorSMSStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    authenticator_sms_stage_request = authentik_openapi.AuthenticatorSMSStageRequest() # AuthenticatorSMSStageRequest | 

    try:
        api_response = api_instance.stages_authenticator_sms_create(authenticator_sms_stage_request)
        print("The response of StagesApi->stages_authenticator_sms_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_sms_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_sms_stage_request** | [**AuthenticatorSMSStageRequest**](AuthenticatorSMSStageRequest.md)|  | 

### Return type

[**AuthenticatorSMSStage**](AuthenticatorSMSStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_sms_destroy**
> stages_authenticator_sms_destroy(stage_uuid)



AuthenticatorSMSStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this SMS Authenticator Setup Stage.

    try:
        api_instance.stages_authenticator_sms_destroy(stage_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_sms_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this SMS Authenticator Setup Stage. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_sms_list**
> PaginatedAuthenticatorSMSStageList stages_authenticator_sms_list(account_sid=account_sid, auth=auth, auth_password=auth_password, auth_type=auth_type, configure_flow=configure_flow, friendly_name=friendly_name, from_number=from_number, mapping=mapping, name=name, ordering=ordering, page=page, page_size=page_size, provider=provider, search=search, stage_uuid=stage_uuid, verify_only=verify_only)



AuthenticatorSMSStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_authenticator_sms_stage_list import PaginatedAuthenticatorSMSStageList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    account_sid = 'account_sid_example' # str |  (optional)
    auth = 'auth_example' # str |  (optional)
    auth_password = 'auth_password_example' # str |  (optional)
    auth_type = 'auth_type_example' # str |  (optional)
    configure_flow = 'configure_flow_example' # str |  (optional)
    friendly_name = 'friendly_name_example' # str |  (optional)
    from_number = 'from_number_example' # str |  (optional)
    mapping = 'mapping_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    provider = 'provider_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)
    stage_uuid = 'stage_uuid_example' # str |  (optional)
    verify_only = True # bool |  (optional)

    try:
        api_response = api_instance.stages_authenticator_sms_list(account_sid=account_sid, auth=auth, auth_password=auth_password, auth_type=auth_type, configure_flow=configure_flow, friendly_name=friendly_name, from_number=from_number, mapping=mapping, name=name, ordering=ordering, page=page, page_size=page_size, provider=provider, search=search, stage_uuid=stage_uuid, verify_only=verify_only)
        print("The response of StagesApi->stages_authenticator_sms_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_sms_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**|  | [optional] 
 **auth** | **str**|  | [optional] 
 **auth_password** | **str**|  | [optional] 
 **auth_type** | **str**|  | [optional] 
 **configure_flow** | **str**|  | [optional] 
 **friendly_name** | **str**|  | [optional] 
 **from_number** | **str**|  | [optional] 
 **mapping** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **provider** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **stage_uuid** | **str**|  | [optional] 
 **verify_only** | **bool**|  | [optional] 

### Return type

[**PaginatedAuthenticatorSMSStageList**](PaginatedAuthenticatorSMSStageList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_sms_partial_update**
> AuthenticatorSMSStage stages_authenticator_sms_partial_update(stage_uuid, patched_authenticator_sms_stage_request=patched_authenticator_sms_stage_request)



AuthenticatorSMSStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_sms_stage import AuthenticatorSMSStage
from authentik_openapi.models.patched_authenticator_sms_stage_request import PatchedAuthenticatorSMSStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this SMS Authenticator Setup Stage.
    patched_authenticator_sms_stage_request = authentik_openapi.PatchedAuthenticatorSMSStageRequest() # PatchedAuthenticatorSMSStageRequest |  (optional)

    try:
        api_response = api_instance.stages_authenticator_sms_partial_update(stage_uuid, patched_authenticator_sms_stage_request=patched_authenticator_sms_stage_request)
        print("The response of StagesApi->stages_authenticator_sms_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_sms_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this SMS Authenticator Setup Stage. | 
 **patched_authenticator_sms_stage_request** | [**PatchedAuthenticatorSMSStageRequest**](PatchedAuthenticatorSMSStageRequest.md)|  | [optional] 

### Return type

[**AuthenticatorSMSStage**](AuthenticatorSMSStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_sms_retrieve**
> AuthenticatorSMSStage stages_authenticator_sms_retrieve(stage_uuid)



AuthenticatorSMSStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_sms_stage import AuthenticatorSMSStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this SMS Authenticator Setup Stage.

    try:
        api_response = api_instance.stages_authenticator_sms_retrieve(stage_uuid)
        print("The response of StagesApi->stages_authenticator_sms_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_sms_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this SMS Authenticator Setup Stage. | 

### Return type

[**AuthenticatorSMSStage**](AuthenticatorSMSStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_sms_update**
> AuthenticatorSMSStage stages_authenticator_sms_update(stage_uuid, authenticator_sms_stage_request)



AuthenticatorSMSStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_sms_stage import AuthenticatorSMSStage
from authentik_openapi.models.authenticator_sms_stage_request import AuthenticatorSMSStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this SMS Authenticator Setup Stage.
    authenticator_sms_stage_request = authentik_openapi.AuthenticatorSMSStageRequest() # AuthenticatorSMSStageRequest | 

    try:
        api_response = api_instance.stages_authenticator_sms_update(stage_uuid, authenticator_sms_stage_request)
        print("The response of StagesApi->stages_authenticator_sms_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_sms_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this SMS Authenticator Setup Stage. | 
 **authenticator_sms_stage_request** | [**AuthenticatorSMSStageRequest**](AuthenticatorSMSStageRequest.md)|  | 

### Return type

[**AuthenticatorSMSStage**](AuthenticatorSMSStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_sms_used_by_list**
> List[UsedBy] stages_authenticator_sms_used_by_list(stage_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this SMS Authenticator Setup Stage.

    try:
        api_response = api_instance.stages_authenticator_sms_used_by_list(stage_uuid)
        print("The response of StagesApi->stages_authenticator_sms_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_sms_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this SMS Authenticator Setup Stage. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_static_create**
> AuthenticatorStaticStage stages_authenticator_static_create(authenticator_static_stage_request)



AuthenticatorStaticStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_static_stage import AuthenticatorStaticStage
from authentik_openapi.models.authenticator_static_stage_request import AuthenticatorStaticStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    authenticator_static_stage_request = authentik_openapi.AuthenticatorStaticStageRequest() # AuthenticatorStaticStageRequest | 

    try:
        api_response = api_instance.stages_authenticator_static_create(authenticator_static_stage_request)
        print("The response of StagesApi->stages_authenticator_static_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_static_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_static_stage_request** | [**AuthenticatorStaticStageRequest**](AuthenticatorStaticStageRequest.md)|  | 

### Return type

[**AuthenticatorStaticStage**](AuthenticatorStaticStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_static_destroy**
> stages_authenticator_static_destroy(stage_uuid)



AuthenticatorStaticStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Static Authenticator Setup Stage.

    try:
        api_instance.stages_authenticator_static_destroy(stage_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_static_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Static Authenticator Setup Stage. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_static_list**
> PaginatedAuthenticatorStaticStageList stages_authenticator_static_list(configure_flow=configure_flow, friendly_name=friendly_name, name=name, ordering=ordering, page=page, page_size=page_size, search=search, stage_uuid=stage_uuid, token_count=token_count, token_length=token_length)



AuthenticatorStaticStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_authenticator_static_stage_list import PaginatedAuthenticatorStaticStageList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    configure_flow = 'configure_flow_example' # str |  (optional)
    friendly_name = 'friendly_name_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    stage_uuid = 'stage_uuid_example' # str |  (optional)
    token_count = 56 # int |  (optional)
    token_length = 56 # int |  (optional)

    try:
        api_response = api_instance.stages_authenticator_static_list(configure_flow=configure_flow, friendly_name=friendly_name, name=name, ordering=ordering, page=page, page_size=page_size, search=search, stage_uuid=stage_uuid, token_count=token_count, token_length=token_length)
        print("The response of StagesApi->stages_authenticator_static_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_static_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configure_flow** | **str**|  | [optional] 
 **friendly_name** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **stage_uuid** | **str**|  | [optional] 
 **token_count** | **int**|  | [optional] 
 **token_length** | **int**|  | [optional] 

### Return type

[**PaginatedAuthenticatorStaticStageList**](PaginatedAuthenticatorStaticStageList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_static_partial_update**
> AuthenticatorStaticStage stages_authenticator_static_partial_update(stage_uuid, patched_authenticator_static_stage_request=patched_authenticator_static_stage_request)



AuthenticatorStaticStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_static_stage import AuthenticatorStaticStage
from authentik_openapi.models.patched_authenticator_static_stage_request import PatchedAuthenticatorStaticStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Static Authenticator Setup Stage.
    patched_authenticator_static_stage_request = authentik_openapi.PatchedAuthenticatorStaticStageRequest() # PatchedAuthenticatorStaticStageRequest |  (optional)

    try:
        api_response = api_instance.stages_authenticator_static_partial_update(stage_uuid, patched_authenticator_static_stage_request=patched_authenticator_static_stage_request)
        print("The response of StagesApi->stages_authenticator_static_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_static_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Static Authenticator Setup Stage. | 
 **patched_authenticator_static_stage_request** | [**PatchedAuthenticatorStaticStageRequest**](PatchedAuthenticatorStaticStageRequest.md)|  | [optional] 

### Return type

[**AuthenticatorStaticStage**](AuthenticatorStaticStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_static_retrieve**
> AuthenticatorStaticStage stages_authenticator_static_retrieve(stage_uuid)



AuthenticatorStaticStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_static_stage import AuthenticatorStaticStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Static Authenticator Setup Stage.

    try:
        api_response = api_instance.stages_authenticator_static_retrieve(stage_uuid)
        print("The response of StagesApi->stages_authenticator_static_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_static_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Static Authenticator Setup Stage. | 

### Return type

[**AuthenticatorStaticStage**](AuthenticatorStaticStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_static_update**
> AuthenticatorStaticStage stages_authenticator_static_update(stage_uuid, authenticator_static_stage_request)



AuthenticatorStaticStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_static_stage import AuthenticatorStaticStage
from authentik_openapi.models.authenticator_static_stage_request import AuthenticatorStaticStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Static Authenticator Setup Stage.
    authenticator_static_stage_request = authentik_openapi.AuthenticatorStaticStageRequest() # AuthenticatorStaticStageRequest | 

    try:
        api_response = api_instance.stages_authenticator_static_update(stage_uuid, authenticator_static_stage_request)
        print("The response of StagesApi->stages_authenticator_static_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_static_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Static Authenticator Setup Stage. | 
 **authenticator_static_stage_request** | [**AuthenticatorStaticStageRequest**](AuthenticatorStaticStageRequest.md)|  | 

### Return type

[**AuthenticatorStaticStage**](AuthenticatorStaticStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_static_used_by_list**
> List[UsedBy] stages_authenticator_static_used_by_list(stage_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Static Authenticator Setup Stage.

    try:
        api_response = api_instance.stages_authenticator_static_used_by_list(stage_uuid)
        print("The response of StagesApi->stages_authenticator_static_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_static_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Static Authenticator Setup Stage. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_totp_create**
> AuthenticatorTOTPStage stages_authenticator_totp_create(authenticator_totp_stage_request)



AuthenticatorTOTPStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_totp_stage import AuthenticatorTOTPStage
from authentik_openapi.models.authenticator_totp_stage_request import AuthenticatorTOTPStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    authenticator_totp_stage_request = authentik_openapi.AuthenticatorTOTPStageRequest() # AuthenticatorTOTPStageRequest | 

    try:
        api_response = api_instance.stages_authenticator_totp_create(authenticator_totp_stage_request)
        print("The response of StagesApi->stages_authenticator_totp_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_totp_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_totp_stage_request** | [**AuthenticatorTOTPStageRequest**](AuthenticatorTOTPStageRequest.md)|  | 

### Return type

[**AuthenticatorTOTPStage**](AuthenticatorTOTPStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_totp_destroy**
> stages_authenticator_totp_destroy(stage_uuid)



AuthenticatorTOTPStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this TOTP Authenticator Setup Stage.

    try:
        api_instance.stages_authenticator_totp_destroy(stage_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_totp_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this TOTP Authenticator Setup Stage. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_totp_list**
> PaginatedAuthenticatorTOTPStageList stages_authenticator_totp_list(configure_flow=configure_flow, digits=digits, friendly_name=friendly_name, name=name, ordering=ordering, page=page, page_size=page_size, search=search, stage_uuid=stage_uuid)



AuthenticatorTOTPStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_authenticator_totp_stage_list import PaginatedAuthenticatorTOTPStageList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    configure_flow = 'configure_flow_example' # str |  (optional)
    digits = 'digits_example' # str |  (optional)
    friendly_name = 'friendly_name_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    stage_uuid = 'stage_uuid_example' # str |  (optional)

    try:
        api_response = api_instance.stages_authenticator_totp_list(configure_flow=configure_flow, digits=digits, friendly_name=friendly_name, name=name, ordering=ordering, page=page, page_size=page_size, search=search, stage_uuid=stage_uuid)
        print("The response of StagesApi->stages_authenticator_totp_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_totp_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configure_flow** | **str**|  | [optional] 
 **digits** | **str**|  | [optional] 
 **friendly_name** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **stage_uuid** | **str**|  | [optional] 

### Return type

[**PaginatedAuthenticatorTOTPStageList**](PaginatedAuthenticatorTOTPStageList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_totp_partial_update**
> AuthenticatorTOTPStage stages_authenticator_totp_partial_update(stage_uuid, patched_authenticator_totp_stage_request=patched_authenticator_totp_stage_request)



AuthenticatorTOTPStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_totp_stage import AuthenticatorTOTPStage
from authentik_openapi.models.patched_authenticator_totp_stage_request import PatchedAuthenticatorTOTPStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this TOTP Authenticator Setup Stage.
    patched_authenticator_totp_stage_request = authentik_openapi.PatchedAuthenticatorTOTPStageRequest() # PatchedAuthenticatorTOTPStageRequest |  (optional)

    try:
        api_response = api_instance.stages_authenticator_totp_partial_update(stage_uuid, patched_authenticator_totp_stage_request=patched_authenticator_totp_stage_request)
        print("The response of StagesApi->stages_authenticator_totp_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_totp_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this TOTP Authenticator Setup Stage. | 
 **patched_authenticator_totp_stage_request** | [**PatchedAuthenticatorTOTPStageRequest**](PatchedAuthenticatorTOTPStageRequest.md)|  | [optional] 

### Return type

[**AuthenticatorTOTPStage**](AuthenticatorTOTPStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_totp_retrieve**
> AuthenticatorTOTPStage stages_authenticator_totp_retrieve(stage_uuid)



AuthenticatorTOTPStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_totp_stage import AuthenticatorTOTPStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this TOTP Authenticator Setup Stage.

    try:
        api_response = api_instance.stages_authenticator_totp_retrieve(stage_uuid)
        print("The response of StagesApi->stages_authenticator_totp_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_totp_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this TOTP Authenticator Setup Stage. | 

### Return type

[**AuthenticatorTOTPStage**](AuthenticatorTOTPStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_totp_update**
> AuthenticatorTOTPStage stages_authenticator_totp_update(stage_uuid, authenticator_totp_stage_request)



AuthenticatorTOTPStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_totp_stage import AuthenticatorTOTPStage
from authentik_openapi.models.authenticator_totp_stage_request import AuthenticatorTOTPStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this TOTP Authenticator Setup Stage.
    authenticator_totp_stage_request = authentik_openapi.AuthenticatorTOTPStageRequest() # AuthenticatorTOTPStageRequest | 

    try:
        api_response = api_instance.stages_authenticator_totp_update(stage_uuid, authenticator_totp_stage_request)
        print("The response of StagesApi->stages_authenticator_totp_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_totp_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this TOTP Authenticator Setup Stage. | 
 **authenticator_totp_stage_request** | [**AuthenticatorTOTPStageRequest**](AuthenticatorTOTPStageRequest.md)|  | 

### Return type

[**AuthenticatorTOTPStage**](AuthenticatorTOTPStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_totp_used_by_list**
> List[UsedBy] stages_authenticator_totp_used_by_list(stage_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this TOTP Authenticator Setup Stage.

    try:
        api_response = api_instance.stages_authenticator_totp_used_by_list(stage_uuid)
        print("The response of StagesApi->stages_authenticator_totp_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_totp_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this TOTP Authenticator Setup Stage. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_validate_create**
> AuthenticatorValidateStage stages_authenticator_validate_create(authenticator_validate_stage_request)



AuthenticatorValidateStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_validate_stage import AuthenticatorValidateStage
from authentik_openapi.models.authenticator_validate_stage_request import AuthenticatorValidateStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    authenticator_validate_stage_request = authentik_openapi.AuthenticatorValidateStageRequest() # AuthenticatorValidateStageRequest | 

    try:
        api_response = api_instance.stages_authenticator_validate_create(authenticator_validate_stage_request)
        print("The response of StagesApi->stages_authenticator_validate_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_validate_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_validate_stage_request** | [**AuthenticatorValidateStageRequest**](AuthenticatorValidateStageRequest.md)|  | 

### Return type

[**AuthenticatorValidateStage**](AuthenticatorValidateStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_validate_destroy**
> stages_authenticator_validate_destroy(stage_uuid)



AuthenticatorValidateStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Authenticator Validation Stage.

    try:
        api_instance.stages_authenticator_validate_destroy(stage_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_validate_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Authenticator Validation Stage. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_validate_list**
> PaginatedAuthenticatorValidateStageList stages_authenticator_validate_list(configuration_stages=configuration_stages, name=name, not_configured_action=not_configured_action, ordering=ordering, page=page, page_size=page_size, search=search)



AuthenticatorValidateStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_authenticator_validate_stage_list import PaginatedAuthenticatorValidateStageList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    configuration_stages = ['configuration_stages_example'] # List[str] |  (optional)
    name = 'name_example' # str |  (optional)
    not_configured_action = 'not_configured_action_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.stages_authenticator_validate_list(configuration_stages=configuration_stages, name=name, not_configured_action=not_configured_action, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of StagesApi->stages_authenticator_validate_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_validate_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_stages** | [**List[str]**](str.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **not_configured_action** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedAuthenticatorValidateStageList**](PaginatedAuthenticatorValidateStageList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_validate_partial_update**
> AuthenticatorValidateStage stages_authenticator_validate_partial_update(stage_uuid, patched_authenticator_validate_stage_request=patched_authenticator_validate_stage_request)



AuthenticatorValidateStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_validate_stage import AuthenticatorValidateStage
from authentik_openapi.models.patched_authenticator_validate_stage_request import PatchedAuthenticatorValidateStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Authenticator Validation Stage.
    patched_authenticator_validate_stage_request = authentik_openapi.PatchedAuthenticatorValidateStageRequest() # PatchedAuthenticatorValidateStageRequest |  (optional)

    try:
        api_response = api_instance.stages_authenticator_validate_partial_update(stage_uuid, patched_authenticator_validate_stage_request=patched_authenticator_validate_stage_request)
        print("The response of StagesApi->stages_authenticator_validate_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_validate_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Authenticator Validation Stage. | 
 **patched_authenticator_validate_stage_request** | [**PatchedAuthenticatorValidateStageRequest**](PatchedAuthenticatorValidateStageRequest.md)|  | [optional] 

### Return type

[**AuthenticatorValidateStage**](AuthenticatorValidateStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_validate_retrieve**
> AuthenticatorValidateStage stages_authenticator_validate_retrieve(stage_uuid)



AuthenticatorValidateStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_validate_stage import AuthenticatorValidateStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Authenticator Validation Stage.

    try:
        api_response = api_instance.stages_authenticator_validate_retrieve(stage_uuid)
        print("The response of StagesApi->stages_authenticator_validate_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_validate_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Authenticator Validation Stage. | 

### Return type

[**AuthenticatorValidateStage**](AuthenticatorValidateStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_validate_update**
> AuthenticatorValidateStage stages_authenticator_validate_update(stage_uuid, authenticator_validate_stage_request)



AuthenticatorValidateStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_validate_stage import AuthenticatorValidateStage
from authentik_openapi.models.authenticator_validate_stage_request import AuthenticatorValidateStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Authenticator Validation Stage.
    authenticator_validate_stage_request = authentik_openapi.AuthenticatorValidateStageRequest() # AuthenticatorValidateStageRequest | 

    try:
        api_response = api_instance.stages_authenticator_validate_update(stage_uuid, authenticator_validate_stage_request)
        print("The response of StagesApi->stages_authenticator_validate_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_validate_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Authenticator Validation Stage. | 
 **authenticator_validate_stage_request** | [**AuthenticatorValidateStageRequest**](AuthenticatorValidateStageRequest.md)|  | 

### Return type

[**AuthenticatorValidateStage**](AuthenticatorValidateStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_validate_used_by_list**
> List[UsedBy] stages_authenticator_validate_used_by_list(stage_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Authenticator Validation Stage.

    try:
        api_response = api_instance.stages_authenticator_validate_used_by_list(stage_uuid)
        print("The response of StagesApi->stages_authenticator_validate_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_validate_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Authenticator Validation Stage. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_webauthn_create**
> AuthenticatorWebAuthnStage stages_authenticator_webauthn_create(authenticator_web_authn_stage_request)



AuthenticatorWebAuthnStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_web_authn_stage import AuthenticatorWebAuthnStage
from authentik_openapi.models.authenticator_web_authn_stage_request import AuthenticatorWebAuthnStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    authenticator_web_authn_stage_request = authentik_openapi.AuthenticatorWebAuthnStageRequest() # AuthenticatorWebAuthnStageRequest | 

    try:
        api_response = api_instance.stages_authenticator_webauthn_create(authenticator_web_authn_stage_request)
        print("The response of StagesApi->stages_authenticator_webauthn_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_webauthn_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_web_authn_stage_request** | [**AuthenticatorWebAuthnStageRequest**](AuthenticatorWebAuthnStageRequest.md)|  | 

### Return type

[**AuthenticatorWebAuthnStage**](AuthenticatorWebAuthnStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_webauthn_destroy**
> stages_authenticator_webauthn_destroy(stage_uuid)



AuthenticatorWebAuthnStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this WebAuthn Authenticator Setup Stage.

    try:
        api_instance.stages_authenticator_webauthn_destroy(stage_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_webauthn_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this WebAuthn Authenticator Setup Stage. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_webauthn_device_types_list**
> PaginatedWebAuthnDeviceTypeList stages_authenticator_webauthn_device_types_list(aaguid=aaguid, description=description, icon=icon, ordering=ordering, page=page, page_size=page_size, search=search)



WebAuthnDeviceType Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_web_authn_device_type_list import PaginatedWebAuthnDeviceTypeList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    aaguid = 'aaguid_example' # str |  (optional)
    description = 'description_example' # str |  (optional)
    icon = 'icon_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.stages_authenticator_webauthn_device_types_list(aaguid=aaguid, description=description, icon=icon, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of StagesApi->stages_authenticator_webauthn_device_types_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_webauthn_device_types_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aaguid** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **icon** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedWebAuthnDeviceTypeList**](PaginatedWebAuthnDeviceTypeList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_webauthn_device_types_retrieve**
> WebAuthnDeviceType stages_authenticator_webauthn_device_types_retrieve(aaguid)



WebAuthnDeviceType Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.web_authn_device_type import WebAuthnDeviceType
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    aaguid = 'aaguid_example' # str | A UUID string identifying this WebAuthn Device type.

    try:
        api_response = api_instance.stages_authenticator_webauthn_device_types_retrieve(aaguid)
        print("The response of StagesApi->stages_authenticator_webauthn_device_types_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_webauthn_device_types_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aaguid** | **str**| A UUID string identifying this WebAuthn Device type. | 

### Return type

[**WebAuthnDeviceType**](WebAuthnDeviceType.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_webauthn_list**
> PaginatedAuthenticatorWebAuthnStageList stages_authenticator_webauthn_list(authenticator_attachment=authenticator_attachment, configure_flow=configure_flow, device_type_restrictions=device_type_restrictions, friendly_name=friendly_name, name=name, ordering=ordering, page=page, page_size=page_size, resident_key_requirement=resident_key_requirement, search=search, stage_uuid=stage_uuid, user_verification=user_verification)



AuthenticatorWebAuthnStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_authenticator_web_authn_stage_list import PaginatedAuthenticatorWebAuthnStageList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    authenticator_attachment = 'authenticator_attachment_example' # str |  (optional)
    configure_flow = 'configure_flow_example' # str |  (optional)
    device_type_restrictions = ['device_type_restrictions_example'] # List[str] |  (optional)
    friendly_name = 'friendly_name_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    resident_key_requirement = 'resident_key_requirement_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)
    stage_uuid = 'stage_uuid_example' # str |  (optional)
    user_verification = 'user_verification_example' # str |  (optional)

    try:
        api_response = api_instance.stages_authenticator_webauthn_list(authenticator_attachment=authenticator_attachment, configure_flow=configure_flow, device_type_restrictions=device_type_restrictions, friendly_name=friendly_name, name=name, ordering=ordering, page=page, page_size=page_size, resident_key_requirement=resident_key_requirement, search=search, stage_uuid=stage_uuid, user_verification=user_verification)
        print("The response of StagesApi->stages_authenticator_webauthn_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_webauthn_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_attachment** | **str**|  | [optional] 
 **configure_flow** | **str**|  | [optional] 
 **device_type_restrictions** | [**List[str]**](str.md)|  | [optional] 
 **friendly_name** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **resident_key_requirement** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **stage_uuid** | **str**|  | [optional] 
 **user_verification** | **str**|  | [optional] 

### Return type

[**PaginatedAuthenticatorWebAuthnStageList**](PaginatedAuthenticatorWebAuthnStageList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_webauthn_partial_update**
> AuthenticatorWebAuthnStage stages_authenticator_webauthn_partial_update(stage_uuid, patched_authenticator_web_authn_stage_request=patched_authenticator_web_authn_stage_request)



AuthenticatorWebAuthnStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_web_authn_stage import AuthenticatorWebAuthnStage
from authentik_openapi.models.patched_authenticator_web_authn_stage_request import PatchedAuthenticatorWebAuthnStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this WebAuthn Authenticator Setup Stage.
    patched_authenticator_web_authn_stage_request = authentik_openapi.PatchedAuthenticatorWebAuthnStageRequest() # PatchedAuthenticatorWebAuthnStageRequest |  (optional)

    try:
        api_response = api_instance.stages_authenticator_webauthn_partial_update(stage_uuid, patched_authenticator_web_authn_stage_request=patched_authenticator_web_authn_stage_request)
        print("The response of StagesApi->stages_authenticator_webauthn_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_webauthn_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this WebAuthn Authenticator Setup Stage. | 
 **patched_authenticator_web_authn_stage_request** | [**PatchedAuthenticatorWebAuthnStageRequest**](PatchedAuthenticatorWebAuthnStageRequest.md)|  | [optional] 

### Return type

[**AuthenticatorWebAuthnStage**](AuthenticatorWebAuthnStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_webauthn_retrieve**
> AuthenticatorWebAuthnStage stages_authenticator_webauthn_retrieve(stage_uuid)



AuthenticatorWebAuthnStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_web_authn_stage import AuthenticatorWebAuthnStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this WebAuthn Authenticator Setup Stage.

    try:
        api_response = api_instance.stages_authenticator_webauthn_retrieve(stage_uuid)
        print("The response of StagesApi->stages_authenticator_webauthn_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_webauthn_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this WebAuthn Authenticator Setup Stage. | 

### Return type

[**AuthenticatorWebAuthnStage**](AuthenticatorWebAuthnStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_webauthn_update**
> AuthenticatorWebAuthnStage stages_authenticator_webauthn_update(stage_uuid, authenticator_web_authn_stage_request)



AuthenticatorWebAuthnStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticator_web_authn_stage import AuthenticatorWebAuthnStage
from authentik_openapi.models.authenticator_web_authn_stage_request import AuthenticatorWebAuthnStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this WebAuthn Authenticator Setup Stage.
    authenticator_web_authn_stage_request = authentik_openapi.AuthenticatorWebAuthnStageRequest() # AuthenticatorWebAuthnStageRequest | 

    try:
        api_response = api_instance.stages_authenticator_webauthn_update(stage_uuid, authenticator_web_authn_stage_request)
        print("The response of StagesApi->stages_authenticator_webauthn_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_webauthn_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this WebAuthn Authenticator Setup Stage. | 
 **authenticator_web_authn_stage_request** | [**AuthenticatorWebAuthnStageRequest**](AuthenticatorWebAuthnStageRequest.md)|  | 

### Return type

[**AuthenticatorWebAuthnStage**](AuthenticatorWebAuthnStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_authenticator_webauthn_used_by_list**
> List[UsedBy] stages_authenticator_webauthn_used_by_list(stage_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this WebAuthn Authenticator Setup Stage.

    try:
        api_response = api_instance.stages_authenticator_webauthn_used_by_list(stage_uuid)
        print("The response of StagesApi->stages_authenticator_webauthn_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_authenticator_webauthn_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this WebAuthn Authenticator Setup Stage. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_captcha_create**
> CaptchaStage stages_captcha_create(captcha_stage_request)



CaptchaStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.captcha_stage import CaptchaStage
from authentik_openapi.models.captcha_stage_request import CaptchaStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    captcha_stage_request = authentik_openapi.CaptchaStageRequest() # CaptchaStageRequest | 

    try:
        api_response = api_instance.stages_captcha_create(captcha_stage_request)
        print("The response of StagesApi->stages_captcha_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_captcha_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **captcha_stage_request** | [**CaptchaStageRequest**](CaptchaStageRequest.md)|  | 

### Return type

[**CaptchaStage**](CaptchaStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_captcha_destroy**
> stages_captcha_destroy(stage_uuid)



CaptchaStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Captcha Stage.

    try:
        api_instance.stages_captcha_destroy(stage_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_captcha_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Captcha Stage. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_captcha_list**
> PaginatedCaptchaStageList stages_captcha_list(name=name, ordering=ordering, page=page, page_size=page_size, public_key=public_key, search=search)



CaptchaStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_captcha_stage_list import PaginatedCaptchaStageList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    public_key = 'public_key_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.stages_captcha_list(name=name, ordering=ordering, page=page, page_size=page_size, public_key=public_key, search=search)
        print("The response of StagesApi->stages_captcha_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_captcha_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **public_key** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedCaptchaStageList**](PaginatedCaptchaStageList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_captcha_partial_update**
> CaptchaStage stages_captcha_partial_update(stage_uuid, patched_captcha_stage_request=patched_captcha_stage_request)



CaptchaStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.captcha_stage import CaptchaStage
from authentik_openapi.models.patched_captcha_stage_request import PatchedCaptchaStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Captcha Stage.
    patched_captcha_stage_request = authentik_openapi.PatchedCaptchaStageRequest() # PatchedCaptchaStageRequest |  (optional)

    try:
        api_response = api_instance.stages_captcha_partial_update(stage_uuid, patched_captcha_stage_request=patched_captcha_stage_request)
        print("The response of StagesApi->stages_captcha_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_captcha_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Captcha Stage. | 
 **patched_captcha_stage_request** | [**PatchedCaptchaStageRequest**](PatchedCaptchaStageRequest.md)|  | [optional] 

### Return type

[**CaptchaStage**](CaptchaStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_captcha_retrieve**
> CaptchaStage stages_captcha_retrieve(stage_uuid)



CaptchaStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.captcha_stage import CaptchaStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Captcha Stage.

    try:
        api_response = api_instance.stages_captcha_retrieve(stage_uuid)
        print("The response of StagesApi->stages_captcha_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_captcha_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Captcha Stage. | 

### Return type

[**CaptchaStage**](CaptchaStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_captcha_update**
> CaptchaStage stages_captcha_update(stage_uuid, captcha_stage_request)



CaptchaStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.captcha_stage import CaptchaStage
from authentik_openapi.models.captcha_stage_request import CaptchaStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Captcha Stage.
    captcha_stage_request = authentik_openapi.CaptchaStageRequest() # CaptchaStageRequest | 

    try:
        api_response = api_instance.stages_captcha_update(stage_uuid, captcha_stage_request)
        print("The response of StagesApi->stages_captcha_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_captcha_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Captcha Stage. | 
 **captcha_stage_request** | [**CaptchaStageRequest**](CaptchaStageRequest.md)|  | 

### Return type

[**CaptchaStage**](CaptchaStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_captcha_used_by_list**
> List[UsedBy] stages_captcha_used_by_list(stage_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Captcha Stage.

    try:
        api_response = api_instance.stages_captcha_used_by_list(stage_uuid)
        print("The response of StagesApi->stages_captcha_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_captcha_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Captcha Stage. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_consent_create**
> ConsentStage stages_consent_create(consent_stage_request)



ConsentStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.consent_stage import ConsentStage
from authentik_openapi.models.consent_stage_request import ConsentStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    consent_stage_request = authentik_openapi.ConsentStageRequest() # ConsentStageRequest | 

    try:
        api_response = api_instance.stages_consent_create(consent_stage_request)
        print("The response of StagesApi->stages_consent_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_consent_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_stage_request** | [**ConsentStageRequest**](ConsentStageRequest.md)|  | 

### Return type

[**ConsentStage**](ConsentStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_consent_destroy**
> stages_consent_destroy(stage_uuid)



ConsentStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Consent Stage.

    try:
        api_instance.stages_consent_destroy(stage_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_consent_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Consent Stage. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_consent_list**
> PaginatedConsentStageList stages_consent_list(consent_expire_in=consent_expire_in, mode=mode, name=name, ordering=ordering, page=page, page_size=page_size, search=search, stage_uuid=stage_uuid)



ConsentStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_consent_stage_list import PaginatedConsentStageList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    consent_expire_in = 'consent_expire_in_example' # str |  (optional)
    mode = 'mode_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    stage_uuid = 'stage_uuid_example' # str |  (optional)

    try:
        api_response = api_instance.stages_consent_list(consent_expire_in=consent_expire_in, mode=mode, name=name, ordering=ordering, page=page, page_size=page_size, search=search, stage_uuid=stage_uuid)
        print("The response of StagesApi->stages_consent_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_consent_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_expire_in** | **str**|  | [optional] 
 **mode** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **stage_uuid** | **str**|  | [optional] 

### Return type

[**PaginatedConsentStageList**](PaginatedConsentStageList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_consent_partial_update**
> ConsentStage stages_consent_partial_update(stage_uuid, patched_consent_stage_request=patched_consent_stage_request)



ConsentStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.consent_stage import ConsentStage
from authentik_openapi.models.patched_consent_stage_request import PatchedConsentStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Consent Stage.
    patched_consent_stage_request = authentik_openapi.PatchedConsentStageRequest() # PatchedConsentStageRequest |  (optional)

    try:
        api_response = api_instance.stages_consent_partial_update(stage_uuid, patched_consent_stage_request=patched_consent_stage_request)
        print("The response of StagesApi->stages_consent_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_consent_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Consent Stage. | 
 **patched_consent_stage_request** | [**PatchedConsentStageRequest**](PatchedConsentStageRequest.md)|  | [optional] 

### Return type

[**ConsentStage**](ConsentStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_consent_retrieve**
> ConsentStage stages_consent_retrieve(stage_uuid)



ConsentStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.consent_stage import ConsentStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Consent Stage.

    try:
        api_response = api_instance.stages_consent_retrieve(stage_uuid)
        print("The response of StagesApi->stages_consent_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_consent_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Consent Stage. | 

### Return type

[**ConsentStage**](ConsentStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_consent_update**
> ConsentStage stages_consent_update(stage_uuid, consent_stage_request)



ConsentStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.consent_stage import ConsentStage
from authentik_openapi.models.consent_stage_request import ConsentStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Consent Stage.
    consent_stage_request = authentik_openapi.ConsentStageRequest() # ConsentStageRequest | 

    try:
        api_response = api_instance.stages_consent_update(stage_uuid, consent_stage_request)
        print("The response of StagesApi->stages_consent_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_consent_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Consent Stage. | 
 **consent_stage_request** | [**ConsentStageRequest**](ConsentStageRequest.md)|  | 

### Return type

[**ConsentStage**](ConsentStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_consent_used_by_list**
> List[UsedBy] stages_consent_used_by_list(stage_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Consent Stage.

    try:
        api_response = api_instance.stages_consent_used_by_list(stage_uuid)
        print("The response of StagesApi->stages_consent_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_consent_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Consent Stage. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_deny_create**
> DenyStage stages_deny_create(deny_stage_request)



DenyStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.deny_stage import DenyStage
from authentik_openapi.models.deny_stage_request import DenyStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    deny_stage_request = authentik_openapi.DenyStageRequest() # DenyStageRequest | 

    try:
        api_response = api_instance.stages_deny_create(deny_stage_request)
        print("The response of StagesApi->stages_deny_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_deny_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deny_stage_request** | [**DenyStageRequest**](DenyStageRequest.md)|  | 

### Return type

[**DenyStage**](DenyStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_deny_destroy**
> stages_deny_destroy(stage_uuid)



DenyStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Deny Stage.

    try:
        api_instance.stages_deny_destroy(stage_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_deny_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Deny Stage. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_deny_list**
> PaginatedDenyStageList stages_deny_list(deny_message=deny_message, name=name, ordering=ordering, page=page, page_size=page_size, search=search, stage_uuid=stage_uuid)



DenyStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_deny_stage_list import PaginatedDenyStageList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    deny_message = 'deny_message_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    stage_uuid = 'stage_uuid_example' # str |  (optional)

    try:
        api_response = api_instance.stages_deny_list(deny_message=deny_message, name=name, ordering=ordering, page=page, page_size=page_size, search=search, stage_uuid=stage_uuid)
        print("The response of StagesApi->stages_deny_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_deny_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deny_message** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **stage_uuid** | **str**|  | [optional] 

### Return type

[**PaginatedDenyStageList**](PaginatedDenyStageList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_deny_partial_update**
> DenyStage stages_deny_partial_update(stage_uuid, patched_deny_stage_request=patched_deny_stage_request)



DenyStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.deny_stage import DenyStage
from authentik_openapi.models.patched_deny_stage_request import PatchedDenyStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Deny Stage.
    patched_deny_stage_request = authentik_openapi.PatchedDenyStageRequest() # PatchedDenyStageRequest |  (optional)

    try:
        api_response = api_instance.stages_deny_partial_update(stage_uuid, patched_deny_stage_request=patched_deny_stage_request)
        print("The response of StagesApi->stages_deny_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_deny_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Deny Stage. | 
 **patched_deny_stage_request** | [**PatchedDenyStageRequest**](PatchedDenyStageRequest.md)|  | [optional] 

### Return type

[**DenyStage**](DenyStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_deny_retrieve**
> DenyStage stages_deny_retrieve(stage_uuid)



DenyStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.deny_stage import DenyStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Deny Stage.

    try:
        api_response = api_instance.stages_deny_retrieve(stage_uuid)
        print("The response of StagesApi->stages_deny_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_deny_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Deny Stage. | 

### Return type

[**DenyStage**](DenyStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_deny_update**
> DenyStage stages_deny_update(stage_uuid, deny_stage_request)



DenyStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.deny_stage import DenyStage
from authentik_openapi.models.deny_stage_request import DenyStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Deny Stage.
    deny_stage_request = authentik_openapi.DenyStageRequest() # DenyStageRequest | 

    try:
        api_response = api_instance.stages_deny_update(stage_uuid, deny_stage_request)
        print("The response of StagesApi->stages_deny_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_deny_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Deny Stage. | 
 **deny_stage_request** | [**DenyStageRequest**](DenyStageRequest.md)|  | 

### Return type

[**DenyStage**](DenyStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_deny_used_by_list**
> List[UsedBy] stages_deny_used_by_list(stage_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Deny Stage.

    try:
        api_response = api_instance.stages_deny_used_by_list(stage_uuid)
        print("The response of StagesApi->stages_deny_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_deny_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Deny Stage. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_dummy_create**
> DummyStage stages_dummy_create(dummy_stage_request)



DummyStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.dummy_stage import DummyStage
from authentik_openapi.models.dummy_stage_request import DummyStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    dummy_stage_request = authentik_openapi.DummyStageRequest() # DummyStageRequest | 

    try:
        api_response = api_instance.stages_dummy_create(dummy_stage_request)
        print("The response of StagesApi->stages_dummy_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_dummy_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dummy_stage_request** | [**DummyStageRequest**](DummyStageRequest.md)|  | 

### Return type

[**DummyStage**](DummyStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_dummy_destroy**
> stages_dummy_destroy(stage_uuid)



DummyStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Dummy Stage.

    try:
        api_instance.stages_dummy_destroy(stage_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_dummy_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Dummy Stage. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_dummy_list**
> PaginatedDummyStageList stages_dummy_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search, stage_uuid=stage_uuid, throw_error=throw_error)



DummyStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_dummy_stage_list import PaginatedDummyStageList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    stage_uuid = 'stage_uuid_example' # str |  (optional)
    throw_error = True # bool |  (optional)

    try:
        api_response = api_instance.stages_dummy_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search, stage_uuid=stage_uuid, throw_error=throw_error)
        print("The response of StagesApi->stages_dummy_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_dummy_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **stage_uuid** | **str**|  | [optional] 
 **throw_error** | **bool**|  | [optional] 

### Return type

[**PaginatedDummyStageList**](PaginatedDummyStageList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_dummy_partial_update**
> DummyStage stages_dummy_partial_update(stage_uuid, patched_dummy_stage_request=patched_dummy_stage_request)



DummyStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.dummy_stage import DummyStage
from authentik_openapi.models.patched_dummy_stage_request import PatchedDummyStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Dummy Stage.
    patched_dummy_stage_request = authentik_openapi.PatchedDummyStageRequest() # PatchedDummyStageRequest |  (optional)

    try:
        api_response = api_instance.stages_dummy_partial_update(stage_uuid, patched_dummy_stage_request=patched_dummy_stage_request)
        print("The response of StagesApi->stages_dummy_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_dummy_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Dummy Stage. | 
 **patched_dummy_stage_request** | [**PatchedDummyStageRequest**](PatchedDummyStageRequest.md)|  | [optional] 

### Return type

[**DummyStage**](DummyStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_dummy_retrieve**
> DummyStage stages_dummy_retrieve(stage_uuid)



DummyStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.dummy_stage import DummyStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Dummy Stage.

    try:
        api_response = api_instance.stages_dummy_retrieve(stage_uuid)
        print("The response of StagesApi->stages_dummy_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_dummy_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Dummy Stage. | 

### Return type

[**DummyStage**](DummyStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_dummy_update**
> DummyStage stages_dummy_update(stage_uuid, dummy_stage_request)



DummyStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.dummy_stage import DummyStage
from authentik_openapi.models.dummy_stage_request import DummyStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Dummy Stage.
    dummy_stage_request = authentik_openapi.DummyStageRequest() # DummyStageRequest | 

    try:
        api_response = api_instance.stages_dummy_update(stage_uuid, dummy_stage_request)
        print("The response of StagesApi->stages_dummy_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_dummy_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Dummy Stage. | 
 **dummy_stage_request** | [**DummyStageRequest**](DummyStageRequest.md)|  | 

### Return type

[**DummyStage**](DummyStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_dummy_used_by_list**
> List[UsedBy] stages_dummy_used_by_list(stage_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Dummy Stage.

    try:
        api_response = api_instance.stages_dummy_used_by_list(stage_uuid)
        print("The response of StagesApi->stages_dummy_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_dummy_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Dummy Stage. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_email_create**
> EmailStage stages_email_create(email_stage_request)



EmailStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.email_stage import EmailStage
from authentik_openapi.models.email_stage_request import EmailStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    email_stage_request = authentik_openapi.EmailStageRequest() # EmailStageRequest | 

    try:
        api_response = api_instance.stages_email_create(email_stage_request)
        print("The response of StagesApi->stages_email_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_email_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_stage_request** | [**EmailStageRequest**](EmailStageRequest.md)|  | 

### Return type

[**EmailStage**](EmailStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_email_destroy**
> stages_email_destroy(stage_uuid)



EmailStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Email Stage.

    try:
        api_instance.stages_email_destroy(stage_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_email_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Email Stage. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_email_list**
> PaginatedEmailStageList stages_email_list(activate_user_on_success=activate_user_on_success, from_address=from_address, host=host, name=name, ordering=ordering, page=page, page_size=page_size, port=port, search=search, subject=subject, template=template, timeout=timeout, token_expiry=token_expiry, use_global_settings=use_global_settings, use_ssl=use_ssl, use_tls=use_tls, username=username)



EmailStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_email_stage_list import PaginatedEmailStageList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    activate_user_on_success = True # bool |  (optional)
    from_address = 'from_address_example' # str |  (optional)
    host = 'host_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    port = 56 # int |  (optional)
    search = 'search_example' # str | A search term. (optional)
    subject = 'subject_example' # str |  (optional)
    template = 'template_example' # str |  (optional)
    timeout = 56 # int |  (optional)
    token_expiry = 56 # int |  (optional)
    use_global_settings = True # bool |  (optional)
    use_ssl = True # bool |  (optional)
    use_tls = True # bool |  (optional)
    username = 'username_example' # str |  (optional)

    try:
        api_response = api_instance.stages_email_list(activate_user_on_success=activate_user_on_success, from_address=from_address, host=host, name=name, ordering=ordering, page=page, page_size=page_size, port=port, search=search, subject=subject, template=template, timeout=timeout, token_expiry=token_expiry, use_global_settings=use_global_settings, use_ssl=use_ssl, use_tls=use_tls, username=username)
        print("The response of StagesApi->stages_email_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_email_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activate_user_on_success** | **bool**|  | [optional] 
 **from_address** | **str**|  | [optional] 
 **host** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **port** | **int**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **subject** | **str**|  | [optional] 
 **template** | **str**|  | [optional] 
 **timeout** | **int**|  | [optional] 
 **token_expiry** | **int**|  | [optional] 
 **use_global_settings** | **bool**|  | [optional] 
 **use_ssl** | **bool**|  | [optional] 
 **use_tls** | **bool**|  | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**PaginatedEmailStageList**](PaginatedEmailStageList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_email_partial_update**
> EmailStage stages_email_partial_update(stage_uuid, patched_email_stage_request=patched_email_stage_request)



EmailStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.email_stage import EmailStage
from authentik_openapi.models.patched_email_stage_request import PatchedEmailStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Email Stage.
    patched_email_stage_request = authentik_openapi.PatchedEmailStageRequest() # PatchedEmailStageRequest |  (optional)

    try:
        api_response = api_instance.stages_email_partial_update(stage_uuid, patched_email_stage_request=patched_email_stage_request)
        print("The response of StagesApi->stages_email_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_email_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Email Stage. | 
 **patched_email_stage_request** | [**PatchedEmailStageRequest**](PatchedEmailStageRequest.md)|  | [optional] 

### Return type

[**EmailStage**](EmailStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_email_retrieve**
> EmailStage stages_email_retrieve(stage_uuid)



EmailStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.email_stage import EmailStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Email Stage.

    try:
        api_response = api_instance.stages_email_retrieve(stage_uuid)
        print("The response of StagesApi->stages_email_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_email_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Email Stage. | 

### Return type

[**EmailStage**](EmailStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_email_templates_list**
> List[TypeCreate] stages_email_templates_list()



Get all available templates, including custom templates

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.type_create import TypeCreate
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)

    try:
        api_response = api_instance.stages_email_templates_list()
        print("The response of StagesApi->stages_email_templates_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_email_templates_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TypeCreate]**](TypeCreate.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_email_update**
> EmailStage stages_email_update(stage_uuid, email_stage_request)



EmailStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.email_stage import EmailStage
from authentik_openapi.models.email_stage_request import EmailStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Email Stage.
    email_stage_request = authentik_openapi.EmailStageRequest() # EmailStageRequest | 

    try:
        api_response = api_instance.stages_email_update(stage_uuid, email_stage_request)
        print("The response of StagesApi->stages_email_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_email_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Email Stage. | 
 **email_stage_request** | [**EmailStageRequest**](EmailStageRequest.md)|  | 

### Return type

[**EmailStage**](EmailStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_email_used_by_list**
> List[UsedBy] stages_email_used_by_list(stage_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Email Stage.

    try:
        api_response = api_instance.stages_email_used_by_list(stage_uuid)
        print("The response of StagesApi->stages_email_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_email_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Email Stage. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_identification_create**
> IdentificationStage stages_identification_create(identification_stage_request)



IdentificationStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.identification_stage import IdentificationStage
from authentik_openapi.models.identification_stage_request import IdentificationStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    identification_stage_request = authentik_openapi.IdentificationStageRequest() # IdentificationStageRequest | 

    try:
        api_response = api_instance.stages_identification_create(identification_stage_request)
        print("The response of StagesApi->stages_identification_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_identification_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identification_stage_request** | [**IdentificationStageRequest**](IdentificationStageRequest.md)|  | 

### Return type

[**IdentificationStage**](IdentificationStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_identification_destroy**
> stages_identification_destroy(stage_uuid)



IdentificationStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Identification Stage.

    try:
        api_instance.stages_identification_destroy(stage_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_identification_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Identification Stage. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_identification_list**
> PaginatedIdentificationStageList stages_identification_list(case_insensitive_matching=case_insensitive_matching, enrollment_flow=enrollment_flow, name=name, ordering=ordering, page=page, page_size=page_size, password_stage=password_stage, passwordless_flow=passwordless_flow, recovery_flow=recovery_flow, search=search, show_matched_user=show_matched_user, show_source_labels=show_source_labels)



IdentificationStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_identification_stage_list import PaginatedIdentificationStageList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    case_insensitive_matching = True # bool |  (optional)
    enrollment_flow = 'enrollment_flow_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    password_stage = 'password_stage_example' # str |  (optional)
    passwordless_flow = 'passwordless_flow_example' # str |  (optional)
    recovery_flow = 'recovery_flow_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)
    show_matched_user = True # bool |  (optional)
    show_source_labels = True # bool |  (optional)

    try:
        api_response = api_instance.stages_identification_list(case_insensitive_matching=case_insensitive_matching, enrollment_flow=enrollment_flow, name=name, ordering=ordering, page=page, page_size=page_size, password_stage=password_stage, passwordless_flow=passwordless_flow, recovery_flow=recovery_flow, search=search, show_matched_user=show_matched_user, show_source_labels=show_source_labels)
        print("The response of StagesApi->stages_identification_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_identification_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_insensitive_matching** | **bool**|  | [optional] 
 **enrollment_flow** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **password_stage** | **str**|  | [optional] 
 **passwordless_flow** | **str**|  | [optional] 
 **recovery_flow** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **show_matched_user** | **bool**|  | [optional] 
 **show_source_labels** | **bool**|  | [optional] 

### Return type

[**PaginatedIdentificationStageList**](PaginatedIdentificationStageList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_identification_partial_update**
> IdentificationStage stages_identification_partial_update(stage_uuid, patched_identification_stage_request=patched_identification_stage_request)



IdentificationStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.identification_stage import IdentificationStage
from authentik_openapi.models.patched_identification_stage_request import PatchedIdentificationStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Identification Stage.
    patched_identification_stage_request = authentik_openapi.PatchedIdentificationStageRequest() # PatchedIdentificationStageRequest |  (optional)

    try:
        api_response = api_instance.stages_identification_partial_update(stage_uuid, patched_identification_stage_request=patched_identification_stage_request)
        print("The response of StagesApi->stages_identification_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_identification_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Identification Stage. | 
 **patched_identification_stage_request** | [**PatchedIdentificationStageRequest**](PatchedIdentificationStageRequest.md)|  | [optional] 

### Return type

[**IdentificationStage**](IdentificationStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_identification_retrieve**
> IdentificationStage stages_identification_retrieve(stage_uuid)



IdentificationStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.identification_stage import IdentificationStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Identification Stage.

    try:
        api_response = api_instance.stages_identification_retrieve(stage_uuid)
        print("The response of StagesApi->stages_identification_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_identification_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Identification Stage. | 

### Return type

[**IdentificationStage**](IdentificationStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_identification_update**
> IdentificationStage stages_identification_update(stage_uuid, identification_stage_request)



IdentificationStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.identification_stage import IdentificationStage
from authentik_openapi.models.identification_stage_request import IdentificationStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Identification Stage.
    identification_stage_request = authentik_openapi.IdentificationStageRequest() # IdentificationStageRequest | 

    try:
        api_response = api_instance.stages_identification_update(stage_uuid, identification_stage_request)
        print("The response of StagesApi->stages_identification_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_identification_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Identification Stage. | 
 **identification_stage_request** | [**IdentificationStageRequest**](IdentificationStageRequest.md)|  | 

### Return type

[**IdentificationStage**](IdentificationStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_identification_used_by_list**
> List[UsedBy] stages_identification_used_by_list(stage_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Identification Stage.

    try:
        api_response = api_instance.stages_identification_used_by_list(stage_uuid)
        print("The response of StagesApi->stages_identification_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_identification_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Identification Stage. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_invitation_invitations_create**
> Invitation stages_invitation_invitations_create(invitation_request)



Invitation Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.invitation import Invitation
from authentik_openapi.models.invitation_request import InvitationRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    invitation_request = authentik_openapi.InvitationRequest() # InvitationRequest | 

    try:
        api_response = api_instance.stages_invitation_invitations_create(invitation_request)
        print("The response of StagesApi->stages_invitation_invitations_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_invitation_invitations_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_request** | [**InvitationRequest**](InvitationRequest.md)|  | 

### Return type

[**Invitation**](Invitation.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_invitation_invitations_destroy**
> stages_invitation_invitations_destroy(invite_uuid)



Invitation Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    invite_uuid = 'invite_uuid_example' # str | A UUID string identifying this Invitation.

    try:
        api_instance.stages_invitation_invitations_destroy(invite_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_invitation_invitations_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_uuid** | **str**| A UUID string identifying this Invitation. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_invitation_invitations_list**
> PaginatedInvitationList stages_invitation_invitations_list(created_by__username=created_by__username, expires=expires, flow__slug=flow__slug, name=name, ordering=ordering, page=page, page_size=page_size, search=search)



Invitation Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_invitation_list import PaginatedInvitationList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    created_by__username = 'created_by__username_example' # str |  (optional)
    expires = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    flow__slug = 'flow__slug_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.stages_invitation_invitations_list(created_by__username=created_by__username, expires=expires, flow__slug=flow__slug, name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of StagesApi->stages_invitation_invitations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_invitation_invitations_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_by__username** | **str**|  | [optional] 
 **expires** | **datetime**|  | [optional] 
 **flow__slug** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedInvitationList**](PaginatedInvitationList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_invitation_invitations_partial_update**
> Invitation stages_invitation_invitations_partial_update(invite_uuid, patched_invitation_request=patched_invitation_request)



Invitation Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.invitation import Invitation
from authentik_openapi.models.patched_invitation_request import PatchedInvitationRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    invite_uuid = 'invite_uuid_example' # str | A UUID string identifying this Invitation.
    patched_invitation_request = authentik_openapi.PatchedInvitationRequest() # PatchedInvitationRequest |  (optional)

    try:
        api_response = api_instance.stages_invitation_invitations_partial_update(invite_uuid, patched_invitation_request=patched_invitation_request)
        print("The response of StagesApi->stages_invitation_invitations_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_invitation_invitations_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_uuid** | **str**| A UUID string identifying this Invitation. | 
 **patched_invitation_request** | [**PatchedInvitationRequest**](PatchedInvitationRequest.md)|  | [optional] 

### Return type

[**Invitation**](Invitation.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_invitation_invitations_retrieve**
> Invitation stages_invitation_invitations_retrieve(invite_uuid)



Invitation Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.invitation import Invitation
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    invite_uuid = 'invite_uuid_example' # str | A UUID string identifying this Invitation.

    try:
        api_response = api_instance.stages_invitation_invitations_retrieve(invite_uuid)
        print("The response of StagesApi->stages_invitation_invitations_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_invitation_invitations_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_uuid** | **str**| A UUID string identifying this Invitation. | 

### Return type

[**Invitation**](Invitation.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_invitation_invitations_update**
> Invitation stages_invitation_invitations_update(invite_uuid, invitation_request)



Invitation Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.invitation import Invitation
from authentik_openapi.models.invitation_request import InvitationRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    invite_uuid = 'invite_uuid_example' # str | A UUID string identifying this Invitation.
    invitation_request = authentik_openapi.InvitationRequest() # InvitationRequest | 

    try:
        api_response = api_instance.stages_invitation_invitations_update(invite_uuid, invitation_request)
        print("The response of StagesApi->stages_invitation_invitations_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_invitation_invitations_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_uuid** | **str**| A UUID string identifying this Invitation. | 
 **invitation_request** | [**InvitationRequest**](InvitationRequest.md)|  | 

### Return type

[**Invitation**](Invitation.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_invitation_invitations_used_by_list**
> List[UsedBy] stages_invitation_invitations_used_by_list(invite_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    invite_uuid = 'invite_uuid_example' # str | A UUID string identifying this Invitation.

    try:
        api_response = api_instance.stages_invitation_invitations_used_by_list(invite_uuid)
        print("The response of StagesApi->stages_invitation_invitations_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_invitation_invitations_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_uuid** | **str**| A UUID string identifying this Invitation. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_invitation_stages_create**
> InvitationStage stages_invitation_stages_create(invitation_stage_request)



InvitationStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.invitation_stage import InvitationStage
from authentik_openapi.models.invitation_stage_request import InvitationStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    invitation_stage_request = authentik_openapi.InvitationStageRequest() # InvitationStageRequest | 

    try:
        api_response = api_instance.stages_invitation_stages_create(invitation_stage_request)
        print("The response of StagesApi->stages_invitation_stages_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_invitation_stages_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_stage_request** | [**InvitationStageRequest**](InvitationStageRequest.md)|  | 

### Return type

[**InvitationStage**](InvitationStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_invitation_stages_destroy**
> stages_invitation_stages_destroy(stage_uuid)



InvitationStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Invitation Stage.

    try:
        api_instance.stages_invitation_stages_destroy(stage_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_invitation_stages_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Invitation Stage. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_invitation_stages_list**
> PaginatedInvitationStageList stages_invitation_stages_list(continue_flow_without_invitation=continue_flow_without_invitation, name=name, no_flows=no_flows, ordering=ordering, page=page, page_size=page_size, search=search, stage_uuid=stage_uuid)



InvitationStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_invitation_stage_list import PaginatedInvitationStageList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    continue_flow_without_invitation = True # bool |  (optional)
    name = 'name_example' # str |  (optional)
    no_flows = True # bool |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    stage_uuid = 'stage_uuid_example' # str |  (optional)

    try:
        api_response = api_instance.stages_invitation_stages_list(continue_flow_without_invitation=continue_flow_without_invitation, name=name, no_flows=no_flows, ordering=ordering, page=page, page_size=page_size, search=search, stage_uuid=stage_uuid)
        print("The response of StagesApi->stages_invitation_stages_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_invitation_stages_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **continue_flow_without_invitation** | **bool**|  | [optional] 
 **name** | **str**|  | [optional] 
 **no_flows** | **bool**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **stage_uuid** | **str**|  | [optional] 

### Return type

[**PaginatedInvitationStageList**](PaginatedInvitationStageList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_invitation_stages_partial_update**
> InvitationStage stages_invitation_stages_partial_update(stage_uuid, patched_invitation_stage_request=patched_invitation_stage_request)



InvitationStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.invitation_stage import InvitationStage
from authentik_openapi.models.patched_invitation_stage_request import PatchedInvitationStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Invitation Stage.
    patched_invitation_stage_request = authentik_openapi.PatchedInvitationStageRequest() # PatchedInvitationStageRequest |  (optional)

    try:
        api_response = api_instance.stages_invitation_stages_partial_update(stage_uuid, patched_invitation_stage_request=patched_invitation_stage_request)
        print("The response of StagesApi->stages_invitation_stages_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_invitation_stages_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Invitation Stage. | 
 **patched_invitation_stage_request** | [**PatchedInvitationStageRequest**](PatchedInvitationStageRequest.md)|  | [optional] 

### Return type

[**InvitationStage**](InvitationStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_invitation_stages_retrieve**
> InvitationStage stages_invitation_stages_retrieve(stage_uuid)



InvitationStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.invitation_stage import InvitationStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Invitation Stage.

    try:
        api_response = api_instance.stages_invitation_stages_retrieve(stage_uuid)
        print("The response of StagesApi->stages_invitation_stages_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_invitation_stages_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Invitation Stage. | 

### Return type

[**InvitationStage**](InvitationStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_invitation_stages_update**
> InvitationStage stages_invitation_stages_update(stage_uuid, invitation_stage_request)



InvitationStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.invitation_stage import InvitationStage
from authentik_openapi.models.invitation_stage_request import InvitationStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Invitation Stage.
    invitation_stage_request = authentik_openapi.InvitationStageRequest() # InvitationStageRequest | 

    try:
        api_response = api_instance.stages_invitation_stages_update(stage_uuid, invitation_stage_request)
        print("The response of StagesApi->stages_invitation_stages_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_invitation_stages_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Invitation Stage. | 
 **invitation_stage_request** | [**InvitationStageRequest**](InvitationStageRequest.md)|  | 

### Return type

[**InvitationStage**](InvitationStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_invitation_stages_used_by_list**
> List[UsedBy] stages_invitation_stages_used_by_list(stage_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Invitation Stage.

    try:
        api_response = api_instance.stages_invitation_stages_used_by_list(stage_uuid)
        print("The response of StagesApi->stages_invitation_stages_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_invitation_stages_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Invitation Stage. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_password_create**
> PasswordStage stages_password_create(password_stage_request)



PasswordStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.password_stage import PasswordStage
from authentik_openapi.models.password_stage_request import PasswordStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    password_stage_request = authentik_openapi.PasswordStageRequest() # PasswordStageRequest | 

    try:
        api_response = api_instance.stages_password_create(password_stage_request)
        print("The response of StagesApi->stages_password_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_password_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_stage_request** | [**PasswordStageRequest**](PasswordStageRequest.md)|  | 

### Return type

[**PasswordStage**](PasswordStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_password_destroy**
> stages_password_destroy(stage_uuid)



PasswordStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Password Stage.

    try:
        api_instance.stages_password_destroy(stage_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_password_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Password Stage. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_password_list**
> PaginatedPasswordStageList stages_password_list(configure_flow=configure_flow, failed_attempts_before_cancel=failed_attempts_before_cancel, name=name, ordering=ordering, page=page, page_size=page_size, search=search)



PasswordStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_password_stage_list import PaginatedPasswordStageList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    configure_flow = 'configure_flow_example' # str |  (optional)
    failed_attempts_before_cancel = 56 # int |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.stages_password_list(configure_flow=configure_flow, failed_attempts_before_cancel=failed_attempts_before_cancel, name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of StagesApi->stages_password_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_password_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configure_flow** | **str**|  | [optional] 
 **failed_attempts_before_cancel** | **int**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedPasswordStageList**](PaginatedPasswordStageList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_password_partial_update**
> PasswordStage stages_password_partial_update(stage_uuid, patched_password_stage_request=patched_password_stage_request)



PasswordStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.password_stage import PasswordStage
from authentik_openapi.models.patched_password_stage_request import PatchedPasswordStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Password Stage.
    patched_password_stage_request = authentik_openapi.PatchedPasswordStageRequest() # PatchedPasswordStageRequest |  (optional)

    try:
        api_response = api_instance.stages_password_partial_update(stage_uuid, patched_password_stage_request=patched_password_stage_request)
        print("The response of StagesApi->stages_password_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_password_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Password Stage. | 
 **patched_password_stage_request** | [**PatchedPasswordStageRequest**](PatchedPasswordStageRequest.md)|  | [optional] 

### Return type

[**PasswordStage**](PasswordStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_password_retrieve**
> PasswordStage stages_password_retrieve(stage_uuid)



PasswordStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.password_stage import PasswordStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Password Stage.

    try:
        api_response = api_instance.stages_password_retrieve(stage_uuid)
        print("The response of StagesApi->stages_password_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_password_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Password Stage. | 

### Return type

[**PasswordStage**](PasswordStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_password_update**
> PasswordStage stages_password_update(stage_uuid, password_stage_request)



PasswordStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.password_stage import PasswordStage
from authentik_openapi.models.password_stage_request import PasswordStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Password Stage.
    password_stage_request = authentik_openapi.PasswordStageRequest() # PasswordStageRequest | 

    try:
        api_response = api_instance.stages_password_update(stage_uuid, password_stage_request)
        print("The response of StagesApi->stages_password_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_password_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Password Stage. | 
 **password_stage_request** | [**PasswordStageRequest**](PasswordStageRequest.md)|  | 

### Return type

[**PasswordStage**](PasswordStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_password_used_by_list**
> List[UsedBy] stages_password_used_by_list(stage_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Password Stage.

    try:
        api_response = api_instance.stages_password_used_by_list(stage_uuid)
        print("The response of StagesApi->stages_password_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_password_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Password Stage. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_prompt_prompts_create**
> Prompt stages_prompt_prompts_create(prompt_request)



Prompt Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.prompt import Prompt
from authentik_openapi.models.prompt_request import PromptRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    prompt_request = authentik_openapi.PromptRequest() # PromptRequest | 

    try:
        api_response = api_instance.stages_prompt_prompts_create(prompt_request)
        print("The response of StagesApi->stages_prompt_prompts_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_prompt_prompts_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_request** | [**PromptRequest**](PromptRequest.md)|  | 

### Return type

[**Prompt**](Prompt.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_prompt_prompts_destroy**
> stages_prompt_prompts_destroy(prompt_uuid)



Prompt Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    prompt_uuid = 'prompt_uuid_example' # str | A UUID string identifying this Prompt.

    try:
        api_instance.stages_prompt_prompts_destroy(prompt_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_prompt_prompts_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_uuid** | **str**| A UUID string identifying this Prompt. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_prompt_prompts_list**
> PaginatedPromptList stages_prompt_prompts_list(field_key=field_key, label=label, name=name, ordering=ordering, page=page, page_size=page_size, placeholder=placeholder, search=search, type=type)



Prompt Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_prompt_list import PaginatedPromptList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    field_key = 'field_key_example' # str |  (optional)
    label = 'label_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    placeholder = 'placeholder_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)
    type = 'type_example' # str |  (optional)

    try:
        api_response = api_instance.stages_prompt_prompts_list(field_key=field_key, label=label, name=name, ordering=ordering, page=page, page_size=page_size, placeholder=placeholder, search=search, type=type)
        print("The response of StagesApi->stages_prompt_prompts_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_prompt_prompts_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_key** | **str**|  | [optional] 
 **label** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **placeholder** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **type** | **str**|  | [optional] 

### Return type

[**PaginatedPromptList**](PaginatedPromptList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_prompt_prompts_partial_update**
> Prompt stages_prompt_prompts_partial_update(prompt_uuid, patched_prompt_request=patched_prompt_request)



Prompt Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_prompt_request import PatchedPromptRequest
from authentik_openapi.models.prompt import Prompt
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    prompt_uuid = 'prompt_uuid_example' # str | A UUID string identifying this Prompt.
    patched_prompt_request = authentik_openapi.PatchedPromptRequest() # PatchedPromptRequest |  (optional)

    try:
        api_response = api_instance.stages_prompt_prompts_partial_update(prompt_uuid, patched_prompt_request=patched_prompt_request)
        print("The response of StagesApi->stages_prompt_prompts_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_prompt_prompts_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_uuid** | **str**| A UUID string identifying this Prompt. | 
 **patched_prompt_request** | [**PatchedPromptRequest**](PatchedPromptRequest.md)|  | [optional] 

### Return type

[**Prompt**](Prompt.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_prompt_prompts_preview_create**
> PromptChallenge stages_prompt_prompts_preview_create(prompt_request)



Preview a prompt as a challenge, just like a flow would receive

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.prompt_challenge import PromptChallenge
from authentik_openapi.models.prompt_request import PromptRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    prompt_request = authentik_openapi.PromptRequest() # PromptRequest | 

    try:
        api_response = api_instance.stages_prompt_prompts_preview_create(prompt_request)
        print("The response of StagesApi->stages_prompt_prompts_preview_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_prompt_prompts_preview_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_request** | [**PromptRequest**](PromptRequest.md)|  | 

### Return type

[**PromptChallenge**](PromptChallenge.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_prompt_prompts_retrieve**
> Prompt stages_prompt_prompts_retrieve(prompt_uuid)



Prompt Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.prompt import Prompt
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    prompt_uuid = 'prompt_uuid_example' # str | A UUID string identifying this Prompt.

    try:
        api_response = api_instance.stages_prompt_prompts_retrieve(prompt_uuid)
        print("The response of StagesApi->stages_prompt_prompts_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_prompt_prompts_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_uuid** | **str**| A UUID string identifying this Prompt. | 

### Return type

[**Prompt**](Prompt.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_prompt_prompts_update**
> Prompt stages_prompt_prompts_update(prompt_uuid, prompt_request)



Prompt Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.prompt import Prompt
from authentik_openapi.models.prompt_request import PromptRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    prompt_uuid = 'prompt_uuid_example' # str | A UUID string identifying this Prompt.
    prompt_request = authentik_openapi.PromptRequest() # PromptRequest | 

    try:
        api_response = api_instance.stages_prompt_prompts_update(prompt_uuid, prompt_request)
        print("The response of StagesApi->stages_prompt_prompts_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_prompt_prompts_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_uuid** | **str**| A UUID string identifying this Prompt. | 
 **prompt_request** | [**PromptRequest**](PromptRequest.md)|  | 

### Return type

[**Prompt**](Prompt.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_prompt_prompts_used_by_list**
> List[UsedBy] stages_prompt_prompts_used_by_list(prompt_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    prompt_uuid = 'prompt_uuid_example' # str | A UUID string identifying this Prompt.

    try:
        api_response = api_instance.stages_prompt_prompts_used_by_list(prompt_uuid)
        print("The response of StagesApi->stages_prompt_prompts_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_prompt_prompts_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_uuid** | **str**| A UUID string identifying this Prompt. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_prompt_stages_create**
> PromptStage stages_prompt_stages_create(prompt_stage_request)



PromptStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.prompt_stage import PromptStage
from authentik_openapi.models.prompt_stage_request import PromptStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    prompt_stage_request = authentik_openapi.PromptStageRequest() # PromptStageRequest | 

    try:
        api_response = api_instance.stages_prompt_stages_create(prompt_stage_request)
        print("The response of StagesApi->stages_prompt_stages_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_prompt_stages_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_stage_request** | [**PromptStageRequest**](PromptStageRequest.md)|  | 

### Return type

[**PromptStage**](PromptStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_prompt_stages_destroy**
> stages_prompt_stages_destroy(stage_uuid)



PromptStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Prompt Stage.

    try:
        api_instance.stages_prompt_stages_destroy(stage_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_prompt_stages_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Prompt Stage. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_prompt_stages_list**
> PaginatedPromptStageList stages_prompt_stages_list(fields=fields, name=name, ordering=ordering, page=page, page_size=page_size, search=search, stage_uuid=stage_uuid, validation_policies=validation_policies)



PromptStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_prompt_stage_list import PaginatedPromptStageList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    fields = ['fields_example'] # List[str] |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    stage_uuid = 'stage_uuid_example' # str |  (optional)
    validation_policies = ['validation_policies_example'] # List[str] |  (optional)

    try:
        api_response = api_instance.stages_prompt_stages_list(fields=fields, name=name, ordering=ordering, page=page, page_size=page_size, search=search, stage_uuid=stage_uuid, validation_policies=validation_policies)
        print("The response of StagesApi->stages_prompt_stages_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_prompt_stages_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**List[str]**](str.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **stage_uuid** | **str**|  | [optional] 
 **validation_policies** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**PaginatedPromptStageList**](PaginatedPromptStageList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_prompt_stages_partial_update**
> PromptStage stages_prompt_stages_partial_update(stage_uuid, patched_prompt_stage_request=patched_prompt_stage_request)



PromptStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_prompt_stage_request import PatchedPromptStageRequest
from authentik_openapi.models.prompt_stage import PromptStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Prompt Stage.
    patched_prompt_stage_request = authentik_openapi.PatchedPromptStageRequest() # PatchedPromptStageRequest |  (optional)

    try:
        api_response = api_instance.stages_prompt_stages_partial_update(stage_uuid, patched_prompt_stage_request=patched_prompt_stage_request)
        print("The response of StagesApi->stages_prompt_stages_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_prompt_stages_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Prompt Stage. | 
 **patched_prompt_stage_request** | [**PatchedPromptStageRequest**](PatchedPromptStageRequest.md)|  | [optional] 

### Return type

[**PromptStage**](PromptStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_prompt_stages_retrieve**
> PromptStage stages_prompt_stages_retrieve(stage_uuid)



PromptStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.prompt_stage import PromptStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Prompt Stage.

    try:
        api_response = api_instance.stages_prompt_stages_retrieve(stage_uuid)
        print("The response of StagesApi->stages_prompt_stages_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_prompt_stages_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Prompt Stage. | 

### Return type

[**PromptStage**](PromptStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_prompt_stages_update**
> PromptStage stages_prompt_stages_update(stage_uuid, prompt_stage_request)



PromptStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.prompt_stage import PromptStage
from authentik_openapi.models.prompt_stage_request import PromptStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Prompt Stage.
    prompt_stage_request = authentik_openapi.PromptStageRequest() # PromptStageRequest | 

    try:
        api_response = api_instance.stages_prompt_stages_update(stage_uuid, prompt_stage_request)
        print("The response of StagesApi->stages_prompt_stages_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_prompt_stages_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Prompt Stage. | 
 **prompt_stage_request** | [**PromptStageRequest**](PromptStageRequest.md)|  | 

### Return type

[**PromptStage**](PromptStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_prompt_stages_used_by_list**
> List[UsedBy] stages_prompt_stages_used_by_list(stage_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Prompt Stage.

    try:
        api_response = api_instance.stages_prompt_stages_used_by_list(stage_uuid)
        print("The response of StagesApi->stages_prompt_stages_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_prompt_stages_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Prompt Stage. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_source_create**
> SourceStage stages_source_create(source_stage_request)



SourceStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.source_stage import SourceStage
from authentik_openapi.models.source_stage_request import SourceStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    source_stage_request = authentik_openapi.SourceStageRequest() # SourceStageRequest | 

    try:
        api_response = api_instance.stages_source_create(source_stage_request)
        print("The response of StagesApi->stages_source_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_source_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_stage_request** | [**SourceStageRequest**](SourceStageRequest.md)|  | 

### Return type

[**SourceStage**](SourceStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_source_destroy**
> stages_source_destroy(stage_uuid)



SourceStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Source Stage.

    try:
        api_instance.stages_source_destroy(stage_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_source_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Source Stage. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_source_list**
> PaginatedSourceStageList stages_source_list(name=name, ordering=ordering, page=page, page_size=page_size, resume_timeout=resume_timeout, search=search, source=source, stage_uuid=stage_uuid)



SourceStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_source_stage_list import PaginatedSourceStageList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    resume_timeout = 'resume_timeout_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)
    source = 'source_example' # str |  (optional)
    stage_uuid = 'stage_uuid_example' # str |  (optional)

    try:
        api_response = api_instance.stages_source_list(name=name, ordering=ordering, page=page, page_size=page_size, resume_timeout=resume_timeout, search=search, source=source, stage_uuid=stage_uuid)
        print("The response of StagesApi->stages_source_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_source_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **resume_timeout** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **source** | **str**|  | [optional] 
 **stage_uuid** | **str**|  | [optional] 

### Return type

[**PaginatedSourceStageList**](PaginatedSourceStageList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_source_partial_update**
> SourceStage stages_source_partial_update(stage_uuid, patched_source_stage_request=patched_source_stage_request)



SourceStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_source_stage_request import PatchedSourceStageRequest
from authentik_openapi.models.source_stage import SourceStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Source Stage.
    patched_source_stage_request = authentik_openapi.PatchedSourceStageRequest() # PatchedSourceStageRequest |  (optional)

    try:
        api_response = api_instance.stages_source_partial_update(stage_uuid, patched_source_stage_request=patched_source_stage_request)
        print("The response of StagesApi->stages_source_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_source_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Source Stage. | 
 **patched_source_stage_request** | [**PatchedSourceStageRequest**](PatchedSourceStageRequest.md)|  | [optional] 

### Return type

[**SourceStage**](SourceStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_source_retrieve**
> SourceStage stages_source_retrieve(stage_uuid)



SourceStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.source_stage import SourceStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Source Stage.

    try:
        api_response = api_instance.stages_source_retrieve(stage_uuid)
        print("The response of StagesApi->stages_source_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_source_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Source Stage. | 

### Return type

[**SourceStage**](SourceStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_source_update**
> SourceStage stages_source_update(stage_uuid, source_stage_request)



SourceStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.source_stage import SourceStage
from authentik_openapi.models.source_stage_request import SourceStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Source Stage.
    source_stage_request = authentik_openapi.SourceStageRequest() # SourceStageRequest | 

    try:
        api_response = api_instance.stages_source_update(stage_uuid, source_stage_request)
        print("The response of StagesApi->stages_source_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_source_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Source Stage. | 
 **source_stage_request** | [**SourceStageRequest**](SourceStageRequest.md)|  | 

### Return type

[**SourceStage**](SourceStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_source_used_by_list**
> List[UsedBy] stages_source_used_by_list(stage_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this Source Stage.

    try:
        api_response = api_instance.stages_source_used_by_list(stage_uuid)
        print("The response of StagesApi->stages_source_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_source_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this Source Stage. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_delete_create**
> UserDeleteStage stages_user_delete_create(user_delete_stage_request)



UserDeleteStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_delete_stage import UserDeleteStage
from authentik_openapi.models.user_delete_stage_request import UserDeleteStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    user_delete_stage_request = authentik_openapi.UserDeleteStageRequest() # UserDeleteStageRequest | 

    try:
        api_response = api_instance.stages_user_delete_create(user_delete_stage_request)
        print("The response of StagesApi->stages_user_delete_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_delete_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_delete_stage_request** | [**UserDeleteStageRequest**](UserDeleteStageRequest.md)|  | 

### Return type

[**UserDeleteStage**](UserDeleteStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_delete_destroy**
> stages_user_delete_destroy(stage_uuid)



UserDeleteStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this User Delete Stage.

    try:
        api_instance.stages_user_delete_destroy(stage_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_delete_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this User Delete Stage. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_delete_list**
> PaginatedUserDeleteStageList stages_user_delete_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search, stage_uuid=stage_uuid)



UserDeleteStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_user_delete_stage_list import PaginatedUserDeleteStageList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    stage_uuid = 'stage_uuid_example' # str |  (optional)

    try:
        api_response = api_instance.stages_user_delete_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search, stage_uuid=stage_uuid)
        print("The response of StagesApi->stages_user_delete_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_delete_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **stage_uuid** | **str**|  | [optional] 

### Return type

[**PaginatedUserDeleteStageList**](PaginatedUserDeleteStageList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_delete_partial_update**
> UserDeleteStage stages_user_delete_partial_update(stage_uuid, patched_user_delete_stage_request=patched_user_delete_stage_request)



UserDeleteStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_user_delete_stage_request import PatchedUserDeleteStageRequest
from authentik_openapi.models.user_delete_stage import UserDeleteStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this User Delete Stage.
    patched_user_delete_stage_request = authentik_openapi.PatchedUserDeleteStageRequest() # PatchedUserDeleteStageRequest |  (optional)

    try:
        api_response = api_instance.stages_user_delete_partial_update(stage_uuid, patched_user_delete_stage_request=patched_user_delete_stage_request)
        print("The response of StagesApi->stages_user_delete_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_delete_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this User Delete Stage. | 
 **patched_user_delete_stage_request** | [**PatchedUserDeleteStageRequest**](PatchedUserDeleteStageRequest.md)|  | [optional] 

### Return type

[**UserDeleteStage**](UserDeleteStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_delete_retrieve**
> UserDeleteStage stages_user_delete_retrieve(stage_uuid)



UserDeleteStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_delete_stage import UserDeleteStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this User Delete Stage.

    try:
        api_response = api_instance.stages_user_delete_retrieve(stage_uuid)
        print("The response of StagesApi->stages_user_delete_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_delete_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this User Delete Stage. | 

### Return type

[**UserDeleteStage**](UserDeleteStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_delete_update**
> UserDeleteStage stages_user_delete_update(stage_uuid, user_delete_stage_request)



UserDeleteStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_delete_stage import UserDeleteStage
from authentik_openapi.models.user_delete_stage_request import UserDeleteStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this User Delete Stage.
    user_delete_stage_request = authentik_openapi.UserDeleteStageRequest() # UserDeleteStageRequest | 

    try:
        api_response = api_instance.stages_user_delete_update(stage_uuid, user_delete_stage_request)
        print("The response of StagesApi->stages_user_delete_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_delete_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this User Delete Stage. | 
 **user_delete_stage_request** | [**UserDeleteStageRequest**](UserDeleteStageRequest.md)|  | 

### Return type

[**UserDeleteStage**](UserDeleteStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_delete_used_by_list**
> List[UsedBy] stages_user_delete_used_by_list(stage_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this User Delete Stage.

    try:
        api_response = api_instance.stages_user_delete_used_by_list(stage_uuid)
        print("The response of StagesApi->stages_user_delete_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_delete_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this User Delete Stage. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_login_create**
> UserLoginStage stages_user_login_create(user_login_stage_request)



UserLoginStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_login_stage import UserLoginStage
from authentik_openapi.models.user_login_stage_request import UserLoginStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    user_login_stage_request = authentik_openapi.UserLoginStageRequest() # UserLoginStageRequest | 

    try:
        api_response = api_instance.stages_user_login_create(user_login_stage_request)
        print("The response of StagesApi->stages_user_login_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_login_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_login_stage_request** | [**UserLoginStageRequest**](UserLoginStageRequest.md)|  | 

### Return type

[**UserLoginStage**](UserLoginStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_login_destroy**
> stages_user_login_destroy(stage_uuid)



UserLoginStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this User Login Stage.

    try:
        api_instance.stages_user_login_destroy(stage_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_login_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this User Login Stage. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_login_list**
> PaginatedUserLoginStageList stages_user_login_list(geoip_binding=geoip_binding, name=name, network_binding=network_binding, ordering=ordering, page=page, page_size=page_size, remember_me_offset=remember_me_offset, search=search, session_duration=session_duration, stage_uuid=stage_uuid, terminate_other_sessions=terminate_other_sessions)



UserLoginStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_user_login_stage_list import PaginatedUserLoginStageList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    geoip_binding = 'geoip_binding_example' # str | Bind sessions created by this stage to the configured GeoIP location   (optional)
    name = 'name_example' # str |  (optional)
    network_binding = 'network_binding_example' # str | Bind sessions created by this stage to the configured network   (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    remember_me_offset = 'remember_me_offset_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)
    session_duration = 'session_duration_example' # str |  (optional)
    stage_uuid = 'stage_uuid_example' # str |  (optional)
    terminate_other_sessions = True # bool |  (optional)

    try:
        api_response = api_instance.stages_user_login_list(geoip_binding=geoip_binding, name=name, network_binding=network_binding, ordering=ordering, page=page, page_size=page_size, remember_me_offset=remember_me_offset, search=search, session_duration=session_duration, stage_uuid=stage_uuid, terminate_other_sessions=terminate_other_sessions)
        print("The response of StagesApi->stages_user_login_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_login_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geoip_binding** | **str**| Bind sessions created by this stage to the configured GeoIP location   | [optional] 
 **name** | **str**|  | [optional] 
 **network_binding** | **str**| Bind sessions created by this stage to the configured network   | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **remember_me_offset** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **session_duration** | **str**|  | [optional] 
 **stage_uuid** | **str**|  | [optional] 
 **terminate_other_sessions** | **bool**|  | [optional] 

### Return type

[**PaginatedUserLoginStageList**](PaginatedUserLoginStageList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_login_partial_update**
> UserLoginStage stages_user_login_partial_update(stage_uuid, patched_user_login_stage_request=patched_user_login_stage_request)



UserLoginStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_user_login_stage_request import PatchedUserLoginStageRequest
from authentik_openapi.models.user_login_stage import UserLoginStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this User Login Stage.
    patched_user_login_stage_request = authentik_openapi.PatchedUserLoginStageRequest() # PatchedUserLoginStageRequest |  (optional)

    try:
        api_response = api_instance.stages_user_login_partial_update(stage_uuid, patched_user_login_stage_request=patched_user_login_stage_request)
        print("The response of StagesApi->stages_user_login_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_login_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this User Login Stage. | 
 **patched_user_login_stage_request** | [**PatchedUserLoginStageRequest**](PatchedUserLoginStageRequest.md)|  | [optional] 

### Return type

[**UserLoginStage**](UserLoginStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_login_retrieve**
> UserLoginStage stages_user_login_retrieve(stage_uuid)



UserLoginStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_login_stage import UserLoginStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this User Login Stage.

    try:
        api_response = api_instance.stages_user_login_retrieve(stage_uuid)
        print("The response of StagesApi->stages_user_login_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_login_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this User Login Stage. | 

### Return type

[**UserLoginStage**](UserLoginStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_login_update**
> UserLoginStage stages_user_login_update(stage_uuid, user_login_stage_request)



UserLoginStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_login_stage import UserLoginStage
from authentik_openapi.models.user_login_stage_request import UserLoginStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this User Login Stage.
    user_login_stage_request = authentik_openapi.UserLoginStageRequest() # UserLoginStageRequest | 

    try:
        api_response = api_instance.stages_user_login_update(stage_uuid, user_login_stage_request)
        print("The response of StagesApi->stages_user_login_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_login_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this User Login Stage. | 
 **user_login_stage_request** | [**UserLoginStageRequest**](UserLoginStageRequest.md)|  | 

### Return type

[**UserLoginStage**](UserLoginStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_login_used_by_list**
> List[UsedBy] stages_user_login_used_by_list(stage_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this User Login Stage.

    try:
        api_response = api_instance.stages_user_login_used_by_list(stage_uuid)
        print("The response of StagesApi->stages_user_login_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_login_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this User Login Stage. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_logout_create**
> UserLogoutStage stages_user_logout_create(user_logout_stage_request)



UserLogoutStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_logout_stage import UserLogoutStage
from authentik_openapi.models.user_logout_stage_request import UserLogoutStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    user_logout_stage_request = authentik_openapi.UserLogoutStageRequest() # UserLogoutStageRequest | 

    try:
        api_response = api_instance.stages_user_logout_create(user_logout_stage_request)
        print("The response of StagesApi->stages_user_logout_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_logout_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_logout_stage_request** | [**UserLogoutStageRequest**](UserLogoutStageRequest.md)|  | 

### Return type

[**UserLogoutStage**](UserLogoutStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_logout_destroy**
> stages_user_logout_destroy(stage_uuid)



UserLogoutStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this User Logout Stage.

    try:
        api_instance.stages_user_logout_destroy(stage_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_logout_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this User Logout Stage. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_logout_list**
> PaginatedUserLogoutStageList stages_user_logout_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search, stage_uuid=stage_uuid)



UserLogoutStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_user_logout_stage_list import PaginatedUserLogoutStageList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    stage_uuid = 'stage_uuid_example' # str |  (optional)

    try:
        api_response = api_instance.stages_user_logout_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search, stage_uuid=stage_uuid)
        print("The response of StagesApi->stages_user_logout_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_logout_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **stage_uuid** | **str**|  | [optional] 

### Return type

[**PaginatedUserLogoutStageList**](PaginatedUserLogoutStageList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_logout_partial_update**
> UserLogoutStage stages_user_logout_partial_update(stage_uuid, patched_user_logout_stage_request=patched_user_logout_stage_request)



UserLogoutStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_user_logout_stage_request import PatchedUserLogoutStageRequest
from authentik_openapi.models.user_logout_stage import UserLogoutStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this User Logout Stage.
    patched_user_logout_stage_request = authentik_openapi.PatchedUserLogoutStageRequest() # PatchedUserLogoutStageRequest |  (optional)

    try:
        api_response = api_instance.stages_user_logout_partial_update(stage_uuid, patched_user_logout_stage_request=patched_user_logout_stage_request)
        print("The response of StagesApi->stages_user_logout_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_logout_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this User Logout Stage. | 
 **patched_user_logout_stage_request** | [**PatchedUserLogoutStageRequest**](PatchedUserLogoutStageRequest.md)|  | [optional] 

### Return type

[**UserLogoutStage**](UserLogoutStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_logout_retrieve**
> UserLogoutStage stages_user_logout_retrieve(stage_uuid)



UserLogoutStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_logout_stage import UserLogoutStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this User Logout Stage.

    try:
        api_response = api_instance.stages_user_logout_retrieve(stage_uuid)
        print("The response of StagesApi->stages_user_logout_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_logout_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this User Logout Stage. | 

### Return type

[**UserLogoutStage**](UserLogoutStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_logout_update**
> UserLogoutStage stages_user_logout_update(stage_uuid, user_logout_stage_request)



UserLogoutStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_logout_stage import UserLogoutStage
from authentik_openapi.models.user_logout_stage_request import UserLogoutStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this User Logout Stage.
    user_logout_stage_request = authentik_openapi.UserLogoutStageRequest() # UserLogoutStageRequest | 

    try:
        api_response = api_instance.stages_user_logout_update(stage_uuid, user_logout_stage_request)
        print("The response of StagesApi->stages_user_logout_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_logout_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this User Logout Stage. | 
 **user_logout_stage_request** | [**UserLogoutStageRequest**](UserLogoutStageRequest.md)|  | 

### Return type

[**UserLogoutStage**](UserLogoutStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_logout_used_by_list**
> List[UsedBy] stages_user_logout_used_by_list(stage_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this User Logout Stage.

    try:
        api_response = api_instance.stages_user_logout_used_by_list(stage_uuid)
        print("The response of StagesApi->stages_user_logout_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_logout_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this User Logout Stage. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_write_create**
> UserWriteStage stages_user_write_create(user_write_stage_request)



UserWriteStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_write_stage import UserWriteStage
from authentik_openapi.models.user_write_stage_request import UserWriteStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    user_write_stage_request = authentik_openapi.UserWriteStageRequest() # UserWriteStageRequest | 

    try:
        api_response = api_instance.stages_user_write_create(user_write_stage_request)
        print("The response of StagesApi->stages_user_write_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_write_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_write_stage_request** | [**UserWriteStageRequest**](UserWriteStageRequest.md)|  | 

### Return type

[**UserWriteStage**](UserWriteStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_write_destroy**
> stages_user_write_destroy(stage_uuid)



UserWriteStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this User Write Stage.

    try:
        api_instance.stages_user_write_destroy(stage_uuid)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_write_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this User Write Stage. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_write_list**
> PaginatedUserWriteStageList stages_user_write_list(create_users_as_inactive=create_users_as_inactive, create_users_group=create_users_group, name=name, ordering=ordering, page=page, page_size=page_size, search=search, stage_uuid=stage_uuid, user_creation_mode=user_creation_mode, user_path_template=user_path_template, user_type=user_type)



UserWriteStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_user_write_stage_list import PaginatedUserWriteStageList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    create_users_as_inactive = True # bool |  (optional)
    create_users_group = 'create_users_group_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    stage_uuid = 'stage_uuid_example' # str |  (optional)
    user_creation_mode = 'user_creation_mode_example' # str |  (optional)
    user_path_template = 'user_path_template_example' # str |  (optional)
    user_type = 'user_type_example' # str |  (optional)

    try:
        api_response = api_instance.stages_user_write_list(create_users_as_inactive=create_users_as_inactive, create_users_group=create_users_group, name=name, ordering=ordering, page=page, page_size=page_size, search=search, stage_uuid=stage_uuid, user_creation_mode=user_creation_mode, user_path_template=user_path_template, user_type=user_type)
        print("The response of StagesApi->stages_user_write_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_write_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_users_as_inactive** | **bool**|  | [optional] 
 **create_users_group** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **stage_uuid** | **str**|  | [optional] 
 **user_creation_mode** | **str**|  | [optional] 
 **user_path_template** | **str**|  | [optional] 
 **user_type** | **str**|  | [optional] 

### Return type

[**PaginatedUserWriteStageList**](PaginatedUserWriteStageList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_write_partial_update**
> UserWriteStage stages_user_write_partial_update(stage_uuid, patched_user_write_stage_request=patched_user_write_stage_request)



UserWriteStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_user_write_stage_request import PatchedUserWriteStageRequest
from authentik_openapi.models.user_write_stage import UserWriteStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this User Write Stage.
    patched_user_write_stage_request = authentik_openapi.PatchedUserWriteStageRequest() # PatchedUserWriteStageRequest |  (optional)

    try:
        api_response = api_instance.stages_user_write_partial_update(stage_uuid, patched_user_write_stage_request=patched_user_write_stage_request)
        print("The response of StagesApi->stages_user_write_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_write_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this User Write Stage. | 
 **patched_user_write_stage_request** | [**PatchedUserWriteStageRequest**](PatchedUserWriteStageRequest.md)|  | [optional] 

### Return type

[**UserWriteStage**](UserWriteStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_write_retrieve**
> UserWriteStage stages_user_write_retrieve(stage_uuid)



UserWriteStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_write_stage import UserWriteStage
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this User Write Stage.

    try:
        api_response = api_instance.stages_user_write_retrieve(stage_uuid)
        print("The response of StagesApi->stages_user_write_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_write_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this User Write Stage. | 

### Return type

[**UserWriteStage**](UserWriteStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_write_update**
> UserWriteStage stages_user_write_update(stage_uuid, user_write_stage_request)



UserWriteStage Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_write_stage import UserWriteStage
from authentik_openapi.models.user_write_stage_request import UserWriteStageRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this User Write Stage.
    user_write_stage_request = authentik_openapi.UserWriteStageRequest() # UserWriteStageRequest | 

    try:
        api_response = api_instance.stages_user_write_update(stage_uuid, user_write_stage_request)
        print("The response of StagesApi->stages_user_write_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_write_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this User Write Stage. | 
 **user_write_stage_request** | [**UserWriteStageRequest**](UserWriteStageRequest.md)|  | 

### Return type

[**UserWriteStage**](UserWriteStage.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stages_user_write_used_by_list**
> List[UsedBy] stages_user_write_used_by_list(stage_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.StagesApi(api_client)
    stage_uuid = 'stage_uuid_example' # str | A UUID string identifying this User Write Stage.

    try:
        api_response = api_instance.stages_user_write_used_by_list(stage_uuid)
        print("The response of StagesApi->stages_user_write_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StagesApi->stages_user_write_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_uuid** | **str**| A UUID string identifying this User Write Stage. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

