import json

class HttpSuccessResponse():

    def __init__(self, value, error_number = 0, error_message = ""):
        self.Value = value
        self.ClientTransactionID = 0 # TODO
        self.ServerTransactionID = 0 # TODO
        self.ErrorNumber = error_number
        self.ErrorMessage = error_message

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class HttpErrorResponse():

    def __init__(self, error_code, error_message):
        self.ErrorCode = error_code
        self.ErrorMessage = error_message

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
