from django.db import models
from django.contrib.auth.models import User

# модель_Создание пользователя
class Author(models.Model):
    EXECUTER = 'UE'
    AUTHOR_PROJECT = 'AP'
    ROLE_CHOICES = (
        ('UE', 'Executor'),
        ('AP', 'Autor Project'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default=EXECUTER)

# Модель Проекта
class Project(models.Model):
    authr_project = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name='project')
    authr_project_name = models.CharField(max_length=155, blank=True)
    created_time_project = models.DateTimeField(auto_now_add=True)
    updated_time_project = models.DateTimeField(auto_now=True)


    pass

class ProjectStatus(models.Model):
    pass

class ProjectName(models.Model):
    pass

class ProjectContent(models.Model):
    pass

# модель_Задача
class Task(models.Model):
    pass

class TaskLeadTime(models.Model):
    #указание время исполнения задачи в часах
    pass

class TaskStatus(models.Model):
    #статус задачи. возможность менять статус задачи. 
    #статусы: Новая задача, Оценка, В работе, Ожидание ответа, Готово для вырузки, Завершена.
    pass

class TaskProject(models.Model):
    #создание задачи в указанном проекте. т.е. задача должна быть привязана какому-либо проекту
    pass

class TaskName(models.Model):
    #наименование задачи
    pass

class TaskContent(models.Model):
    #описание задачи, возможность прилажить файл или картинку
    pass



# Модель сообщения
class MassageOutcome(models.Model):
    #out_massage
    pass

class MassageIncoming(models.Model):
    #in_massage
    pass

class MassageTask(models.Model):
    #привязан к задаче.
    pass

class MassageDateOfCreation(models.Model):
    pass

class MassageCorrectionDate(models.Model):
    pass