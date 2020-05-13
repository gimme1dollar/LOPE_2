from django.urls import path

from . import views

urlpatterns = [
    path('meme', views.MemeList.as_view()),
    path('detail/meme/<int:meme>', views.MemeDetails.as_view()),
    path('detail/meme/<int:meme>/category/<str:category>', views.meme_category_details)
]
