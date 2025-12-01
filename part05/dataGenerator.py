import random

from faker import Faker

fake = Faker()


def escape_sql_string(value):
    if isinstance(value, str):
        value = value.replace("'", "''")
        value = value.replace("\n", " ").replace("\r", " ")
    return value


def generate_courses(file, num_courses=40):
    generated_courses = []

    for course_id in range(1, num_courses + 1):
        courseName = f"CourseName {course_id}"
        department = fake.random_element(elements=("CS", "Math", "Physics", "History"))
        courseDescription = fake.paragraph(nb_sentences = 3, variable_nb_sentences= True)
        prerequisite = f"CourseName {course_id}"
        units = random.randint(0,5)
        
        generated_courses.append((course_id, courseName, department, courseDescription, prerequisite))

        file.write(
            f"INSERT INTO `Course` (`courseId`, `courseName`, `department`, `courseDescription`, `prerequisite`, `units`) VALUES (NULL, '{courseName}', '{department}', '{courseDescription}', '{prerequisite}', {units})\n"
        )
        
    return generate_courses


def generate_course_material(file, num_course_material = 50):
    generated_course_materials = []

    for materialId in range (1, num_course_material + 1):
        materialDescription = fake.paragraph(nb_sentences= 4, variable_nb_sentences= True)
        isRequired = random.choice(["True", "False"])
        msrp = fake.pricetag()[1:]
        materialName = fake.word()
        
        generated_course_materials.append((materialId, materialDescription, isRequired, msrp, materialName))

        #for ints, remove back ticks or not (idk)
        file.write(
        f"INSERT INTO `CourseMaterial` ( `materialID`, `dateAdded`, `materialDescription`, `isRequired`, `msrp`, `materialName`) VALUES (NULL, NULL, '{materialDescription}', '{isRequired}', '{msrp}', '{materialName}')\n"
        )

    return generated_course_materials


def generate_course_supplies(file, course_materials, num_course_supplies=50):
    for course_material in course_materials:
        materialId = course_material[0]
        brand = fake.word()
        height = random.randint(1, 30)
        width = random.randint(1, 25)
        itemLength = random.randint(1, 30)
        itemWeight = random.randint(1, 30)
        
        file.write(
            f"INSERT INTO `CourseSupplies` (`materialId`, `brand`, `height`, `width`, `itemLength`, `itemWeight`) VALUES ({materialId}, '{brand}', '{height}', '{width}', '{itemLength}', '{itemWeight}' )\n"
        )


def generate_app_users(file, num_users=50):
    generated_app_users = []

    for userId in range(1, num_users + 1):
        email = fake.unique.email()
        password_hash = fake.md5()
        first_name = fake.first_name()
        last_name = fake.last_name()
        is_verified = random.choice(["True", "False"])
        overallRating =  round(random.uniform(0.00, 9.99), 2)
        responseTimeMinutes = random.randint(1, 10080) #One week in minutes
        returnPolicy = fake.paragraph(nb_sentences= 7, variable_nb_sentences= True)
        sellerBio = fake.paragraph(nb_sentences= 7, variable_nb_sentences= True)
        phoneNumber = fake.basic_phone_number()
        
        generated_app_users.append((userId, email, password_hash, first_name, last_name, is_verified, overallRating, responseTimeMinutes, returnPolicy, sellerBio, phoneNumber))

        file.write(
            f"INSERT INTO `AppUser` (`userId`, `email`, `passwordHash`, `firstName`, `lastName`, `isVerified`, `overallRating`, `responseTimeMinutes`, `returnPolicy`, `sellerBio`, `phoneNumber`, `dateJoined`) VALUES (NULL, '{email}', '{password_hash}', '{first_name}', '{last_name}', '{is_verified}', '{overallRating}', '{responseTimeMinutes}', '{returnPolicy}', '{phoneNumber}', NULL )\n"
        )

    return generated_app_users


def generate_listings(file, num_listing=50):
    for listingId in range(1, num_listing + 1):
        userId = fake.unique.random_int(min=1, max=50) 
        materialId = fake.unique.random_int(min=1, max=50)    #make range in specialization 1-50 for TB /51-100 for CM
        listPrice = round(fake.pyfloat(2, positive=True), 2)
        quantity = fake.pyint(1, 50)
        material_condition = fake.random_element(elements=('new', 'like new', 'used', 'refurbished'))
        isActive = fake.boolean(chance_of_getting_true=80)
        datePosted = fake.date_between(start_date='-1y', end_date='today')

        print(
            f"INSERT INTO `Listing` (`listingId`, `userId`, `materialId`, `listingPrice`, `quantity`, `material_condition`, `isActive`, `datePosted`) VALUES (NULL, '{userId}', '{materialId}', '{listPrice}', '{quantity}', '{material_condition}', '{isActive}', '{datePosted}');"
       )

def generate_authors(file, num_authors=50):
    generated_authors = []

    for authorId in range(num_authors):
        fname = escape_sql_string(fake.first_name())
        lname = escape_sql_string(fake.last_name())
        email = f"{fname.lower()}{lname.lower()}{authorId}@example.com"
        affiliation = escape_sql_string(fake.company())
        biography = escape_sql_string(fake.text())

        generated_authors.append((authorId, fname, lname, email, affiliation, biography))

        file.write(
            f"INSERT INTO `Author` (`authorId`, `firstName`, `lastName`, `affiliation`, `biography`, `email`) VALUES (NULL, '{fname}', '{lname}', '{affiliation}', '{biography}', '{email}');\n"
        )
    
    return generated_authors


def generate_sections_and_dependencies(file, num_courses=40):
    generated_sections = []

    for course_id in range(1, num_courses + 1):
        # Courses can have up to 3 sections
        for section_num in range(1, random.randint(2, 4)):
            semester = random.choice(["Spring", "Summer", "Fall", "Winter"])
            capacity = random.choice([30, 45, 60, 120])
            delivery = random.choice(["In-Person", "Online", "Hybrid"])
            room = random.randint(100, 500)
            days = random.choice(["MWF", "TuTh", "Mon", "Wed"])
            hour = random.randint(8, 18)
            time_block = f"{days} {hour}:00-{hour+1}:00"

            generated_sections.append((course_id, section_num, semester))

            file.write(
                f"INSERT INTO `Section` (`courseId`, `sectionNumber`, `semester`, `capacity`, `deliveryMethod`, `roomNumber`, `timeBlock`) VALUES ({course_id}, {section_num}, '{semester}', '{capacity}', '{delivery}', {room}, '{time_block}');\n"
            )

    return generated_sections


def generate_section_professors(file, sections, num_professors=50):
    for section in sections:
        course_id, section_num, semester = section
        prof_id = random.randint(1, num_professors)

        file.write(
            f"INSERT INTO `SectionProfessor` (`courseId`, `sectionNumber`, `semester`, `profId`) VALUES ({course_id}, {section_num}, '{semester}', {prof_id});\n"
        )


def generate_section_course_materials(file, sections, num_materials=70):
    for section in sections:
        if random.random() > 0.2:  # 80% of sections require course materials
            course_id, section_num, semester = section
            material_id = random.randint(1, num_materials)

            file.write(
                f"INSERT INTO `SectionCourseMaterial` (`courseId`, `sectionNumber`, `semester`, `materialId`) VALUES ({course_id}, {section_num}, '{semester}', {material_id});\n"
            )


def generate_user_reviews(file, num=50, num_users=100):
    for _ in range(num):
        verified = random.choice([0, 1])
        description = escape_sql_string(fake.text(max_nb_chars=150))
        user_id = random.randint(1, num_users)

        file.write(
            f"INSERT INTO `UserReview` (`reviewId`, `datePosted`, `verifiedPurchase`, `reviewDescription`, `userId`) VALUES (NULL, NULL, {verified}, '{description}', {user_id});\n"
        )


def generate_written_by(file, num_materials=25, num_authors=25):
    for material_id in range(1, num_materials + 1):
        num_book_authors = random.randint(1, 3)
        chosen_authors = random.sample(range(1, num_authors + 1), num_book_authors)

        for author_id in chosen_authors:
            file.write(
                f"INSERT INTO `WrittenBy` (`materialId`, `authorId`) VALUES ({material_id}, {author_id});\n"
            )


def main():
    output_file = "insert_data.sql"

    with open(output_file, "w", encoding="utf-8") as file:
        generate_authors(file)
        generate_courses(file)

        valid_course_materials = generate_course_material(file)
        generate_course_supplies(file, valid_course_materials)

        generate_app_users(file)

        valid_sections = generate_sections_and_dependencies(file)
        generate_section_professors(file, valid_sections)
        generate_section_course_materials(file, valid_sections)
        generate_user_reviews(file)
        generate_written_by(file)


def Insert_sql_query(tableName):
    pass


if __name__ == "__main__":
    main()
