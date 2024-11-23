from django.urls import path

from .views import (
    CategorySummaryView,
    ExpenseByDateRangeView,
    ExpenseDetailView,
    ExpenseListCreateView,
    UserDetailView,
    UserListCreateView,
)

urlpatterns = [
    path("users/", UserListCreateView.as_view(), name="user-list-create"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("expenses/", ExpenseListCreateView.as_view(), name="expense-list-create"),
    path("expenses/<int:pk>/", ExpenseDetailView.as_view(), name="expense-detail"),
    path("expenses/<int:user_id>/<str:start_date>/<str:end_date>/", ExpenseByDateRangeView.as_view(),
         name="expense-by-date-range"),
    path("expenses/<int:user_id>/summary/<int:year>/<int:month>/", CategorySummaryView.as_view(),
         name="category-summary"),
]