<?php 
require_once 'page/parts/header.php';
?>


<div class="container">
  <form name="log_in" method="GET" action="exom/regist_ex.php" enctype="multipart/form-data">
    <div class="form">
      <div class="input-field">
        <span class="log_span">Log In</span>
      </div>
      <div class="input-field">
        <label for="email">Email</label>
        <input class="input_log" type="email" placeholder="example@example.com" id="email" name="mail">
      </div>
      <div class="input-field">
        <label for="password">Password</label>
        <input class="input_log" type="password" placeholder="********" id="password" name="password">
      </div>
      <div class="action">
        <a href="register.php">Regist?</a>
        <input id="btn" class="btn" type="submit" value="Log in">
      </div>
    </div>
  </form>
</div>




<?php
require_once 'page/parts/footer.php';
?>
