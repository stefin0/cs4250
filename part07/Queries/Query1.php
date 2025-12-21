<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

require_once __DIR__ . '/../db.php';

?>

<!DOCTYPE html>
<html>
    <head>
        <title>Query One</title>
    </head>  
    <body>
        <h1>Query One</h1>
        <p>
            <strong>Description:</strong>
            what users have left a review where they have at least one verified purchase. Useful for knowing which users actually buy products and leave real reviews. 
        </p>
        <table>
            <?php
                $sql = "SELECT DISTINCT userID
                        FROM UserReview
                        WHERE verifiedPurchase >= 1";
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