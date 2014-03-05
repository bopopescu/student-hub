
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
    #first_name = models.CharField(max_length=20, null=True)
    #last_name = models.CharField(max_length = 20, null=True)
    #user=models.ForeignKey(User)

    class Meta:
    	abstract=True



class Student(UserProfile):
    #ip=models.CharField(max_length=20, null=True, default=None)
    listed=models.CharField(max_length=3, null=True, default='Yes')
    user=models.OneToOneField(User, unique=True, related_name="student")
    degree=models.CharField(max_length=100, default=None, null=True)
    bio= models.TextField(max_length=200, null=True, default=None)
    picture = models.ImageField(upload_to='images/%Y/%m/%d', default=None)
    city=models.CharField(max_length=100, null=True, default=None)
    country=models.CharField(max_length=100, null=True, default=None)
    latitude=models.DecimalField(max_digits=16, decimal_places=13)
    longitude=models.DecimalField(max_digits=16, decimal_places=13)
    facebook_link=models.CharField(max_length=100, null=True, default=None)
	#time slot
	#price
    def __unicode__(self):  # Python 3: def __str__(self):
        return unicode(self.user.last_name) or u''

class Message(models.Model):
	text= models.TextField(max_length=200, null=True)
	sender=models.ForeignKey(Student, related_name="sender")
	receiver=models.ForeignKey(Student, related_name="receiver")

class Skills(models.Model):
	name=models.CharField(max_length=100, default=None, null=True)
	level=models.CharField(max_length=100, default=None, null=True)
	student=models.ForeignKey(Student)


class Review(models.Model):
    text= models.TextField(max_length=200, null=True)
    commenter=models.ForeignKey(Student, related_name="commenter")
    commented=models.ForeignKey(Student, related_name="commented")  

'''
from neo4django.db import models
from neo4django.graph_auth.models import User
class Student(models.NodeModel):
    user = models.Relationship(User,rel_type='auth_info', single=True, related_name='user')
    bio=models.StringProperty()
    degree = models.StringProperty()
    city=models.StringProperty()
    country=models.StringProperty()

class Skills(models.NodeModel):
    name=models.StringProperty()
    level=models.StringProperty()
    student=models.Relationship(Student, 
                                rel_type='knows',
                                single=True,
                                related_name='skill')
class Message(models.NodeModel):
    text=models.StringProperty()
    sender=models.Relationship(Student, rel_type="sends")
    receiver=models.Relationship(Student, rel_type="receives")

class Review(models.NodeModel):
    text=models.StringProperty()
    commenter=models.Relationship(Student, rel_type="comments")
    commented=models.Relationship(Student, rel_type="commented")

    '''

    