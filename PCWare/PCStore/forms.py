from django.forms import ModelForm, ModelChoiceField
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction


class CategoryChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.categoryName


class ProductCategoryForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = {'categoryName', 'categoryDetails'}


class ProductForm(ModelForm):
    category = CategoryChoiceField(queryset=ProductCategory.objects.all())
    class Meta:
        model = Product
        fields = {"productName", "productDetails", "category", "stock", "price", "picture"}


class UserSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.isAdmin = False
        user.save()
        return user


class UserLoginForm(AuthenticationForm):
    def __init_(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    username = forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '', 'id': 'howdy'}))
