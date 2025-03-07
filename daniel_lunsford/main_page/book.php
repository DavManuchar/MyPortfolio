<?php 
require_once '../page/parts/header.php';
?>
<?php 
require_once '../configs/db.php';
?>

<div class="section_5">
  <div class="zagalov">
    <div class="hr2"></div>
    <h1 class="h1">Books</h1>
  </div>
  <?php
  $all_prod = "SELECT * FROM `produckts`";
  $produckts = $conn->query($all_prod);
  
  $count = $produckts->num_rows;
  $produckts = $produckts->fetch_all();

  ?>
  <div class="about_box">
    <div class="div_books_box">
      <?php 
        for($i = 0; $i < $count; $i++){?>
          <div class="part_book">
            <div class="book_box_shop">
              <img src="<?php echo $produckts[$i][3]; ?>" alt="book">
              <div class="bnut">
                <div class="book_price"></div>
                <span class="book_name"><?php echo $produckts[$i][1]; ?></span>
                <div class="hr"></div>
                <span class="price">$<?php echo $produckts[$i][2]; ?></span>
                <button id="<?php echo $produckts[$i][0]; ?>" class="<?php 
  
                  if (!empty($_SESSION['books'] ) ) {
                    $c = $_SESSION['books'];
                    $a = array();
                
                    for($j = 0; $j<count($c); $j++){
                      if($c[$j] != 0){
                        array_push($a, $c[$j]);
                      }
                    }
                    $nick = $produckts[$i][4];
                    $book_id_ex = "SELECT `id` FROM `produckts` WHERE `nick` = '$nick'" ;
                    $book_id = $conn->query($book_id_ex);
                    $book_id = $book_id->fetch_assoc();

                    if(in_array($book_id['id'], $a)){
                      echo "to_cart_button_on";
                    }else{
                      echo "to_cart_button";
                    }
                  }else{
                    echo "to_cart_button";
                  }
                ?>" name="<?php echo $produckts[$i][4]; ?>">Add to Cart</button>
              </div>
            </div>
          </div>        
        <?php
        }
      ?>
    </div>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js" integrity="sha512-v2CJ7UaYy4JwqLDIrZUI/4hqeoQieOmAZNXBeQyjo21dadnwR+8ZaIJVT8EE2iyI61OV8e6M8PP2/4hpQINQ/g==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script src="../js/book.js"></script>

<?php
require_once '../page/parts/footer.php';
?>