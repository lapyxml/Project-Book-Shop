from django.urls import path
from manager.views import MyPage, AddLike2Comment, AddRate2Book, BookDetail, AddBook, AddComment, logout_user, \
    UpdateComment, comment_delete, RegisterView
from manager.views import LoginView, book_delete, UpdateBook

urlpatterns = [
    path("add_like_to_comment/<int:id>/<str:slug>/", AddLike2Comment.as_view(), name="add-like-to-comment"),
    path("add_rate_to_book/<str:slug>/<int:rate>/", AddRate2Book.as_view(), name="add-rate"),
    path("add_rate_to_book/<str:slug>/<int:rate>/<str:location>/",
         AddRate2Book.as_view(), name="add-rate-location"),
    path("book_view_detail/<str:slug>/", BookDetail.as_view(), name="book-detail"),
    path("add_book/", AddBook.as_view(), name="add-book"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("add_comment/<str:slug>/", AddComment.as_view(), name="add-comment"),
    path("delete_book/<str:slug>/", book_delete, name="delete-book"),
    path("update_book/<str:slug>/", UpdateBook.as_view(), name="update-book"),
    path("update_comment/<int:id>/", UpdateComment.as_view(), name="update-comment"),
    path("delete_comment/<int:id>/", comment_delete, name="delete-comment"),
    path("register/", RegisterView.as_view(), name="register"),
    path("", MyPage.as_view(), name="the-main-page"),
]
