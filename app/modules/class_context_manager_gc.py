class Database:
    def __enter__(self):
        print("Database connection open")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("Database connection closed")


with Database() as db:
    print("Executing database query")
 