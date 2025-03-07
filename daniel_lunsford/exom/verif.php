
<?php 
require_once '../page/parts/header.php';
?>


<div class="container">
  <form name="file_upload" enctype="multipart/form-data">
    <div class="form">
      <div class="input-field">
        <span class="log_span" id="nname">Code</span>
      </div>
      <div class="input-field" style="margin-top: 50px;">
        <label for="email" id="nname">we have sent the code to your email</label>
        <input class="input_log" type="number" placeholder="Code" id="code" name="code" style="margin-top: 2px;">
      </div>
      <div class="input-field" style="margin-top: 50px;">
        <input type="button" value="Register" id="btn" class="btn">
      </div>
    </div>
  </form>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js" integrity="sha512-v2CJ7UaYy4JwqLDIrZUI/4hqeoQieOmAZNXBeQyjo21dadnwR+8ZaIJVT8EE2iyI61OV8e6M8PP2/4hpQINQ/g==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script src="../js/verif.js"></script>

<?php
require_once '../page/parts/footer.php';
?>