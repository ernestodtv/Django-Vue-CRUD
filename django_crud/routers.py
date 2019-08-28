from rest_framework import routers
from notes.viewsets import NoteViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)
router.register(r'users', UserViewSet)
