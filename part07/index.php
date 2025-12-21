<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

require_once 'db.php';

$sql = "SELECT * FROM AppUser LIMIT 5";
$stmt = $pdo->query($sql);
?>

<!DOCTYPE html>
<html>
<head>
        <title>CS4250 Project Part 7</title>
</head>
<body>

<h1>Cs 4250 Database Project</h1>

<p><strong>Project Name:</strong> Keybound</p>
<p><strong>Group Members:</strong> Eris Hutchins, Saul Martinez, Stefin Racho</p>


<p>website currently under construction</p>
<p>Last updated 12/17/25</p>
<h3>Log In Here!!</h3>
<form action="login.php">
        <button type="submit"> Click Me to Log In</button>
</form>

<h3>Relations</h3>
<ul>
        <li><a href="RelationPages/AppUserRelation.php">AppUser</a></li>
        <li><a href="RelationPages/AuthorRelation.php">Author</a></li>
        <li><a href="RelationPages/CourseMaterialRelation.php">CourseMaterial</a></li>
        <li><a href="RelationPages/CourseRelation.php">Course</a></li>
        <li><a href="RelationPages/CourseSupplies.php">CourseSupplies</a></li>
        <li><a href="RelationPages/ListingRelation.php">Listing</a></li>
        <li><a href="RelationPages/ProfessorRelation.php">Professor</a></li>
        <li><a href="RelationPages/PublisherRelation.php">Publisher</a></li>
        <li><a href="RelationPages/SectionCourseMaterialRelation.php">SectionCourseMaterial</a></li>
        <li><a href="RelationPages/SectionProfessorRelation.php">SectionProfessor</a></li>
        <li><a href="RelationPages/SectionRelation.php">Section</a></li>
        <li><a href="RelationPages/TextbookRelation.php">Textbook</a></li>
        <li><a href="RelationPages/UserReviewRelation.php">UserReview</a></li>
        <li><a href="RelationPages/WrittenByRelation.php">WrittenBy</a></li>
</ul>

<h3>Queries</h3>
<ul>
        <li><a href="Queries/Query1.php">Query One</a></li>
        <li><a href="Queries/Query2.php">Query Two</a></li>
        <li><a href="Queries/Query3.php">Query Three</a></li>
        <li><a href="Queries/Query4.php">Query Four</a></li>
        <li><a href="Queries/Query5.php">Query Five</a></li>
</ul>


<h3> SQL Console</h3>
<h4>Note: PDO does not allow for multiple ';' within a single statement</h4>

<form method="post">
        <textarea name = "sql" rows = "6" cols = "80"
                placehoder="Enter any MYSQL statement"></textarea><br>
        <button type="submit">Execute</button>
</form>

<?php
if (isset($_POST['sql'])) {
        $sql = trim($_POST['sql']);

        try {
                $stmt = $pdo->query($sql);
                $rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

        if ($rows) {
                echo "<table border='1'><tr>";
                foreach (array_keys($rows[0]) as $col) {
                        echo "<th>" . htmlspecialchars($col) . "</th>";
                }
                echo "</tr>";

                foreach ($rows as $row) {
                        echo "<tr>";
                        foreach ($row as $cell) {
                                echo "<td>" . htmlspecialchars($cell) . "</td>";
                        }
                        echo "</tr>";
                }
                echo "</table>";
        } else {
                echo "<p>Query executed. No result set.</p>";
        }
        } catch (PDOException $e) {
                //if query() fails, try exec() (update, delete, etc.)
                try {
                        $affected = $pdo->exec($sql);
                        echo "<p>Statement executed succefully.</p>";
                        echo "<p>Rows affected: $affected</p>";
                } catch (PDOException $e2) {
                        echo "<p>Error: " . htmlspecialchars($e2->getMessage()) . "</p>";
                }
        }
}
?>
</body>
</html>
