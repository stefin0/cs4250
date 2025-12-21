<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

require_once 'db.php';
$message = "";
$login_attempted = false;

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $firstName = $_POST['first_name'];
    $lastName = $_POST['last_name'];
    $email = $_POST['email'];
    $password = $_POST['password'];

    if (!empty($firstName) && !empty($lastName) && !empty($email) && !empty($password)) {
        try {
            $sql = "INSERT INTO `AppUser` (`userId`, `email`, `passwordHash`, `firstName`, `lastName`, `isVerified`, `overallRating`, `responseTimeMinutes`, `returnPolicy`, `sellerBio`, `phoneNumber`, `dateJoined`) VALUES
             (NULL, :email, :password, :firstName, :lastName, NULL, NULL, NULL, NULL, NULL, NULL, NULL)"; 
            $stmt = $pdo->prepare($sql);
            $stmt->execute(['email' => $email, 'password' => $password, 'firstName' => $firstName, 'lastName' => $lastName]);
            $message = "<p style='color: green;'>Successfully added!</p>";
            $login_attempted = true;
        } catch (PDOException $e) {
            $message = "<p style='color: red;'>Error: " . $e->getMessage() . "</p>";
            $login_attempted = true;
        }
    }
}
?>

<!DOCTYPE html>
<html>
    <body>
        <h1>Sign Up for KeyBound</h1>
        <h3>input information</h3>
        <form method="POST">
            <label for="first_name">First Name:</label><br>
            <input type="text" id="first_name" name="first_name" required><br><br>

            <label for="last_name">Last Name:</label><br>
            <input type="text" id="last_name" name="last_name" required><br><br>

            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email" required><br><br>

            <label for="password">Password:</label><br>
            <input type="text" id="password" name="password" required><br><br>

            <button type="submit">Sign Up</button>
        </form>
        <?php
            if($login_attempted) {
                echo $message;
            }
        ?>
        </body>
</html>