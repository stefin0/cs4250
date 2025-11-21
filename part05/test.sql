CREATE TABLE AppUser (
    userId INTEGER NOT NULL AUTO_INCREMENT,
    email VARCHAR(191) NOT NULL,
    passwordHash VARCHAR(255) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    isVerified TINYINT(1) DEFAULT 0,
    overallRating DECIMAL(3, 2) DEFAULT 0.00,
    responseTimeMinutes INTEGER,
    returnPolicy TEXT,
    sellerBio TEXT,
    phoneNumber VARCHAR(20),
    dateJoined DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (userId),
    UNIQUE (email)
);

CREATE TABLE Publisher (
    publisherId INTEGER NOT NULL AUTO_INCREMENT,
    publisherName VARCHAR(300) NOT NULL,
    country VARCHAR(100),
    email VARCHAR(191),
    website VARCHAR(500),
    yearEstablished YEAR,
    PRIMARY KEY (publisherId)
);

CREATE TABLE Author (
    authorId INTEGER NOT NULL AUTO_INCREMENT,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    affiliation VARCHAR(300),
    biography TEXT,
    email VARCHAR(191) NOT NULL,
    PRIMARY KEY (authorId)
);

CREATE TABLE Course (
    courseId INTEGER NOT NULL AUTO_INCREMENT,
    department VARCHAR(100) NOT NULL,
    courseName VARCHAR(100) NOT NULL,
    courseDescription TEXT,
    prerequisite VARCHAR(100),
    units INTEGER NOT NULL,
    PRIMARY KEY (courseId)
);

CREATE TABLE Professor (
    profId INTEGER NOT NULL AUTO_INCREMENT,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    email VARCHAR(191) NOT NULL,
    department VARCHAR(50) NOT NULL,
    institution VARCHAR(100) NOT NULL,
    officeHours VARCHAR(100),
    PRIMARY KEY (profId)
);

CREATE TABLE CourseMaterial (
    materialId INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(200),
    description VARCHAR(500),
    msrp DECIMAL(10, 2),
    isRequired TINYINT(1) DEFAULT 1,
    dateAdded DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (materialId)
);

CREATE TABLE CourseSupplies (
    materialId INTEGER NOT NULL,
    brand VARCHAR(100),
    height INTEGER,
    width INTEGER,
    length INTEGER,
    weight INTEGER,
    PRIMARY KEY (materialId),
    FOREIGN KEY (materialId) REFERENCES CourseMaterial (materialId) ON DELETE CASCADE
);

CREATE TABLE Textbook (
    materialId INTEGER NOT NULL,
    ISBN VARCHAR(17) NOT NULL,
    title VARCHAR(200),
    edition VARCHAR(50),
    language VARCHAR(50) NOT NULL,
    publicationYear YEAR NOT NULL,
    numberOfPages INTEGER NOT NULL,
    imageURL VARCHAR(2083),
    publisherId INTEGER NOT NULL,
    PRIMARY KEY (materialId),
    UNIQUE (ISBN),
    FOREIGN KEY (materialId) REFERENCES CourseMaterial (materialId) ON DELETE CASCADE,
    FOREIGN KEY (publisherId) REFERENCES Publisher (publisherId)
);

CREATE TABLE Listing (
    listingId INTEGER NOT NULL AUTO_INCREMENT,
    userId INTEGER NOT NULL,
    materialId INTEGER NOT NULL,
    listingPrice DECIMAL(10, 2) NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    `condition` VARCHAR(100),
    isActive TINYINT(1) DEFAULT 1,
    datePosted DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (listingId),
    FOREIGN KEY (userId) REFERENCES AppUser (userId) ON DELETE CASCADE,
    FOREIGN KEY (materialId) REFERENCES CourseMaterial (materialId)
);

CREATE TABLE Section (
    courseId INTEGER NOT NULL,
    sectionNumber VARCHAR(10) NOT NULL,
    semester VARCHAR(10) NOT NULL,
    capacity INTEGER NOT NULL,
    deliveryMethod VARCHAR(100),
    roomNumber VARCHAR(20),
    timeBlock VARCHAR(100) NOT NULL,
    PRIMARY KEY (courseId, sectionNumber, semester),
    FOREIGN KEY (courseId) REFERENCES Course (courseId) ON DELETE CASCADE
);

CREATE TABLE UserReview (
    reviewId INTEGER NOT NULL AUTO_INCREMENT,
    userId INTEGER NOT NULL,
    reviewerId INTEGER,
    reviewDescription VARCHAR(500),
    verifiedPurchase TINYINT(1) DEFAULT 0,
    datePosted DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (reviewId),
    FOREIGN KEY (userId) REFERENCES AppUser (userId) ON DELETE CASCADE
);

CREATE TABLE SectionProfessor (
    courseId INTEGER NOT NULL,
    sectionNumber VARCHAR(10) NOT NULL,
    semester VARCHAR(10) NOT NULL,
    professorId INTEGER NOT NULL,
    PRIMARY KEY (courseId, sectionNumber, semester, professorId),
    FOREIGN KEY (courseId, sectionNumber, semester) 
        REFERENCES Section (courseId, sectionNumber, semester) ON DELETE CASCADE,
    FOREIGN KEY (professorId) REFERENCES Professor (profId) ON DELETE CASCADE
);

CREATE TABLE SectionCourseMaterial (
    courseId INTEGER NOT NULL,
    sectionNumber VARCHAR(10) NOT NULL,
    semester VARCHAR(10) NOT NULL,
    materialId INTEGER NOT NULL,
    PRIMARY KEY (courseId, sectionNumber, semester, materialId),
    FOREIGN KEY (courseId, sectionNumber, semester) 
        REFERENCES Section (courseId, sectionNumber, semester) ON DELETE CASCADE,
    FOREIGN KEY (materialId) REFERENCES CourseMaterial (materialId)
);

CREATE TABLE WrittenBy (
    materialId INTEGER NOT NULL,
    authorId INTEGER NOT NULL,
    PRIMARY KEY (materialId, authorId),
    FOREIGN KEY (materialId) REFERENCES Textbook (materialId) ON DELETE CASCADE,
    FOREIGN KEY (authorId) REFERENCES Author (authorId) ON DELETE CASCADE
);