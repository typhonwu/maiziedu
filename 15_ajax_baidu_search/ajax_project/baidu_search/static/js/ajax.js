//get或post方法
function do_ajax(){
    word = $("#word").val();
    if(word!=''){
        $.get("/validate/word/", {"word": word}, function(data){
            var str='';
            if(data.message!=[]){
                $.each($.parseJSON(data), function (k, v){
                str +='<li  class="list" id="this_li" onclick=fun(this);>'+v.fields.word_value+'</li>';
                });
                if(str!=''){
                    $("#drop_down").css("display", "block");
                    $("#word_txt").html(str);
                }else{
                    $("#drop_down").css("display", "none");
                }
            }
        })
    }else{
        $("#drop_down").css("display", "none");
    }
}
var fun = function(obj){
    $("#word").val($(obj).html());
    $("#drop_down").css("display", "none");
}

