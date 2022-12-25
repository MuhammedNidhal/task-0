from ninja import Schema
class PostsOut(Schema):
    id: int
    title: str
    text: str
    
class PostsIn(Schema):
    id: int
    title: str
    text: str
    
class MessageOut(Schema):
    message: str