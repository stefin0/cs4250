<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

require_once __DIR__ . '/../db.php';

?>

<!DOCTYPE html>
<html>
    <head>
        <title>Query Four</title>
    </head>  
    <body>
        <h1>Query Four</h1>
        <p>
            <strong>Description:</strong>
             What authors have written multiple textbooks, showing their first and last names as well as the titles of all of their books.
        </p>
        <table>
            <?php
                $sql = "SELECT A.firstName, A.lastName, T.title
                        FROM `Author` AS A, `WrittenBy` AS W, `Textbook` AS T 
                        WHERE A.authorId = W.authorId 
                        AND W.materialId = T.materialId
                        AND A.authorId IN
                        (SELECT authorId
                        FROM `WrittenBy`
                        GROUP BY authorId
                        HAVING COUNT(*) > 1)
                        ORDER BY A.lastName;";
                $stmt = $pdo->query($sql);
                $rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

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
                ?>
        </table>
    </body>
</html>