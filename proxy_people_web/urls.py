"""proxy_people_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,patterns
from django.contrib import admin
from main_app.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^web_test/$',web_test,name="api_test"),
    url(r'^api/admin_proxy_account_add_api/$',admin_proxy_account_add_API,name='admin_proxy_account_add_API'),
    url(r'^api/admin_proxy_account_topup/$',admin_proxy_account_topup,name='admin_proxy_account_topup'),
    url(r'^api/get_all_software/$',get_all_software,name='get_all_software'),
    url(r'^api/get_all_software_TOKEN/$', get_all_software_TOKEN, name='get_all_software_TOKEN'),
    url(r'^api/admin_proxy_account_balance_setup/$',admin_proxy_account_balance_setup,name='admin_proxy_account_balance_setup'),
    url(r'^api/proxy_account_balance_check/$',proxy_account_balance_check,name='proxy_account_balance_check'),
    url(r'^api/proxy_account_login/$',proxy_account_login,name='proxy_account_login'),
    url(r'^api/proxy_account_change_password/$',proxy_account_change_password,name='proxy_account_change_password'),
    url(r'^api/admin_proxy_account_change_password/$',admin_proxy_account_change_password,name='admin_proxy_account_change_password'),
    url(r'^api/proxy_account_ad_change/$',proxy_account_ad_change,name='proxy_account_ad_change'),
    url(r'^api/proxy_info_get/$',proxy_info_get,name='proxy_info_get'),
    url(r'^api/admin_set_software/$',admin_set_software,name='admin_set_software'),
    url(r'^api/admin_update_software_version/$',admin_update_software_version,name='admin_update_software_version'),
    url(r'^api/admin_update_software_cost/$',admin_update_software_cost,name='admin_update_software_cost'),
    url(r'^api/proxy_get_software_code/$',proxy_get_software_code,name='proxy_get_software_code'),
    url(r'^api/authorization_make/$',authorization_make,name='authorization_make'),
    url(r'^api/authorization_check/$',authorization_check,name='authorization_check'),
    url(r'^api/authorization_change/$',authorization_change,name='authorization_change'),
    url(r'^$',index_page,name='index'),
    url(r'^accounts/login/$',login_view,name='login'),
    url(r'^accounts/logout/$',log_out_view,name='logout'),
    url(r'^accounts/register/$',reg,name='register'),
    url(r'^shop/$',shop_page,name='shop'),
    url(r'^shop/item/(?P<software_id>[0-9]+)/$',shop_detail,name="shop_detail"),
    url(r'^shop/item/buy_items/$',buy_items,name='buy_items'),
    url(r'^shop/check_deal/(?P<deal_code>[0-9]+)/$',check_deal,name="check_deal"),
    url(r'^shop/check_all_deal/$',check_all_deal,name='check_all_deal'),
    url(r'^profile_setting/$',profile_setting,name='profile_setting'),
    url(r'^check_all_auth/$',check_all_auth,name='check_all_auth'),
    url(r'^check_auth/(?P<pk>[0-9]+)/$',check_auth,name='check_auth'),
    url(r'^check_all_down_proxy/$',check_all_down_proxy,name='check_all_down_proxy'),
    url(r'^change_down_proxy_info/(?P<pk>[0-9]+)/$',change_down_proxy_info,name='change_down_proxy_info'),
]

urlpatterns +=patterns('',
                        url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
                        url(r'^static/<?P<path>.*>$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
                       )