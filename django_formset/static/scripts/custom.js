$("#add_form").click(function(){
   var total = $('.man_class').find('#id_form-TOTAL_FORMS').val();
   var init = $('.man_class').find('#id_form-INITIAL_FORMS').val();
   var extra = total-init+1;
   var total = total+1;
  $.ajax({
        url: '/exams/getset/',
        data : {extra:extra},
    })
    .done(function(response) { 
        $('.setclass').html(response);
        $('.man_class').find('#id_form-TOTAL_FORMS').val(total)
        alert(total);                                 
    });
});