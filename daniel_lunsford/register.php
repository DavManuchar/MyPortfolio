<?php 
require_once 'page/parts/header.php';
?>

<div class="container">
  <form name="file_upload" enctype="multipart/form-data">
    <div class="form">
      <div class="input-field">
        <span class="log_span">Register</span>
      </div>
      <div class="input-field">
        <label for="email" id="nname">Email</label>
        <input class="input_log" type="email" placeholder="example@example.com" id="email" name="email">
      </div>
      <div class="input-field">
        <label for="email">Phone Number</label>
        <input class="input_log" type="text" placeholder="077777777" id="phone" name="phone_number">
      </div>
      <div class="input-field">
        <label for="password">Password</label>
        <input class="input_log" type="password" placeholder="********" id="password" name="password">
      </div>
      <div class="input-field">
        <label for="password">Repeat Password</label>
        <input class="input_log" type="password" placeholder="********" id="repeat_password" name="r_password">
      </div>
      <div class="action">
        <a href="log_in.php">Log In?</a>
        <input type="button" value="Register" id="btn" class="btn">
      </div>
    </div>
  </form>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js" integrity="sha512-v2CJ7UaYy4JwqLDIrZUI/4hqeoQieOmAZNXBeQyjo21dadnwR+8ZaIJVT8EE2iyI61OV8e6M8PP2/4hpQINQ/g==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script src="js/register.js"></script>

<?php
require_once 'page/parts/footer.php';
?>
