from django.forms import ModelForm, TextInput, Textarea, CharField, PasswordInput, SelectMultiple
from manager.models import Book, Comment
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(widget=TextInput(attrs={'autofocus': True, "class": "form-control"}))
    password = CharField(
        label="Password",
        strip=False,
        widget=PasswordInput(attrs={'autocomplete': 'current-password', "class": "form-control"}),
    )


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        pass

    username = UsernameField(widget=TextInput(attrs={"class": "form-control"}))
    password1 = CharField(
        label="Password",
        strip=False,
        widget=PasswordInput(attrs={'autocomplete': 'new-password', "class": "form-control"}),
    )
    password2 = CharField(
        label="Password confirmation",
        widget=PasswordInput(attrs={'autocomplete': 'new-password',"class": "form-control"}),
        strip=False
    )


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "text", "genre", "book_image"]
        widgets = {
            "title": TextInput(attrs={"class": "form-control"}),
            "text": Textarea(attrs={"class": "form-control", "rows":5, "cols":50}),
            "genre": SelectMultiple(attrs={"class":"form-control"})
        }
        help_texts = {
            "title": "",
            "text": ""
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            "text": Textarea(attrs={"class":"form-control", "rows":5, "cols": 50})
        }
        help_texts = {
            "text": ""
        }