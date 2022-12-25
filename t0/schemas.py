from ninja import Schema
#Output Schema for posts
class PostsOut(Schema):
    id: int
    title: str
    text: str

#Input Schema for posts
class PostsIn(Schema):
    id: int
    title: str
    text: str

#Output Schema for outputting a message when a post is created 
class MessageOut(Schema):
    message: str