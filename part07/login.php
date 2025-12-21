<?php
session_start();
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

require_once 'db.php';
$message = "";
$login_attempted = false;

if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $email = $_POST['email'];
        $password = $_POST['password'];

        $stmt = $pdo->prepare("SELECT email, passwordHash FROM `AppUser` WHERE email = :email");
        $stmt->execute(['email' => $email]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        if($user) {
            if($user['passwordHash'] == $password) {
                $_SESSION['email'] = $email;
                $_SESSION['password'] = $password;
                $message = "<p style= 'color: green;'>Login Successful! Redirecting to Account Management</p>";
                $login_attempted = true;
            }
            else {
                $message = "<p style='color: red;'>Error: Incorrect Password</p>";
                $login_attempted = true;
            }
        }
        else{
            $message = "<p style='color: red;'>Error: Email not within System</p>";
            $login_attempted = true;
        }
}
?>

<!DOCTYPE html>
<html>
    <body>
        <h1>Log In</h1>
        <form method="POST">
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email" required><br><br>

            <label for="password">Password:</label><br>
            <input type="text" id="password" name="password" required><br><br>

            <button type="submit">Log In</button>
        </form>

        <form action="signup.php">
            <button type="submit"> Sign Up</button>
        </form>
        <?php
            if($login_attempted) {
                echo $message;
            }
        ?>
        </body>
    </body>
</html>