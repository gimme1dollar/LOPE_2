from django.urls import path

from . import views

urlpatterns = [
    path('meme', views.MemeInfo.as_view()),
    path('meme/<str:phase>', views.MemeList.as_view()),
    path('meme/<int:id>', views.MemeDetail.as_view()),
    path('property/meme/<int:meme>', views.MemeProperty.as_view()),
    path('detail/meme/<int:meme>', views.MemeDetails.as_view())
]
