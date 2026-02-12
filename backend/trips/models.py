from django.db import models

class TravelProject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    
    is_completed = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class Place(models.Model):
    project = models.ForeignKey(
        TravelProject, 
        on_delete=models.CASCADE, 
        related_name='places'
    )
    
    external_id = models.PositiveIntegerField()
    
    notes = models.TextField(blank=True, default='')

    is_visited = models.BooleanField(default=False)

    class Meta:
        unique_together = ('project', 'external_id')
        ordering = ['pk']

    def __str__(self):
        return f"ArtID: {self.external_id} (Project: {self.project.name})"