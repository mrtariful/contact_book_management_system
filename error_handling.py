def validate_contact(name, phone):
    if not name.isalpha():
        print("Error: Name must contain only letters.")
        return False
    if not phone.isdigit():
        print("Error: Phone number must be numeric.")
        return False
    return True
