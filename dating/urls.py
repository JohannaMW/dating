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
    url(r'^admin/', include(admin.site.urls)),
    # Forms
#    url(r'^core_beliefs/$', 'date.views.core_beliefs', name='core_beliefs'),
#    url(r'^questions/$', 'date.views.argues', name='argues'),
#    url(r'^questions/$', 'date.views.break_up', name='break_up'),
#    url(r'^questions/$', 'date.views.relation_kind', name='relation_kind'),
#    url(r'^questions/$', 'date.views.relation_last', name='relation_last'),
#    url(r'^questions/$', 'date.views.right_person', name='right_person'),
#    url(r'^questions/$', 'date.views.romance', name='romance'),
#    url(r'^questions/$', 'date.views.status', name='status'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)