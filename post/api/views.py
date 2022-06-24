
from post.api.standard_views_import import *
from post.models import Post,Comment,ReplyComment
from account.models import Account
from .serializers import PostSerializers,CommentSerializers,ReplyCommentSerializer

def custom_view(request):
    return JsonResponse({"data":"success"})

class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    #adding after post detail comment to find post's all comments => 23.09.2021,  9:08pm at home
    #E.g => http://localhost:8000/api/post/posts/4/comments/ 
    @action(detail=True,methods=['get','post'])
    def comments(self,request,pk=None):
        post = self.get_object()
        if request.method == 'GET':
            comments = post.comments.all()
            
            serializer = CommentSerializers(comments, many=True)
            return Response(serializer.data)
        else:
            
            data = request.data
         
            data = data.update({"post":post.id})
          
           
            try:
                user_id = request.data.get('user')
                account_obj = Account.objects.get(id=user_id)
            except:
                raise serializers.ValidationError({'error':"User does not exists"}) 
            
            serializer = CommentSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            # return Response({"success":"Comment Posted "})
            #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            #check if not serializer is not valid
            raise serializers.ValidationError({'error':"Something went wrong.. It may be post id"})
       
    @action(detail=True,methods=['post'])
    def like_post(self,request,pk=None):
        print("Like The post")
        post = self.get_object()
        if not request.data.get('user'):
            raise serializers.ValidationError({'error':"You need to login"})
        
        try:
                user_id = request.data.get('user')
                account_obj = Account.objects.get(id=user_id)
        except:
                raise serializers.ValidationError({'error':"User does not exists"})

        if account_obj in post.like_by.all():
            return JsonResponse({"successs":"You have already liked the post"})
        else:
            post.like_by.add(account_obj)
            post.post_likes_count +=1 
            post.save()
        
        
        data = {"success":"Successfully like the post"}
        return Response(data)
    

@api_view(['GET','POST'])
def replyComment(request,**kwargs):
    print(kwargs,"####")
    post_id = kwargs.get('postid')
    comment_id =kwargs.get('commentid')
    post_obj = Post.objects.get(id=post_id)
    if request.method == 'GET':
        comment_obj = post_obj.comments.filter(id=comment_id)
        

        all_replies  = comment_obj[0].replies.all()
        serializer = ReplyCommentSerializer(all_replies,many=True)
        return Response(serializer.data)
    else:
        if not request.data.get('user'):
            raise serializers.ValidationError({'error':"You need to login"})
        data = request.data
        print(data,"######")

        serializer = ReplyCommentSerializer(data=request.data)
        print(serializer,"#####")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        raise serializers.ValidationError({'error':"Something went wrong"})

        
        # return Response({"success":"posted"})



