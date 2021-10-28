"""config URL Configuration

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
from app.views import CommentViewSet, IssueViewSet, ProjectViewSet
from authentication.views import RegisterView, UserViewSet
from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)


router = routers.SimpleRouter()
router.register('projects', ProjectViewSet, basename='projects')

projects_router = routers.NestedSimpleRouter(router, 'projects', lookup='project')
projects_router.register('issues', IssueViewSet, basename='project_issues')
# projects_router.register('users', UserViewSet, basename='project_users')

issues_router = routers.NestedSimpleRouter(projects_router, 'issues', lookup='issue')
issues_router.register('comments', CommentViewSet, basename='issue_comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('api/', include(router.urls)),
    path('api/', include(projects_router.urls)),
    path('api/', include(issues_router.urls)),
    # path('api/projects/<int:project_pk>/users/', UserViewSet.as_view({'get': 'list', 'post':'create', 'delete': 'destroy'}), name='project_user'),
    path('api/projects/<int:project_pk>/users/', UserViewSet.as_view({'get': 'list'}), name='list_users'),
    path('api/projects/<int:project_pk>/users/<int:user_id>', UserViewSet.as_view({'post':'create', 'delete': 'destroy'}), name='create_delete_user')
]
