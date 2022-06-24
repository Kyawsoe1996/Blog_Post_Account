from post.models import Post
from post.models import Comment
from post.models import ReplyComment

post = Post.objects.all()[0]

#getting alll comments base on this post,
 comment = post.comments.all()

#getting the user lists who like that comment
post.comments.all()[0].likes.all()


#post's comment likes total count
post.comments.all()[0].like_count


API for blog post,
1. get all posts, 'done'
2.add_post ('not mandatory'),'done'
3.get_post_detail,   'done'
4.get_each_post_comments 'done'
5.post comment on each post
6.like comment
7.reply comment
8.reply comment like








