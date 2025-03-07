<?php 
require_once '../page/parts/header.php';
?>
<?php 
require_once '../configs/db.php';
?>

<div class="cart_section">
  <span class="my_cart_span">My Cart</span>
  <div class="cart_hr"></div>

  <?php 
  session_start();
    if (!empty($_SESSION['books'] ) ) {
      $c = $_SESSION['books'];
      
      $a = array();
      $vorosh = 0;
      
      for($j = 0; $j<count($c); $j++){
        if($c[$j] != 0){
          array_push($a, $c[$j]);
          $vorosh += $c[$j];
        }
      }?>
  <div style="display:flex;">
    <div class="cart_div_section"><?php
          for($i = 0; $i < count($a); $i++){
            $c = $_SESSION['price'];
    
            $id = $a[$i];
            $book_id_ex = "SELECT * FROM `produckts` WHERE `id` = '$id'" ;
            $book_id = $conn->query($book_id_ex);
            $book_id = $book_id->fetch_assoc();
            ?>
      <div class="book_section_set">
        <div class="cart_img_div">
          <img src="<?php echo $book_id['img'] ?>" class="cart_img" alt="book">
        </div>
        <div class="cart_set_div" style="width: 75px;">
          <span><?php echo $book_id['name'] ?></span>
          <span id="pr<?= $i;?>"><?php echo $book_id['price'] ?></span>
        </div>
        <div class="cart_input_div" data-index="<?= $i;?>">
          <button class="min">-</button>
          <input id="count_id<?php echo $i; ?>" data-index="<?= $book_id['id'] - 1;?>" type="text" value="<?php 
                if (!empty($_SESSION['count'])){
                  echo $_SESSION['count'][$book_id['id'] - 1];
                }
                ?>" readonly>
          <button class="max">+</button>
        </div>
        <div class="cart_price_div" data-index="<?= $i;?>">
          <span id="pr_span<?= $i;?>">$<?php echo $c[$book_id['id'] - 1];?></span>
        </div>
        <div class="cart_delete_div">
          <svg class="cart_delete" id="<?= $a[$i];?>" name="<?= $i;?>" xmlns="http://www.w3.org/2000/svg" width="800px" height="800px"
            viewBox="0 0 24 24" fill="none">
            <g id="Menu / Close_SM">
              <path id="Vector" d="M16 16L12 12M12 12L8 8M12 12L16 8M12 12L8 16" stroke="#000000" stroke-width="2"
                stroke-linecap="round" stroke-linejoin="round" />
            </g>
          </svg>
        </div>
      </div>
      <?php
        }?>
    </div><?php
    if (!empty($_SESSION['total'] && $vorosh > 0)){?>
      <div class="pay_section_div">
        <div class="div_pay_span">
          <span>Total</span><span id="total">$<?php 
            echo $_SESSION['total'];
                ?>
          </span>
        </div>
        <div class="div_pay_button">
          <button>Checkout</button>
        </div>
        <span class="sec_svg">
        <svg width="11" height="14" viewBox="0 0 11 14" xmlns="http://www.w3.org/2000/svg" class="RtnbAi"
          data-hook="SecureCheckoutDataHook.lock">
          <g fill="currentColor" fill-rule="evenodd">
            <path
              d="M0 12.79c0 .558.445 1.01.996 1.01h9.008A1 1 0 0 0 11 12.79V6.01c0-.558-.445-1.01-.996-1.01H.996A1 1 0 0 0 0 6.01v6.78Z">
            </path>
            <path
              d="M9.5 5v-.924C9.5 2.086 7.696.5 5.5.5c-2.196 0-4 1.586-4 3.576V5h1v-.924c0-1.407 1.33-2.576 3-2.576s3 1.17 3 2.576V5h1Z"
              fill-rule="nonzero"></path>
          </g>
        </svg>
        Secure Checkout
        </span>
      </div>
    <?php }else{
      $_SESSION['total'] = 0;
    } ?>
  </div>
  <?php
      if($vorosh == 0){
        ?>
  <div class="div_cart_empty">
    <span>Cart is empty</span>
    <a href="book.php">Continue Browsing</a>
  </div>
  <?php
      }
    }else{?>
  <div class="div_cart_empty">
    <span>Cart is empty</span>
    <a href="book.php">Continue Browsing</a>
  </div>
  <?php
    }
  ?>
</div>


<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js"
  integrity="sha512-v2CJ7UaYy4JwqLDIrZUI/4hqeoQieOmAZNXBeQyjo21dadnwR+8ZaIJVT8EE2iyI61OV8e6M8PP2/4hpQINQ/g=="
  crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script src="../js/book.js"></script>

<?php
require_once '../page/parts/footer.php';
?>