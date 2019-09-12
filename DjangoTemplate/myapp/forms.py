
from django import forms
# from django.forms.utils import ErrorList

from .models import Post


# class FormPost(forms.Form):
#     title = forms.CharField(max_length=300)
#     contente = forms.CharField(widget=forms.Textarea)


# html_error = """
# <div class="alert alert-danger">
#     <div class="offset-md-1">
#         {content}
#     </div>
# </div>
# """
#
#
# class ErrorList(ErrorList):
#     def __str__(self):
#         """
#             problem, only modify the content (list), not the html field
#         """
#         if not self:
#             return ''
#         return "\n".join([html_error.format(content=e) for e in self])


class FormPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

    def clean_title(self):
        return self.cleaned_data['title'].title()

    # def clean(self):
    #     raise forms.ValidationError("error global")

    # this is already done by Django, the comment is here as a reminder

    # # overwite title to delete unique constaint
    # title = forms.CharField(max_length=300)
    #
    # # handle unique constaint here
    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     post_id = self.data.get('id', None)
    #     if post_id is not None:
    #         try:
    #             post_id = int(post_id)
    #         except ValueError:
    #             raise forms.ValidationError("Yolo id wtf '{}'".format(id))
    #         post = Post.objects.filter(id=post_id).first()
    #         if post.title != title:
    #             if Post.objects.filter(title=title).count() > 0:
    #                 raise forms.ValidationError("Yolo exist elswhere dah!")
    #     else:
    #         if Post.objects.filter(title=title).count() > 0:
    #             raise forms.ValidationError("Yolo exist dude")
    #
    #     # Always return a value to use as the new cleaned data, even if
    #     # this method didn't change it.
    #     return title
