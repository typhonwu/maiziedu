//get或post方法
function do_ajax(){
    word = $("#word").val();
    $('#drop_down').css('display','block');
    //用键值对的形式向服务器传送数据，在django的views中也用相同名称获取数据
    //这个方法就是$.ajax()的简写形式
    $.get('/search/', {'word':word}, function(data){
        //alert(data.length);
        //获得的data里面其实是一个字典，用each方法遍历出来
        //jQuery.parseJSON()函数用于将格式完好的JSON字符串转为与之对应的JavaScript对象。
        queries = $.parseJSON(data)
        $.each(queries,function(key,value){
            //具体取哪个字段可以在chrome的控制台查看一下返回的json文件内容
            $('#word_txt').html('<li>'+value.fields.title+'</li>')
        });
    });
}

