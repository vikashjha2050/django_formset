$("#add_form").click(function(){
   var total = $('.man_class').find('#id_form-TOTAL_FORMS').val();
   var init = $('.man_class').find('#id_form-INITIAL_FORMS').val();
   var extra = total-init+1;
   var total = parseInt(total, 10)+1;
   var pathname = window.location.pathname.split('/');
   if(pathname.length == 5){
     pk = pathname[2];
   }else{
     pk = 0;
   }
  $.ajax({
        url: '/exams/getset/',
        data : {extra:extra,pk:pk},
    })
    .done(function(response) { 
        $('.setclass').html(response);
        $('.man_class').find('#id_form-TOTAL_FORMS').val(total)
    });
});
