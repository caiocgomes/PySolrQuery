class RequiredParamException(Exception):
    def __init__(self, parameterList):
        message = "The required parameters {parameterList} is missing.".format(**locals())
        Exception.__init__(self, message)
