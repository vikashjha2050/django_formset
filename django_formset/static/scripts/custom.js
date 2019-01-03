$("#add_form").click(function(){
  $.ajax({
        url: '/exams/getset/',
    })
    .done(function(response) { 
    	alert(response);       
        $('.setclass').append(response);                                 
    });
});