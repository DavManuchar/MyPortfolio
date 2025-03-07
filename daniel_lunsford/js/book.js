
$('.to_cart_button').click(function(){
  book = $(this).attr('name')
  id = $(this).attr('id')
  count = $('.count').text()
  count = Number(count)

  $.ajax({
    url: '../exom/book_ex.php',
    method: 'POST',
    data: {action: 'book_ex', book: book},
    success: function(data){
      data = JSON.parse(data)
      if (data.success == true){
        $('.count').html(count + 1)
        $('#'+id).removeClass('to_cart_button').addClass('to_cart_button_on')
      }
      else{
        $('.count').html(count - 1)
        $('#'+id).removeClass('to_cart_button_on').addClass('to_cart_button')
      }
    }
  });
})

$('.to_cart_button_on').click(function(){
  book = $(this).attr('name')
  id = $(this).attr('id')
  count = $('.count').text()
  count = Number(count)

  $.ajax({
    url: '../exom/book_ex.php',
    method: 'POST',
    data: {action: 'book_ex', book: book},
    success: function(data){
      data = JSON.parse(data)
      if (data.success == true){
        $('.count').html(count + 1)
        $('#'+id).removeClass('to_cart_button_on').addClass('to_cart_button')
      }
      else{
        $('.count').html(count - 1)
        $('#'+id).removeClass('to_cart_button_on').addClass('to_cart_button')
      }
    }
  });
})

$('.min').click(function(){
  console.log('ddsdF')
  key = $(this).parent().attr('data-index')
  count = $('#count_id'+key).val()
  count = Number(count)

  data_index = $('#count_id'+key).attr('data-index')
  data_index = Number(data_index)

  price = $('#pr'+key).text()
  price = Number(price)
  

  if(count > 1){
    count = count - 1
    $('#count_id'+key).val(count)
    $.ajax({
      url: '../exom/book_price_ex.php',
      method: 'POST',
      data: {action: 'price_ex_min', price:price,data_index: data_index},
      success: function(data){
        data = JSON.parse(data)
        $('#pr_span'+key).html("$"+data.success)
        $('#total').html("$" + data.total)
      }
    })
  }else{
    count = 1
    $('#count_id'+key).val(count)
  }
})

$('.max').click(function(){
  key = $(this).parent().attr('data-index')
  count = $('#count_id'+key).val()
  count = Number(count)

  data_index = $('#count_id'+key).attr('data-index')
  data_index = Number(data_index)

  price = $('#pr'+key).text()
  price = Number(price)
  
  
  $.ajax({
    url: '../exom/book_price_ex.php',
    method: 'POST',
    data: {action: 'price_ex', price:price,data_index: data_index},
    success: function(data){
      data = JSON.parse(data)
      $('#pr_span'+key).html("$"+data.success)
      $('#total').html("$" + data.total)
    }
  })
  count = count + 1
  $('#count_id'+key).val(count)
})

$('.cart_delete').click(function(){
  id = $(this).attr('name')
  id = Number(id)

  key = $(this).attr('id')
  key = Number(key)

  count = $('#count_id'+id).val()
  count = Number(count)

  price = $('#pr'+id).text()
  price = Number(price)
  
  $.ajax({
    url: '../exom/book_price_ex.php',
    method: 'POST',
    data: {action: 'delete_ex',key: key, price:price, count:count},
    success: function(data){
      data = JSON.parse(data)
      if (data.success == true){
        location.reload()
      }
    }
  })
})

