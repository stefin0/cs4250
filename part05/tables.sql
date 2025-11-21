CREATE TABLE
  author (
    authorId INTEGER NOT NULL,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    affiliation VARCHAR(300),
    biography VARCHAR(500),
    email VARCHAR(100) NOT NULL,
    PRIMARY KEY (authorId)
  );

CREATE TABLE
  course (
    courseDescription VARCHAR(500),
    courseId INTEGER NOT NULL,
    courseName VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    prerequisite VARCHAR(100),
    units INTEGER NOT NULL,
    PRIMARY KEY (CourseID)
  );

CREATE TABLE
  courseMaterial (
    dateAdded DATETIME NOT NULL,
    description_ VARCHAR(500),
    isRequired BIT,
    materialId INTEGER NOT NULL,
    msrp DECIMAL(10, 2),
    name_ VARCHAR(100),
    PRIMARY KEY (materialId)
  );

CREATE TABLE
  courseSupplies (
    brand VARCHAR(100),
    height INTEGER,
    width INTEGER,
    length_ INTEGER,
    weight_ INTEGER,
    materialId INTEGER NOT NULL,
    PRIMARY KEY (materialId),
    FOREIGN KEY (materialId) REFERENCES courseMaterial (materialId)
  );

CREATE TABLE
  listing (
    condition_ VARCHAR(100),
    datePosted DATETIME NOT NULL,
    isActive BIT NOT NULL,
    listingId INTEGER NOT NULL,
    listingPrice DECIMAL(10, 2) NOT NULL,
    quantity INTEGER NOT NULL,
    userId INTEGER NOT NULL,
    materialId INTEGER,
    PRIMARY KEY (listingId),
    FOREIGN KEY (userId) REFERENCES user_ (userId),
    FOREIGN KEY (materialId) REFERENCES courseMaterial (materialId)
  );

CREATE TABLE
  professor (
    department VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    institution VARCHAR(100) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    officeHours VARCHAR(20),
    profId INTEGER NOT NULL,
    PRIMARY KEY (profId)
  );

CREATE TABLE
  publisher (
    country INTEGER NOT NULL,
    email VARCHAR(300) NOT NULL,
    publisherId INTEGER NOT NULL,
    publisherName VARCHAR(300) NOT NULL,
    website VARCHAR(500) NOT NULL,
    yearEstablished DATETIME NOT NULL,
    PRIMARY KEY (PublisherID)
  );

CREATE TABLE
  textbook (
    numberOfPages INTEGER NOT NULL,
    language_ VARCHAR(300) NOT NULL,
    edition_ VARCHAR(100),
    publicationYear DATETIME NOT NULL,
    ISBN INTEGER NOT NULL,
    image_ VARCHAR(400),
    materialId INTEGER NOT NULL,
    publisherId INTEGER NOT NULL,
    PRIMARY KEY (materialId),
    FOREIGN KEY (materialId) REFERENCES courseMaterial (materialId),
    FOREIGN KEY (publisherId) REFERENCES publisher (publisherId)
  );

CREATE TABLE
  user_ (
    userId INTEGER NOT NULL,
    isVerified BIT NOT NULL,
    overallRating DECIMAL(1, 1),
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    responseTime INTEGER,
    returnPolicy VARCHAR(500),
    sellerBio VARCHAR(500),
    phoneNumber INTEGER,
    email VARCHAR(300) NOT NULL,
    dateJoined DATETIME NOT NULL,
    PRIMARY KEY (userId)
  );

CREATE TABLE
  section (
    capacity INTEGER NOT NULL,
    deliveryMethod VARCHAR(100),
    roomNumber INTEGER,
    sectionNumber INTEGER NOT NULL,
    semester VARCHAR(10) NOT NULL,
    time_ VARCHAR(100) NOT NULL,
    PRIMARY KEY (courseId, sectionNumber, semester),
    FOREIGN KEY (courseId) REFERENCES course (courseId)
  );

CREATE TABLE
  userReview (
    datePosted DATETIME NOT NULL,
    verifiedPurchase BIT,
    reviewDescription VARCHAR(500),
    userID INTEGER NOT NULL,
    reviewId INTEGER NOT NULL,
    PRIMARY KEY (reviewId),
    FOREIGN KEY (userID) REFERENCES user (userID)
  );

CREATE TABLE
  SectionProfessor (
    courseId INTEGER NOT NULL,
    sectionNumber INTEGER NOT NULL,
    semester VARCHAR(10) NOT NULL,
    professorId INTEGER NOT NULL,
    PRIMARY KEY (courseId, sectionNumber, semester),
    FOREIGN KEY (courseId, sectionNumber, semester) REFERENCES section (courseId, sectionNumber, semester),
    FOREIGN KEY (professorId) REFERENCES professor (professorId)
  );

CREATE TABLE
  SectionCourseMaterial (
    courseId INTEGER NOT NULL,
    sectionNumber INTEGER NOT NULL,
    semester VARCHAR(10) NOT NULL,
    materialId INTEGER NOT NULL,
    PRIMARY KEY (courseId, sectionNumber, semester, materialId),
    FOREIGN KEY (courseId, sectionNumber, semester) REFERENCES section (courseId, sectionNumber, semester),
    FOREIGN KEY (materialId) REFERENCES courseMaterial (materialId)
  );

CREATE TABLE
  writtenBy (
    materialId INTEGER NOT NULL,
    authorId INTEGER NOT NULL,
    PRIMARY KEY (materialId, authorId),
    FOREIGN KEY (materialId) REFERENCES textbook (materialId),
    FOREIGN KEY (authorId) REFERENCES author (authorId)
  );