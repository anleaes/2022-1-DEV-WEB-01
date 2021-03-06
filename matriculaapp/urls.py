"""matriculaapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('cursos/', include('cursos.urls', namespace='cursos')),
    path('areadeconhecimento/', include('areadeconhecimento.urls', namespace='areadeconhecimento')),
    path('disciplinas/', include('disciplinas.urls', namespace='disciplinas')),
    path('alunos/', include('alunos.urls', namespace='alunos')),
    path('matriculas/', include('matriculas.urls', namespace='matriculas')),
    path('contas/', include('accounts.urls', namespace='accounts')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
