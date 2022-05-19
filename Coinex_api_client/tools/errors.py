

class ArgumentTypeErr(Exception):
    def __init__(self, argument_name, argument_type):
        super().__init__(f"The argument {argument_name} needs to be {argument_type}.")

class ArgumentValueErr(Exception):
    def __init__(self, argument_name, values):
        super().__init__(f"The argument {argument_name} needs to {values}")

class ParamCheckError(Exception):
    def __init__(self, errors):
        errors_listing = "\n".join(errors)
        super().__init__(f"The parameter check has found the following errors:\n{errors_listing}")

class AuthenticationError(Exception):
    def __init__(self, endpoint_name):
        super().__init__(f"The {endpoint_name} endpoint requires authentication. The access_id and secret_key configs must not be None or empty string")