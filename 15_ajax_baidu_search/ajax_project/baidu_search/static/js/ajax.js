//get或post方法
function do_ajax(){
    word = $("#word").val();
    //用键值对的形式向服务器传送数据，在django的views中也用相同名称获取数据
    //这个方法就是$.ajax()的简写形式
    $.get('/search/', {'word':word}, function(data){
        alert(data.length)
    })

