class CDEKException(BaseException):
    def __init__(self, code:str=None, message:str=None, status:str=None, *args, **kwargs):
        super(CDEKException, self).__init__(*args, **kwargs)
        self.code = code
        self.message = message
        self.status = status

    def __str__(self):
        return '[%s] %s, status: %s' % (self.code, self.message, self.status)

    def __repr__(self):
        return f'CDEKException: {self}'