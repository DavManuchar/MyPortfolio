<?php 
session_start();
require_once "../configs/db.php";

if (isset($_POST) && !empty($_POST['action'])) {
  if ($_POST['action'] == 'price_ex') {
    extract($_POST);

    $cou = $_SESSION['count'];
    $cou[$data_index] += 1;
    $_SESSION['count'] = $cou;

    $a = $_SESSION['price'];
    $a[$data_index] += $price;
    $_SESSION['price'] = $a;

    $_SESSION['total'] += $price;

    echo json_encode(['success' => $a[$data_index], 'total' => $_SESSION['total']]);
  }

  if ($_POST['action'] == 'price_ex_min') {
    extract($_POST);

    $cou = $_SESSION['count'];
    $cou[$data_index] -= 1;
    $_SESSION['count'] = $cou;

    $a = $_SESSION['price'];
    $a[$data_index] -= $price;
    $_SESSION['price'] = $a;

    $_SESSION['total'] -= $price;

    echo json_encode(['success' => $a[$data_index], 'total' => $_SESSION['total']]);
  }

  if ($_POST['action'] == 'delete_ex') {
    extract($_POST);

    $book = $_SESSION['books'];
    $index = array_search($key, $book);
    $book[$index] = 0;
    $_SESSION['books'] = $book;


    $_SESSION['total'] -= $price*$count;

    echo json_encode(['success' => true]);
  }
}