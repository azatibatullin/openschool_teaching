from rest_framework import routers
from .views import DisciplineViewSet

# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register(r'disciplines', DisciplineViewSet)
# URLs настраиваются автоматически роутером
urlpatterns = router.urls