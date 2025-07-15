from django.core.exceptions import ValidationError

def validate_no_bug_in_summary(value):
    if "bug" in value.lower():
        raise ValidationError("Название не должно содержать слово 'bug'.")

def validate_summary_length(value):
    if len(value.strip()) < 3:
        raise ValidationError("Название должно содержать не менее 3 символов.")