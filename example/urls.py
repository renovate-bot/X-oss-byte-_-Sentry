from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    (r'^sentry/', include('sentry.web.urls')),
)
