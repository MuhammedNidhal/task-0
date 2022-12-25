from typing import List # this is used to display the list of posts
from django.contrib import admin # for admin panel
from django.urls import path # for paths and api urls
from ninja import NinjaAPI # for API endpoint creation and testing
from t0.schemas import * # importing output and input schemas
from t0.models import * # for requests on the database models
from ninja.security import APIKeyHeader # for security and API keys

# Simple Authentication using  a header api key
class ApiKey(APIKeyHeader):
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        if key == "Muhammed":
            return key


header_key = ApiKey()

api = NinjaAPI(auth=header_key) # naming the ninja API "api" and giving all endpoints the auth method

#getting all posts endpoint
@api.get("/posts", response=List[PostsOut])
def get(request):
    posts = Post.objects.all()
    return posts

#creating a new post
@api.post("/posts",response= MessageOut)
def post(request, post_in: PostsIn):
    Post.objects.create(
        id = post_in.id,
        title = post_in.title,
        text = post_in.text,
    )
    return {"message": "Post Created!"}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls) #telling the program to register our API urls
]
