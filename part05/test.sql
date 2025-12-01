/*
DONE
authorId: add AUTO_INCREMENT to prevent manual input of IDs.
*/
CREATE TABLE Author (
    authorId INTEGER NOT NULL AUTO_INCREMENT,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    affiliation VARCHAR(300),
    biography VARCHAR(500),
    email VARCHAR(100) NOT NULL,
    PRIMARY KEY (authorId)
);

/*
DONE
courseId: add AUTO_INCREMENT to prevent manual input of IDs.
*/
CREATE TABLE Course (
    courseId INTEGER NOT NULL AUTO_INCREMENT,
    courseName VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    courseDescription VARCHAR(500),
    prerequisite VARCHAR(100),
    units INTEGER NOT NULL,
    PRIMARY KEY (courseId)
);

/*
DONE
materialId: add AUTO_INCREMENT to prevent manual input of IDs.
materialName: changed from name  because name is a keyword.
materialDescription: changed from description because description is a keyword.
isRequired: BIT -> BOOOLEAN because BOOLEAN is more intuitive.
added a check constraint on MSRP to prevent negative values
*/
CREATE TABLE CourseMaterial (
    materialId INTEGER NOT NULL AUTO_INCREMENT,
    dateAdded TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    materialDescription VARCHAR(500),
    isRequired BOOLEAN DEFAULT FALSE,
    msrp DECIMAL(10, 2),
    materialName VARCHAR(100),
    CHECK (msrp >= 0),
    PRIMARY KEY (materialId)
);

/*
DONE
itemLength: changed from length because length is a keyword.
itemWeight: changed from weight because weight is a keyword.
added ON DELETE CASCADE to maintain data integrity.
*/
CREATE TABLE CourseSupplies (
    materialId INTEGER NOT NULL,
    brand VARCHAR(100),
    height INTEGER,
    width INTEGER,
    itemLength INTEGER,
    itemWeight INTEGER,
    PRIMARY KEY (materialId),
    FOREIGN KEY (materialId) REFERENCES CourseMaterial (materialId) ON DELETE CASCADE
);

/*  DONE
    Explanation:
    User -> AppUser: user is a reserved keyword in SQL.
    overallRating: DECIMAL(3,2); 3 equal to the amount of 
    overallRating: DECIMAL(3,2) to allow ratings like 4.25
    UNIQUE constraint on email to prevent duplicate registrations
    returnPolicy: TEXT to allow for longer descriptions.
    sellerBIo: TEXT to allow for longer descriptions.
    added a check constraint on overall rating to prevent negative values
*/
CREATE TABLE AppUser (
    userId INTEGER NOT NULL AUTO_INCREMENT,
    email VARCHAR(100) NOT NULL UNIQUE,
    passwordHash VARCHAR(255) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    isVerified BOOLEAN DEFAULT 0,
    overallRating DECIMAL(3, 1) DEFAULT 0.0,
    responseTimeMinutes INTEGER,
    returnPolicy TEXT,
    sellerBio TEXT,
    phoneNumber VARCHAR(20),
    dateJoined TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK (overallRating >= 0 AND overallRating <= 10),
    PRIMARY KEY (userId)
);

/* Done
   Explanation:
    condition -> material_condition: condition is a reserved keyword in SQL.
    
    isActive; TINYINT(1) -> BOOLEAN: Using BOOLEAN type to increase readibilty, also to 
    be able to use True and False.
    datePosted: TIMESTAMP with default CURRENT_TIMESTAMP, tracks down to the microsenond when the listing was created.
    added ON DELETE CASCADE to maintain data integrity.
    added a check constraint on listing price and quantity to prevent negative values
*/
CREATE TABLE Listing (
    listingId INTEGER NOT NULL AUTO_INCREMENT,
    userId INTEGER NOT NULL,
    materialId INTEGER NOT NULL,
    listingPrice DECIMAL(10, 2) NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    material_condition ENUM('New', 'Like New', 'Used', 'Worn', 'Well Worn') NOT NULL,
    isActive BOOLEAN DEFAULT 1,
    datePosted TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK (listingPrice >= 0),
    CHECK (quantity > 0),
    PRIMARY KEY (listingId),
    FOREIGN KEY (userId) REFERENCES AppUser (userId) ON DELETE CASCADE,
    FOREIGN KEY (materialId) REFERENCES CourseMaterial (materialId)
);

/* DONE
    Explanation:
    profId: added AUTO_INCREMENET to prevent manual input of IDs.
*/
CREATE TABLE Professor (
    profId INTEGER NOT NULL AUTO_INCREMENT,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    institution VARCHAR(100) NOT NULL,
    officeHours VARCHAR(100),
    PRIMARY KEY (profId)
);
/* DONE
    Explanation:
    email length changed to 100 from 191 to maintain consistency with other tables.
    website -> websit_url to be more descriptive.
    yearEstablished: YEAR type to store only the year, default is a for digit year format
*/
CREATE TABLE Publisher (
    publisherId INTEGER NOT NULL AUTO_INCREMENT,
    publisherName VARCHAR(300) NOT NULL,
    country VARCHAR(100),
    email VARCHAR(100),
    website_url VARCHAR(500),
    yearEstablished YEAR,
    PRIMARY KEY (publisherId)
);


/*done, Explanation: changed edition and language to textbookEdition and textbookLanguage
due to the reserved words, also chaged publicationYear to YEAR type for better data integrity.
*/
CREATE TABLE Textbook (
    materialId INTEGER NOT NULL,
    ISBN VARCHAR(17) NOT NULL,
    title VARCHAR(200),
    textbookEdition VARCHAR(50),
    textbookLanguage VARCHAR(50) NOT NULL,
    publicationYear YEAR NOT NULL,
    numberOfPages INTEGER NOT NULL,
    imageURL VARCHAR(400),
    publisherId INTEGER NOT NULL,
    PRIMARY KEY (materialId),
    UNIQUE (ISBN),
    FOREIGN KEY (materialId) REFERENCES CourseMaterial (materialId) ON DELETE CASCADE,
    FOREIGN KEY (publisherId) REFERENCES Publisher (publisherId)
);

/*Done: 
Explanation: added course as we missed it before, and changed "time" to timeblock due to 
reserved words as we missed it before, and changed semester data type to ENUM to support specific values
*/

CREATE TABLE Section (
    courseId INTEGER NOT NULL,
    sectionNumber INTEGER NOT NULL,
    semester ENUM('Spring', 'Summer', 'Fall', 'Winter') NOT NULL,
    capacity INTEGER NOT NULL,
    deliveryMethod VARCHAR(100),
    roomNumber INTEGER,
    timeBlock VARCHAR(100) NOT NULL,
    PRIMARY KEY (courseId, sectionNumber, semester),
    FOREIGN KEY (courseId) REFERENCES Course (courseId) ON DELETE CASCADE
);

/* DONE
    Explanation:
    reviewDescription: TEXT to allow for longer descriptions.
    verifiedPurchase: TINYINT(1) to BOOLEAN for better readability.
    datePosted: TIMESTAMP with default CURRENT_TIMESTAMP to track when the review was posted.
    added on Delete cascade to maintain data integrity.
*/
CREATE TABLE UserReview (
    reviewId INTEGER NOT NULL AUTO_INCREMENT,
    datePosted TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    verifiedPurchase BOOLEAN DEFAULT 0,
    reviewDescription TEXT,
    userId INTEGER NOT NULL,
    PRIMARY KEY (reviewId),
    FOREIGN KEY (userId) REFERENCES AppUser (userId) ON DELETE CASCADE
);

/*DONE
Explanation: added profId as primary key as we missed it before. changed semester data type to
ENUM to support only specific values.
added on Delete cascade to maintain data integrity.
*/
CREATE TABLE SectionProfessor (
    courseId INTEGER NOT NULL,
    sectionNumber INTEGER NOT NULL,
    semester ENUM('Spring', 'Summer', 'Fall', 'Winter') NOT NULL,
    profId INTEGER NOT NULL,
    PRIMARY KEY (courseId, sectionNumber, semester, profId),
    FOREIGN KEY (courseId, sectionNumber, semester)
        REFERENCES Section (courseId, sectionNumber, semester) ON DELETE CASCADE,
    FOREIGN KEY (profId) REFERENCES Professor (profId) ON DELETE CASCADE
);

/*
    Explanation:
    Semester data type changed to ENUM to support only specific values.
*/
CREATE TABLE SectionCourseMaterial (
    courseId INTEGER NOT NULL,
    sectionNumber INTEGER NOT NULL,
    semester ENUM('Spring', 'Summer', 'Fall', 'Winter') NOT NULL,
    materialId INTEGER NOT NULL,
    PRIMARY KEY (courseId, sectionNumber, semester, materialId),
    FOREIGN KEY (courseId, sectionNumber, semester) 
        REFERENCES Section (courseId, sectionNumber, semester) ON DELETE CASCADE,
    FOREIGN KEY (materialId) REFERENCES CourseMaterial (materialId)
);

/*
added ON DELETE CASCADE to maintain data integrity.
*/
CREATE TABLE WrittenBy (
    materialId INTEGER NOT NULL,
    authorId INTEGER NOT NULL,
    PRIMARY KEY (materialId, authorId),
    FOREIGN KEY (materialId) REFERENCES Textbook (materialId) ON DELETE CASCADE,
    FOREIGN KEY (authorId) REFERENCES Author (authorId) ON DELETE CASCADE
);