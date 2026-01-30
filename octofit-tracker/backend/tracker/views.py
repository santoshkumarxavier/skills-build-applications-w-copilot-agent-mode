from rest_framework import viewsets, permissions
from .models import Activity
from .serializers import ActivitySerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """Simple Activity viewset for CRUD operations."""
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # set current user as owner if authenticated
        if self.request and hasattr(self.request, 'user') and not self.request.user.is_anonymous:
            serializer.save(user=self.request.user)
        else:
            serializer.save()
