class Database:
    __connection = None

    @classmethod
    def connect(cls):
        if cls.__connection is None:
            server = 'tcp:cisdbss.pcc.edu'
            database = 'NAMES'
            username = '275student'
            password = '275student'
            cls.__connection = pyodbc.connect(
                'DRIVER={SQL Server};SERVER=' + server
                + ';DATABASE=' + database
                + ';UID=' + username + ';PWD=' + password
            )

    @classmethod
    def readNames(cls):
        from Name import Name
        cls.connect()
        cursor = cls.__connection.cursor()
        # ... execute a SQL query and convert the results into a list of Name objects...
        return names




