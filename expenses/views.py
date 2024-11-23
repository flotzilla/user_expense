from django.db.models import Sum
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics

from .models import Expense, User
from .serializers import ExpenseSerializer, UserSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of all users or create a new user.",
        responses={
            200: UserSerializer(many=True),
            201: UserSerializer,
            400: "Bad Request",
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new user.",
        responses={
            201: UserSerializer,
            400: "Bad Request",
        },
        request_body=UserSerializer
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_description="Retrieve, update or delete a specific user.",
        responses={
            200: UserSerializer,
            400: "Bad Request",
            404: "Not Found",
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update details of a specific user.",
        responses={
            200: UserSerializer,
            400: "Bad Request",
        },
        request_body=UserSerializer
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a specific user.",
        responses={
            204: "No Content",
            404: "Not Found",
        },
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of expenses or create a new expense.",
        responses={
            200: ExpenseSerializer(many=True),
            201: ExpenseSerializer,
            400: "Bad Request",
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new expense entry.",
        responses={
            201: ExpenseSerializer,
            400: "Bad Request",
        },
        request_body=ExpenseSerializer
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    @swagger_auto_schema(
        operation_description="Retrieve, update or delete a specific expense.",
        responses={
            200: ExpenseSerializer,
            400: "Bad Request",
            404: "Not Found",
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update an existing expense.",
        responses={
            200: ExpenseSerializer,
            400: "Bad Request",
        },
        request_body=ExpenseSerializer
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a specific expense.",
        responses={
            204: "No Content",
            404: "Not Found",
        },
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class ExpenseByDateRangeView(generics.ListAPIView):
    serializer_class = ExpenseSerializer

    @swagger_auto_schema(
        operation_description="Retrieve all expenses for a user within a specific date range.",
        responses={
            200: ExpenseSerializer(many=True),
            400: "Bad Request",
            404: "Not Found",
        }
    )
    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        start_date = self.kwargs["start_date"]
        end_date = self.kwargs["end_date"]
        return Expense.objects.filter(
            user_id=user_id,
            date__range=[start_date, end_date]
        )

class CategorySummaryView(generics.GenericAPIView):
    @swagger_auto_schema(
        operation_description="Retrieve the total expenses per category for a given month.",
        responses={
            200: "Category total expenses summary",
            400: "Bad Request",
            404: "Not Found",
        }
    )
    def get(self, request, user_id, year, month):
        expenses = (
            Expense.objects.filter(
                user_id=user_id,
                date__year=year,
                date__month=month
            )
            .values("category")
            .annotate(total=Sum("amount"))
            .order_by("category")
        )
        return JsonResponse(list(expenses), safe=False)
