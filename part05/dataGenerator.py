import random
import re

from faker import Faker

fake = Faker()


def escape_sql_string(value):
    if isinstance(value, str):
        value = value.replace("'", "''")
        value = value.replace("\n", " ").replace("\r", " ")
    return value


def generate_courses(file, num_courses=100):
    for course_id in range(1, num_courses + 1):
        courseName = f"CourseName {course_id}"
        department = fake.random_element(elements=("CS", "Math", "Physics", "History"))
        courseDescription = fake.paragraph(nb_sentences=3, variable_nb_sentences=True)
        prerequisite = f"CourseName {course_id}"
        units = random.randint(0, 5)

        file.write(
            f"INSERT INTO `Course` (`courseId`, `courseName`, `department`, `courseDescription`, `prerequisite`, `units`) VALUES (NULL, '{courseName}', '{department}', '{courseDescription}', '{prerequisite}', '{units}');\n"
        )

def generate_course_material(file, num_course_material=100):
    for materialId in range(1, num_course_material + 1):
        materialDescription = fake.paragraph(nb_sentences=4, variable_nb_sentences=True)
        isRequired = random.randint(0,1)
        msrp = fake.pricetag()[1:]
        materialName = fake.word()

        # for ints, remove back ticks or not (idk)
        file.write(
            f"INSERT INTO `CourseMaterial` ( `materialID`, `dateAdded`, `materialDescription`, `isRequired`, `msrp`, `materialName`) VALUES (NULL, NULL, '{materialDescription}', '{isRequired}', '{msrp}', '{materialName}');\n"
        )

def generate_course_supplies(file):
    for materialId in range(1, 51):
        brand = fake.word()
        height = random.randint(1, 30)
        width = random.randint(1, 25)
        itemLength = random.randint(1, 30)
        itemWeight = random.randint(1, 30)

        file.write(
            f"INSERT INTO `CourseSupplies` (`materialId`, `brand`, `height`, `width`, `itemLength`, `itemWeight`) VALUES ('{materialId}', '{brand}', '{height}', '{width}', '{itemLength}', '{itemWeight}' );\n"
        )


def generate_app_users(file, num_users=50):
    for userId in range(1, num_users + 1):
        email = fake.unique.email()
        password_hash = fake.md5()
        first_name = fake.first_name()
        last_name = fake.last_name()
        is_verified = random.randint(0,1)
        overallRating = round(random.uniform(0, 10), 1)
        responseTimeMinutes = random.randint(1, 10080)  # One week in minutes
        returnPolicy = fake.paragraph(nb_sentences=7, variable_nb_sentences=True)
        sellerBio = fake.paragraph(nb_sentences=7, variable_nb_sentences=True)
        phoneNumber = fake.basic_phone_number()

        file.write(
            f"INSERT INTO `AppUser` (`userId`, `email`, `passwordHash`, `firstName`, `lastName`, `isVerified`, `overallRating`, `responseTimeMinutes`, `returnPolicy`, `sellerBio`, `phoneNumber`, `dateJoined`) VALUES (NULL, '{email}', '{password_hash}', '{first_name}', '{last_name}', '{is_verified}', '{overallRating}', '{responseTimeMinutes}', '{returnPolicy}', '{sellerBio}', '{phoneNumber}', NULL );\n"
        )

def generate_listings(file, num_listing=50):
    for listingId in range(1, num_listing + 1):
        userId = random.randint(1, 50)
        materialId = random.randint(
            1, 50
        )  # make range in specialization 1-25 for TB /26-50 for CM
        listPrice = round(fake.pyfloat(2, positive=True), 2)
        quantity = fake.pyint(1, 50)
        material_condition = fake.random_element(
            elements=("New", "Like New", "Used", "Worn", "Well Worn")
        )
        isActive = random.randint(0,1)

        file.write(
            f"INSERT INTO `Listing` (`listingId`, `userId`, `materialId`, `listingPrice`, `quantity`, `material_condition`, `isActive`, `datePosted`) VALUES (NULL, '{userId}', '{materialId}', '{listPrice}', '{quantity}', '{material_condition}', '{isActive}', NULL);\n"
        )


def generate_professors(file, num_professors=50):
    for profId in range(1, num_professors + 1):
        fname = fake.first_name()
        lname = fake.last_name()
        email = f"{fname.lower()}{lname.lower()}{profId}@example.com"
        dept = fake.random_element(
            elements=("Sales", "Marketing", "Engineering", "HR", "Finance")
        )  # example departments, change later
        institution = (
            fake.company() + " University"
        )  # example institution, change later (possibly keep simple, all at stan state)
        officeHours = (
            f"{fake.time(pattern='%I:%M %p')} - {fake.time(pattern='%I:%M %p')}"
        )

        file.write(
            f"INSERT INTO `Professor` (`profId`, `firstName`, `lastName`, `email`, `department`, `institution`, `officeHours`) VALUES (NULL, '{fname}', '{lname}', '{email}', '{dept}', '{institution}', '{officeHours}');\n"
        )


def generate_publishers(file, num_publishers=50):
    for publisherId in range(1, num_publishers + 1):
        publisherName = fake.company()
        country = escape_sql_string(fake.country())
        cleanName = re.sub(
            r"[^a-zA-Z0-9]", "", publisherName
        ).lower()  # cleans name for email and website
        email = f"support@{cleanName}.com"
        website_url = f"http://www.{cleanName}.com"
        yearEstablished = fake.year()

        file.write(
            f"INSERT INTO `Publisher` (`publisherId`, `publisherName`, `country`, `email`, `website_url`, `yearEstablished`) VALUES (NULL, '{publisherName}', '{country}', '{email}', '{website_url}', '{yearEstablished}');\n"
        )


def generate_textbook(file):
    for materialId in range(51, 101): # textbook ids are from 51-100
        ISBN = fake.isbn13(separator="-")
        title = fake.sentence(nb_words=4)
        textbookEdition = fake.random_int(min=1, max=10)
        textbookLanguage = fake.language_name()
        publicationYear = fake.year()
        numberOfPages = fake.random_int(min=50, max=1500)
        imageURL = fake.image_url()
        publId = fake.unique.random_int(min=1, max=50)

        file.write(
            f"INSERT INTO `Textbook` (`materialId`, `ISBN`, `title`, `textbookEdition`, `textbookLanguage`, `publicationYear`, `numberOfPages`, `imageURL`, `publisherId`) VALUES ('{materialId}', '{ISBN}', '{title}', '{textbookEdition}', '{textbookLanguage}', '{publicationYear}', '{numberOfPages}', '{imageURL}', '{publId}');\n"
        )


def generate_authors(file, num_authors=50):
    for authorId in range(num_authors):
        fname = escape_sql_string(fake.first_name())
        lname = escape_sql_string(fake.last_name())
        email = f"{fname.lower()}{lname.lower()}{authorId}@example.com"
        affiliation = escape_sql_string(fake.company())
        biography = escape_sql_string(fake.text())

        file.write(
            f"INSERT INTO `Author` (`authorId`, `firstName`, `lastName`, `affiliation`, `biography`, `email`) VALUES (NULL, '{fname}', '{lname}', '{affiliation}', '{biography}', '{email}');\n"
        )


def generate_sections(file):
    for courseId in range(1, 101):
        #commented out for fixes, made sectionNumber and semesters as constants
        # sectionNumber = random.randint(1, 4)
        # semester = random.choice(["Spring", "Summer", "Fall", "Winter"])
        capacity = random.choice([30, 45, 60, 120])
        delivery = random.choice(["In-Person", "Online", "Hybrid"])
        room = random.randint(100, 500)
        days = random.choice(["MWF", "TuTh", "Mon", "Wed"])
        hour = random.randint(8, 18)
        time_block = f"{days} {hour}:00-{hour+1}:00"

        file.write(
            f"INSERT INTO `Section` (`courseId`, `sectionNumber`, `semester`, `capacity`, `deliveryMethod`, `roomNumber`, `timeBlock`) VALUES ('{courseId}', '1', 'Spring', '{capacity}', '{delivery}', '{room}', '{time_block}');\n"
        )


def generate_section_professors(file):
    for i in range(1, 51):
        course_id = i
        #commented out for fixes, made sectionNumber and semesters as constants
        # semester = random.choice(["Spring", "Summer", "Fall", "Winter"])
        #sectionNumber = random.randint(1, 4)
        prof_id = i
        file.write(
            f"INSERT INTO `SectionProfessor` (`courseId`, `sectionNumber`, `semester`, `profId`) VALUES ('{course_id}', '1', 'Spring', '{prof_id}');\n"
        )


def generate_section_course_materials(file):
    for i in range(1, 101):
        course_id = i
        #commented out for fixes, made sectionNumber and semesters as constants
        # semester = random.choice(["Spring", "Summer", "Fall", "Winter"])
        # sectionNumber = random.randint(1, 4)
        materialId = i

        file.write(
            f"INSERT INTO `SectionCourseMaterial` (`courseId`, `sectionNumber`, `semester`, `materialId`) VALUES ('{course_id}', '1', 'Spring', '{materialId}');\n"
        )

        #made userId random ID between 1-50 to remain consistent with the many-one relationship.
def generate_user_reviews(file):
    for userId in range(1, 51):
        verified = random.randint(0, 1)
        description = escape_sql_string(fake.text(max_nb_chars=150))
        uid = random.randint(1, 50)

        file.write(
            f"INSERT INTO `UserReview` (`reviewId`, `datePosted`, `verifiedPurchase`, `reviewDescription`, `userId`) VALUES (NULL, NULL, '{verified}', '{description}', '{uid}');\n"
        )


def generate_written_by(file):
    for i in range(1, 51):
        author_id = i
        material_id = i + 50

        file.write(
            f"INSERT INTO `WrittenBy` (`materialId`, `authorId`) VALUES ('{material_id}', '{author_id}');\n"
        )


def main():
    output_file = "insert_data.sql"

    with open(output_file, "w", encoding="utf-8") as file:
        generate_authors(file)
        generate_courses(file)
        generate_course_material(file)
        generate_course_supplies(file)
        generate_app_users(file)
        generate_listings(file)
        generate_professors(file)
        generate_publishers(file)
        generate_textbook(file)
        generate_sections(file)
        generate_section_professors(file)
        generate_section_course_materials(file)
        generate_user_reviews(file)
        generate_written_by(file)


if __name__ == "__main__":
    main()
