from django.db import models

# модель_Создание пользователя
class ClientUser(models.Model):
    pass

# модель_Задача
class TaskPerformer(models.Model):
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

# Модель Проекта
class ProjectAuthor(models.Model):
    pass

class ProjectStatus(models.Model):
    pass

class ProjectName(models.Model):
    pass

class ProjectContent(models.Model):
    pass