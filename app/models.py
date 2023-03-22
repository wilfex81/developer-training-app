
from django.db import models


# class UserProfile(models.Model):
#     user = models.OneToOneField(User)
#     name = models.CharField(max_length=32)
#     roles = models.ManyToManyField("Role", bank=True, null=True)

#     def __str__(self) -> str:
#         return super().__str__()
    
class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    phone = models.IntegerField(unique=True)
    email = models.EmailField(max_length=100, unique=True)
    

class Course(models.Model):
    '''
    A coure model where facilitators can add
    courses for techies. 
    Techies on the other hand also access
    courses through this model. 
    '''
    
    COURSE_DETAILS = [
        ('Difficulty levels',(
                    ('easy', 'Easy'),
                    ('medium', 'Intermediate'),
                    ('hard', 'Hard'),
                )
            
        ),
        
    ]
    TYPE_OF_COURSE = [
        ('Course Type ',(
                ('instructor-led', 'Instructor-Led'),
                ('on-demand', 'On-Demand'),
                ('both', 'Both'),
            )
            
        ),
    ]
    
    LESSONS_OFFERED=[
         ('Lessons',(
                    ('1', 'Lesson one'),
                    ('2', 'Lesson two'),
                    ('3', 'Lesson three'),
                )
            
        ),
    ]
    ASSESSMENTS=[
          ('Practical Assessment',(
                ('assessment_one', 'Assessment-One'),   
            )   
        ),
    ]
          
    PROGRAMMING_LANGUAGES = [
        ('Programming Languages',(
                    ('java', 'Java'),
                    ('python', 'Python'),
                    ('javascript', 'JavaScript'),
                )
                ),
    ]
    FRAMEWORKS=[
          ('Frameworks',(
                    ('java', 'Spring'),
                    ('python', 'Django'),
                    ('javascript', 'ReactJs'),
                )
               
         ),
    ] 
    title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    course_details = models.CharField(
        max_length=50,
        choices= COURSE_DETAILS
    )
    type_of_course = models.CharField(
        max_length=50,
        choices=TYPE_OF_COURSE
    )
    lessons_offered = models.CharField(
        max_length=50,
        choices= LESSONS_OFFERED
    )
    assessment = models.CharField(
        max_length=50,
        choices= ASSESSMENTS
    )
    programming_languages = models.CharField(
        max_length=50,
        choices= PROGRAMMING_LANGUAGES
    )
    frameworks = models.CharField(
        max_length=50,
        choices=FRAMEWORKS
    )
    price = models.IntegerField(default = 0)
        

    def __str__(self):
        return self.title


class Communitie(models.Model):
    
    CHAMPIONS_LIST = [
        
        'Champions',(
            ('champion1', 'Champion one'),
            ('champion2', 'Champion two'),
            ('champion3', 'Champion three'),
        ),
    ]
    
    
    title = models.CharField(max_length=100)
    champions = models.CharField(max_length=50,
                                 choices = CHAMPIONS_LIST,
                                 default=0),
    upvotes = models.IntegerField(default=0)
    

    def __str__(self):
        return self.title
    

class Project(models.Model):
    PROGRAMMING_LANGUAGES = [
    ('Programming Languages',(
                ('java', 'Java'),
                ('python', 'Python'),
                ('javascript', 'JavaScript'),
            )
            ),
    ]
    FRAMEWORKS=[
          ('Frameworks',(
                    ('java', 'Spring'),
                    ('python', 'Django'),
                    ('javascript', 'ReactJs'),
                )
               
         ),
    ]

    COMPLEXITY = [
        ('Difficulty levels',(
                    ('easy', 'Easy'),
                    ('medium', 'Intermediate'),
                    ('hard', 'Hard'),
                )
            
        ),
        
    ]

    MODULES = [
        ('Modules',(
                    ('module one', 'Module one'),   
                    ('module two', 'Module two'),
                    ('module three', 'Module three'),
                )
            
        ),
        
    ]

    TASKS = [
        ('Tasks Assigned',(
                    ('Task one', 'Task one'),   
                    ('Task two', 'Task two'),
                    ('Task three', 'Task three'),
                )
            
        ),
        
    ]
    
    framework = models.CharField(max_length=100, choices=FRAMEWORKS)
    programming_language = models.CharField(max_length=100, choices=PROGRAMMING_LANGUAGES)
    community = models.ForeignKey(Communitie, on_delete=models.CASCADE, max_length=100)
    complexity = models.CharField(max_length=100, choices=COMPLEXITY)
    modules = models.CharField(max_length=50, choices=MODULES)
    tasks = models.CharField(max_length=100, choices=TASKS)
    
    def __str__(self):
        return self.framework
        
    
class Article(models.Model):
    
    skill = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    project = models.CharField(max_length=100)
    article_details = models.TextField()
    
    def __str__(self):
        return self.skill
    

class Developer(models.Model):
    PROGRAMMING_LANGUAGES = [
        ('Programming Languages',(
                    ('java', 'Java'),
                    ('python', 'Python'),
                    ('javascript', 'JavaScript'),
                )
                ),
    ]
    FRAMEWORKS=[
          ('Frameworks',(
                    ('java', 'Spring'),
                    ('python', 'Django'),
                    ('javascript', 'ReactJs'),
                )
               
         ),
    ] 
    community = models.ForeignKey(Communitie, on_delete = models.CASCADE)
    topic  = models.CharField(max_length=100)
    name = models.CharField(unique=True, max_length=100)
    specialty = models.CharField(max_length=100)
    community = models.CharField(max_length=100)
    programming_language = models.CharField(max_length=100, choices = PROGRAMMING_LANGUAGES)
    framework = models.CharField(max_length=100,choices=FRAMEWORKS)
    
    
    def __str__(self):
        return self.name
    
    