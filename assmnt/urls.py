from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'assmnt.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
# )
urlpatterns = [
    url(r'^', include('indeetv.urls')),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    # url(r'^admin/', include(admin.site.urls)),

    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)