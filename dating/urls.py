from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'date.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^register/$', 'date.views.register', name='register'),
    url(r'^create_transaction/$', 'date.views.create_transaction', name='transaction'),
    url(r'^payment/$', 'date.views.form', name='payment'),
    url(r'^search_singles/(?P<search_query>\w+)/$', 'date.views.search_singles', name='search_singles'),
    url(r'^confirmation/$', 'date.views.confirmation', name='confirmation'),
    url(r'^payment_error/$', 'date.views.payment_error', name='payment_error'),
    url(r'^profile/$', 'date.views.profile', name='profile'),
    url(r'^questions/$', 'date.views.questions', name='questions'),
    url(r'^data/$', 'date.views.data', name='data'),
    url(r'^singles/$', 'date.views.singles', name='singles'),
    url(r'^singles/(?P<single_id>\w+)/$', 'date.views.single_profile', name='sinlges'),
    url(r'^preferences/$', 'date.views.questions', name='questions'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^chat/$', 'date.views.chat', name='chat'),
    url(r'^match/$', 'date.views.match', name='match'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)