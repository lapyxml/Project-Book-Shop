from django.urls import path
from manager.views import hello, MyPage, AddLike2Comment, AddRate2Book, BookDetail, AddBook, AddComment, logout_user
from manager.views import LoginView

urlpatterns = [
    path("hello/<int:digit>/", hello),
    path('hello/<str:name>/', hello),
    path('hello/', hello),
    path("add_like_to_comment/<int:id>/<str:slug>/", AddLike2Comment.as_view(), name="add-like-to-comment"),
    path("add_rate_to_book/<str:slug>/<int:rate>/", AddRate2Book.as_view(), name="add-rate"),
    path("add_rate_to_book/<str:slug>/<int:rate>/<str:location>/",
         AddRate2Book.as_view(), name="add-rate-location"),
    path("book_view_detail/<str:slug>/", BookDetail.as_view(), name="book-detail"),
    path("add_book/", AddBook.as_view(), name="add-book"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("add_comment/<str:slug>/", AddComment.as_view(), name="add-comment"),
    path("", MyPage.as_view(), name="the-main-page"),
]
