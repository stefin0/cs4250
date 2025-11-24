from faker import Faker


def main():
    fake = Faker()
    for i in range(100):
        fname = fake.first_name()
        lname = fake.last_name()
        email = f"{fname.lower()}{lname.lower()}{i}@example.com"
        print(
            f"INSERT INTO `Author` (`authorId`, `firstName`, `lastName`, `affiliation`, `biography`, `email`) VALUES (NULL, '{fname}', '{lname}', 'affiliation', 'biography', '{email}');"
        )


def Insert_sql_query(tableName):
    pass


if __name__ == "__main__":
    main()
