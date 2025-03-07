<?php
require_once '../configs/db.php';
session_start();


if (isset($_POST) && !empty($_POST['action'])) {
  if ($_POST['action'] == 'book_ex') {
    extract($_POST);
    // session_unset(); exit;

    $book_array = array();

    if (!empty($_SESSION['books'] ) ) {
      $a = $_SESSION['books'];

      for($i = 0; $i<count($a); $i++){
        array_push($book_array, $a[$i]);
      }
                                       
      $book_id_ex = "SELECT `id` FROM `produckts` WHERE `nick` = '$book'" ;
      $book_id = $conn->query($book_id_ex);
      $book_id = $book_id->fetch_assoc();

      if (in_array($book_id['id'], $book_array)){
        $index = array_search($book_id['id'], $book_array);
        $book_array[$index] = 0;

        $_SESSION['books'] = $book_array;

        $count_array = $_SESSION['count'];

        $index = $book_id['id'] - 1;
        
        $count_array[$index] = 0;
      
        $_SESSION['count'] = $count_array;

        $price_array = $_SESSION['price'];
        $tot_price = $price_array[$index];
        $price_array[$index] = 0;
      
        $_SESSION['price'] = $price_array;
        $_SESSION['total'] -= $tot_price;

        echo json_encode(['success' => false]);
        exit;
      }
      else{
        array_push($book_array, $book_id['id']);

        $_SESSION['books'] = $book_array;

        $count_id_ex = "SELECT `id` FROM `produckts`";
        $count_id = $conn->query($count_id_ex);
        $count_id = $count_id->fetch_all();

        $price_id_ex = "SELECT `price` FROM `produckts` WHERE `nick` = '$book'";
        $price_id = $conn->query($price_id_ex);
        $price_id = $price_id->fetch_assoc();

        if (!empty($_SESSION['count'])){
          $count_array = $_SESSION['count'];

          $index = $book_id['id'] - 1;
          $count_array[$index] = 1;
        
          $_SESSION['count'] = $count_array;
        }

        if (!empty($_SESSION['price'])){
          $price_array = $_SESSION['price'];

          $index = $book_id['id'] - 1;
          $price_array[$index] = $price_id['price'];
        
          $_SESSION['price'] = $price_array;
        }

        $_SESSION['total'] += $price_id['price'];

        echo json_encode(['success' => true]);
        exit;
      }
    }else{
      $book_array = array();
      $book_id_ex = "SELECT `id` FROM `produckts` WHERE `nick` = '$book'" ;
      $book_id = $conn->query($book_id_ex);
      $book_id = $book_id->fetch_assoc();

      array_push($book_array, $book_id['id']);
      
      $_SESSION['books'] = $book_array;

      $count_id_ex = "SELECT `id` FROM `produckts`";
      $count_id = $conn->query($count_id_ex);
      $count_id = $count_id->fetch_all();

      $price_id_ex = "SELECT `price` FROM `produckts` WHERE `nick` = '$book'";
      $price_id = $conn->query($price_id_ex);
      $price_id = $price_id->fetch_assoc();

      $price_array = array();
      for($z = 0; $z<count($count_id);$z++){
        array_push($price_array, 0);
      }
      $index = $book_id['id'] - 1;
      $price_array[$index] = $price_id['price'];
      $_SESSION['price'] = $price_array;

      $count_array = array();
      for($j = 0; $j<count($count_id);$j++){
        array_push($count_array, 0);
      }
      $index = $book_id['id'] - 1;
      $count_array[$index] = 1;
      $_SESSION['count'] = $count_array;

      $_SESSION['total'] = $price_id['price'];

      echo json_encode(['success' => true]);
      exit;
    }
  }
}
?>