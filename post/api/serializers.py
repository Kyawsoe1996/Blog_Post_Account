from django.contrib.auth import models
from django.db.models import fields
from .standard_views_import import *
from post.models import Post,Comment,ReplyComment
from account.api.serializers import AccountSerializer
from account.models  import Account

class SampleAccountSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id']

class PostSerializers(serializers.ModelSerializer):
    # like_by = AccountSerializer(many=True)
    like_by = SampleAccountSerialzier
    class Meta:
        model = Post
        fields = ['id', 'title', 'description','like_by','post_likes_count']

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','post','comment_text','user','likes','coment_likes_count']
    

    #Create For the user u give in the post request of the body (Sinppet POST REQ)
    def create(self, validated_data,*args,**kwargs):
       
        return super(CommentSerializers,self).create(validated_data)
       
    #     owner = validated_data.pop("owner")
    #     acc = User.objects.get(username=owner['username'])
    #     validated_data['owner'] =acc
    #     return super(SnippetSerializer,self).create(validated_data)
    
    # def create(self,request):
    #     import pdb;pdb.set_trace()
       
    #     files = {'thumb': open('D:/thumb.jpg', 'rb'), 'preview': open('D:/preview.jpg', 'rb')}

    #     print("GG")
    #     pass

class ReplyCommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReplyComment
        fields = ['id','reply_text','comment','user','likes_by','reply_likes_count']
    

