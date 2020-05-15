from django.urls import path

from . import views

urlpatterns = [
    path('meme', views.MemeList.as_view()),
    path('meme/<int:id>', views.MemeDetail.as_view()),
    path('detail/meme/<int:meme>', views.MemeDetails.as_view())
]
