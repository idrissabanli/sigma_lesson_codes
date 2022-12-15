from django import forms
from stories.models import Comment, Recipe, Tag


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'content',
        )


class RecipeForm(forms.ModelForm):
    tag_list = forms.CharField(widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tags'
            }), max_length=300)

    class Meta:
        model = Recipe
        fields = [
            'title',
            'category',
            'short_description',
            'description',
            'image',
            'cover_image',
            # 'tags',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'category'
            }),
            'short_description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Short description'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
            # 'tags': forms.SelectMultiple(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'tags'
            # })
        }

    def save(self, commit=True):
        recipe = super().save(commit)
        tag_list = self.cleaned_data['tag_list'].split()
        tags = list(filter(lambda word: word.startswith('#'), tag_list))
        print('here')
        recipe.tags.clear()
        print('here2')
        print(recipe.tags.all())
        # for tag in tags:
        #     tag_object, created = Tag.objects.get_or_create(title=tag[1:])
        recipe.tags.add(Tag.objects.first())
        # recipe = super().save(commit)
        return recipe