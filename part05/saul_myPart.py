#listing gen
from faker import Faker


def main():
    fake = Faker()
    for i in range(100):
        uid = fake.unique.random_int(min=1, max=100) 
        mid = fake.unique.random_int(min=1, max=100)    #make range in specialization 1-50 for TB /51-100 for CM
        listPrice = round(fake.pyfloat(2, positive=True), 2)
        quantity = fake.pyint(1, 50)
        material_condition = fake.random_element(elements=('new', 'like new', 'used', 'refurbished'))
        isActive = fake.boolean(chance_of_getting_true=80)
        datePosted = fake.date_between(start_date='-1y', end_date='today')

        print(
            f"INSERT INTO `Listing` (`listingId`, `userId`, `materialId`, `listingPrice`, `quantity`, `material_condition`, `isActive`, `datePosted`) VALUES (NULL, '{uid}', '{mid}', '{listPrice}', '{quantity}', '{material_condition}', '{isActive}', '{datePosted}');"
       )


def Insert_sql_query(tableName):
    pass


if __name__ == "__main__":
    main()



#professor gen
from faker import Faker
def main():
    fake = Faker()
    for i in range(100):
        fname = fake.first_name()
        lname = fake.last_name()
        email = f"{fname.lower()}{lname.lower()}{i}@example.com"
        dept = fake.random_element(elements=('Sales', 'Marketing', 'Engineering', 'HR', 'Finance')) #example departments, change later
        institution = fake.company() + " University"  #example institution, change later (possibly keep simple, all at stan state)
        officeHours = f"{fake.time(pattern='%I:%M %p')} - {fake.time(pattern='%I:%M %p')}"

        print(
            f"INSERT INTO `Professor` (`profId`, `firstName`, `lastName`, `email`, `department`, `institution`, `officeHours`) VALUES (NULL, '{fname}', '{lname}', '{email}', '{dept}', '{institution}', '{officeHours}');"
       )


def Insert_sql_query(tableName):
    pass


if __name__ == "__main__":
    main()


#textbook gen
from faker import Faker


def main():
    fake = Faker()
    for i in range(50):
        mid = fake.unique.random_int(min=1, max=50)    #make range in specialization 1-50/51-100
        ISBN = fake.isbn13(separator='-')
        title = fake.sentence(nb_words=4)
        textbookEdition = fake.random_int(min=1, max=10)
        textbookLanguage = fake.language_name()
        publicationYear = fake.year()
        numberOfPages = fake.random_int(min=50, max=1500)
        imageURL = fake.image_url()
        publId = fake.unique.random_int(min=1, max=100)

        print(
            f"INSERT INTO `Textbook` (`materialId`, `ISBN`, `title`, `textbookEdition`, `textbookLanguage`, `publicationYear`, `numberOfPages`, `imageURL`, `publisherId`) VALUES ('{mid}', '{ISBN}', '{title}', '{textbookEdition}', '{textbookLanguage}', '{publicationYear}', '{numberOfPages}', '{imageURL}', '{publId}');"
       )


def Insert_sql_query(tableName):
    pass


if __name__ == "__main__":
    main()


#publisher gen
from faker import Faker
import re

def main():
    fake = Faker()
    for i in range(100):
        publisherName = fake.company()
        country = fake.country()
        cleanName = re.sub(r'[^a-zA-Z0-9]', '', publisherName).lower() #cleans name for email and website
        email = f"support@{cleanName}.com"
        website_url = f"http://www.{cleanName}.com"
        yearEstablished = fake.year()

        print(
            f"INSERT INTO `Publisher` (`publisherId`, `publisherName`, `country`, `email`, `website_url`, `yearEstablished`) VALUES (NULL, '{publisherName}', '{country}', '{email}', '{website_url}', '{yearEstablished}');"
       )


def Insert_sql_query(tableName):
    pass


if __name__ == "__main__":
    main()