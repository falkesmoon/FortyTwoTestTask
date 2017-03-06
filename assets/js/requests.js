var old_number = 0;
var large = "";
var new_number = 0;
var title = 0;
var title_number = 0;
localStorage.old_number = old_number;


function get_requests(){
  $.ajax({
    type: "GET",
    url: "/request_list/",
    dataType: "json",
    success: function(data){
      old_number = data[0].pk;
      localStorage.old_number = old_number;
      console.log('old_number ' + old_number);
      $("#MyTable > tbody").html("");
      for (var i = 0; i < data.length; i++) {
          var data_rewrite = data[i].fields.req_time;
          data_rewrite = data_rewrite.slice(0,10) + ' ' +  data_rewrite.slice(11,19);
          large += '<tr><td>' + data[i].fields.path + '</td>' + '<td>' + data_rewrite + '</td>' +  '<td>' + data[i].fields.method + '</td>' + '<td>' + data[i].fields.status + '</td>' + '</tr>';
      }
      $('#MyBody').append(large);
      large = '';
    },
    error: function (data) {
      alert("fail");
    }
  });
}

setInterval(function get_numbers() {
    $.ajax({
            type: 'GET',
            url: '/request_list_ajax/',
            dataType: 'json',
            success: function(data) {
                title_number = parseInt(localStorage.title_additional);
                new_number = data.records;
                if (new_number > localStorage.old_number) {                 
                    title = new_number - localStorage.old_number;
                    show_title(title);
                    title_number += 1;
                    localStorage.title_additional = title_number;
                } else {
                  
                }
            }
          });}
        , 1000);

function show_title(title) {
  if (title == 1){
    document.title = '(' + title + ')' + ' New request';
  } else if (title > 1){
    document.title = '(' + title + ')' + 'New requests';
  } else {
    document.title = ' Requests';
  }
  
  $(window).focus(function(){
    setTimeout(function(){
      document.title = 'Requests';
      localStorage.old_number = new_number;
      
  }, 1000);
  });
}

$(document).ready(function(){
  get_requests(); 
});

