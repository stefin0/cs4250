<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

require_once __DIR__ . '/../db.php';

?>

<!DOCTYPE html>
<html>
    <head>
        <title>Query Three</title>
    </head>  
    <body>
        <h1>Query Three</h1>
        <p>
            <strong>Description:</strong>
            We want to look at the difference between the MSRP and the CourseMaterial listing price (supplies or textbooks). Useful for seeing if a CourseMaterial is below the MSRP, like if it’s a good sale.
        </p>
        <table>
            <?php
                $sql = "SELECT C.MSRP, L.ListingPrice
                        FROM `Listing` AS L, `CourseMaterial` AS C
                        WHERE L.isActive = 1 
                        AND L.listingPrice < (C.msrp * 0.8);
                        ";
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