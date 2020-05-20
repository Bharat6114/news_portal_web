from django import forms
from news_app.models import News 
from news_app.models import Category


class NewsCreateForm(forms.ModelForm):
    CATEGORY_CHOICES = [(category.id, category.title) for category in Category.objects.all()]
    category = forms.MultipleChoiceField(
        required=True, widget=forms.CheckboxSelectMultiple, choices=CATEGORY_CHOICES,
    )

    class Meta:
        model = News
        fields = "title", "content", "cover_image", "category"