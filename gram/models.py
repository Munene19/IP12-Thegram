from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_photo = models.ImageField()
    Bio = models.CharField(max_length=40)
    followers = models.ManyToManyField('Profile',related_name="followers_profile",blank=True) 
    following = models.ManyToManyField('Profile',related_name="following_profile",blank=True) 
    
    def get_number_of_followers(self):
        print(self.followers.count())
        if self.followers.count():
            return self.followers.count()
        else:
            return 0    
    def get_number_of_following(self):
        print(self.following.count())
        if self.following.count():
            return self.following.count()
        else:
            return 0 

    def __str__(self): 
        return f'{self.user.username} Profile'
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
    
    @classmethod   
    def update_bio(cls,id,new_bio):
        cls.objects.filter(pk = id).update(bio=new_bio)
        new_bio_object = cls.objects.get(bio = new_bio)
        new_bio = new_bio_object.bio
        return new_bio



class Comments(models.Model):
    comment = models.CharField(max_length=100,blank=True,primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # image = models.ForeignKey(Image,on_delete=models.CASCADE)
    dateposted = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(image__id=id)
        return comments
    
    def save_comment(self):
        self.save()
    
    def __str__(self):
        
        return self.comment
        
    
    


class Image(models.Model): #posts
    image = models.ImageField()
    image_caption = models.TextField(max_length=40)
    user= models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    likes = models.IntegerField(default=0, null=True)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE,null=True)
    dateposted = models.DateTimeField(auto_now=True)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    @classmethod    
    def update_caption(cls,id,new_caption):
        cls.objects.filter(pk = id ).update(image_caption = new_caption)
        new_caption_object = cls.objects.get(image_caption=new_caption)
        new_caption = new_caption_object.image_caption
        return new_caption
    
    @classmethod
    def get_single_photo(cls,id):
        image = cls.objects.get(pk=id)
        return image

    @classmethod
    def update_image(cls,current_value,new_value):
        fetched.object = Image.objects.filter(author=current_value)

class Like(models.Model):
    post = models.ForeignKey('Image')
    user = models.ForeignKey(User)
    class Meta:
        unique_together = ("post", "user")
    def __str__(self):
        return 'Like: ' + self.user.username + ' ' + self.post.title

    @classmethod
    def search_by_username(cls,search_term):
        search_result = cls.objects.filter(user__username__icontains=search_term)
        return search_result

    def save_profile(self):
        self.save()
    
    # def __str__(self):     
    #     return self.image_name
class Followers(models.Model):
    user = models.CharField(max_length=20,default='')
    Follower = models.CharField(max_length=20,default='')