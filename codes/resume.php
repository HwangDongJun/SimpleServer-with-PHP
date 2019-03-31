<?php
$conn = mysqli_connect("localhost", "root", "ehdwns20", "githubuser");
$filtered = array(
  'username' => mysqli_real_escape_string($conn, $_POST['user_name'])
);

$sql = "SELECT * FROM user";
$check_name = mysqli_query($conn, $sql);
$in_name = True;
while($row_check = mysqli_fetch_array($check_name)) {
  if($row_check['username'] == $filtered['username']) {
    $in_name = False;
    break;
  }
}

if($in_name) {
  $sql = "
   INSERT INTO user (
     username
   ) VALUES (
     '{$filtered['username']}'
   )";
  mysqli_query($conn, $sql);
}
//It's not enough to just save it on the table.
//Duplication is not implemented.
?>

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title> resume.php </title>
  </head>
  <body>
    <table border="1">
      <tr>
        <td>id</td><td>username</td>
      </tr>
    <?php
      $sql = "SELECT * FROM user";
      $user_names = mysqli_query($conn, $sql);
      while($row = mysqli_fetch_array($user_names)) {
        $escaped = array(
          'id'=>htmlspecialchars($row['id']),
          'username'=>htmlspecialchars($row['username'])
        );
    ?>
        <tr>
          <td><?=$escaped['id']?></td>
          <td><?=$escaped['username']?></td>
        </tr>
      <?php
      }
      ?>
    </table>
    <?php
      $name = htmlspecialchars($filtered['username']);

      $command = 'sudo python3 ~/github/SimpleServer-with-PHP/codes/info_crawler/main.py enter031@naver.com:ghkdehdwns20 '.$name. ' 2>&1'; //if exist error -> return string type

      $ret_val = exec($command, $output);
      echo $ret_val;
      echo $output;

      $myDict = json_decode(file_get_contents('~/github/SimpleServer-with-PHP/codes/info_crawler/info_dict.json'));

      print_r($myDict);

      $image_src = $myDict->user_info[0];
      $bio = $myDict->user_info[1];
      $location = $myDict->user_info[2];
      $name = $myDict->user_info[3];
      $github_url = $myDict->user_info[4];
      $websiteurl = $myDict->user_info[5];
    ?>
    <p><img src="<?=$image_src?>" alt="Github_img" height="100" width="100"></p>
    <p><?=$bio?></p>
    <p><?=$location?></p>
    <p><?=$name?></p>
    <p><a href="<?=$github_url?>">Visit! My Github!!</a></p>
    <p><a href="<?=$websiteurl?>">Visit! My Website!!</a></p>
  </body>
</html>
