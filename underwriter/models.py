from django.db import models


class UnderwriterManager(models.Manager):
    pass  # add your custom methods here


class Underwriter(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    ceo_name = models.CharField(max_length=100)
    ceo_phone_number = models.CharField(max_length=20)
    ceo_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UnderwriterManager()  # add the manager here

    def __str__(self):
        return self.company_name


class ClientManager(models.Manager):
    pass  # add your custom methods here


class Client(models.Model):
    client_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ClientManager()  # add the manager here

    def __str__(self):
        return self.client_name


class ClassDef(models.Model):
    class_of_Business = models.CharField(max_length=50, verbose_name='Business', help_text='Enter class of Business')
    percentage_of_brokerage = models.DecimalField(max_digits=4, decimal_places=2)

    class VATable(models.Model):
        VAT_CHOICES = (
            ('Y', 'YES'),
            ('N', 'NO'),
        )

        gender = models.CharField(max_length=1, choices=VAT_CHOICES)

    class PolicySchedule(models.Model):
        POLICY_CHOICES = (
            ('Y', 'YES'),
            ('N', 'NO'),
        )

        schedule = models.CharField(max_length=1, choices=POLICY_CHOICES)

    class AvailableClasses(models.Model):
        AVAILABLE_CLASSES = (
            ('A', 'MOTOR'),
            ('B', 'FIRE AND BURGLAR'),
            ('C', 'FIRE AND SPECIAL PERIL'),
            ('D', 'MARINE CARGO'),
            ('E', 'MARINE HULL'),
            ('F', 'TERRORISM'),
            ('G', 'LIFE'),
            ('H', 'OTHERS'),
        )

        classes = models.CharField(max_length=50)
        available = models.CharField(max_length=2, choices=AVAILABLE_CLASSES)

        def __str__(self):
            return self.class_of_Business
