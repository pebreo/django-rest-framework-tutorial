from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

# # long way
# class SnippetSerializer(serializers.Serializer):
#     'The long way to serialize data'
#     pk = serializers.Field() # Note: 'Field' is an untyped read-only Field
#     title = serializers.CharField(required=False, max_length=100)
#     code = serializers.CharField(widget=widgets.Textarea, max_length=100000)
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     def restore_object(self, attrs, instance=None):
#         """
#         Create or update a new snippet instance, given a dictionary
#         of deserialized field values

#         Note that if we don't define this method, then deserializing
#         data will simply return a dictionary of items
#         """
#         if instance:
#             # Update existing instance
#             instance.title = attrs.get('title',instance.title)
#             instance.code = attrs.get('code',instance.code)
#             instance.linenos = attrs.get('linenos',instance.linenos)
#             instance.language = attrs.get('language',instance.language)
#             instance.style = attrs.get('style',instance.style)
#             return instance

#         return Snippet(**attrs)

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        # note: the highlight field as an URL/Hyperlink as we defined above
        fields = ('url','highlight','owner','title','code','linenos','language','style')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail')

    class Meta:
        model = User
        fields = ('url','username','snippets')


# short way
# class UserSerializer(serializers.ModelSerializer):
#     # Enable serializing the related field snippets
#     # We do this because snippets is a reverse relationship on the User model
#     # it wouldn't be included by default that's why we explicitly do it here
#     snippets = serializers.PrimaryKeyRelatedField(many=True)
#     class Meta:
#         model = User
#         fields = ('id','username','snippets')


# class SnippetSerializer(serializers.ModelSerializer):
#     'The short way to serialize data'
#     # Enable serializing the field
#     owner = serializers.Field(source='owner.username')
#     class Meta:
#         model = Snippet
#         fields = ('id','owner','title','code','linenos','language','style')
