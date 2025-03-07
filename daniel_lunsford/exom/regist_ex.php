<?php 
session_start();
require_once "../configs/db.php";

if (isset($_POST) && !empty($_POST['action'])) {
  if ($_POST['action'] == 'register') {
    extract($_POST);

    $mail_check = "SELECT `id` FROM `user` WHERE `mail` = '$mail'";
    $result_mail = $conn->query($mail_check);

    if($result_mail->num_rows > 0){
      echo json_encode(['success' => false]);
      exit;
    }
    else{
      $ver_code = rand(100000,999999);
      $ver_code = json_decode($ver_code);
      mail($mail,'Verification mail',$ver_code);

      $_SESSION['mail_code'] = $mail;
      $query = "INSERT INTO `user`( `mail`, `phone`, `password`, `code`, `status`) VALUES ('$mail','$phone','$password','$ver_code','false')";
      $result = $conn->query($query);
      echo json_encode(['success' => true]);
      exit;
    }
  }
  
}

if (isset($_POST) && !empty($_POST['action'])) {
  if ($_POST['action'] == 'code_ex') {
    extract($_POST);

    $mail = $_SESSION['mail_code'];
    $cod = "SELECT `code` FROM `user` WHERE `mail` = '$mail'";
    $cod_result = $conn->query($cod);
    $cod_result = $cod_result->fetch_all();

    if($cod_result[0][0] == $code){
      $status = "SELECT `status` FROM `user` WHERE `mail` = '$mail'";

      $up_status = "UPDATE `user` SET `status` = 'true'";
      $up_status_result = $conn->query($up_status);

      $_SESSION['status'] = true;
      echo json_encode(['success' => true]);
      exit;
    }else{
      echo json_encode(['success' => false]);
      exit;
    }
  }
  exit;
}

if (isset($_GET)) {
  if (isset($_GET['mail'])) {
    $mail = $_GET['mail'];
  }
  if (isset($_GET['password'])) {
    $password = $_GET['password'];
  }
  $mail_check = "SELECT `id` FROM `user` WHERE `mail` = '$mail'";
  $result_mail = $conn->query($mail_check);
  if($result_mail->num_rows > 0){
    $password_check = "SELECT `password` FROM `user` WHERE `mail` = '$mail'";
    $password_res = $conn->query($password_check);
    $password_res = $password_res->fetch_assoc();
    if($password_res['password'] == $password){
      $_SESSION['status'] = true;
      header('Location: /../index.php');
      exit;
    }else{
      header('Location: /../log_in.php');
      echo json_encode(['success' => false , 'error' => 'Invalid password']);
      exit;
    }
  }
  else{
    header('Location: /../log_in.php');
    echo json_encode(['success' => false, 'error' => 'Invalid mail']);
    exit;
  }
}

  ?>