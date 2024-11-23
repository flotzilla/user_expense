from rest_framework import serializers

from .models import Expense, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Expense amount must be positive.")
        return value
