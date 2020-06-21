function preparar_dados_envio(){
    var dados = {};
    
    dados["num1"] = $("#num1").val();
    dados["num2"] = $("#num2").val();
    dados["base"] = $("#base").val();
    dados["operador"] = $("#operador").val();

    return(dados);
};

function formatar_dados_resposta(dados){
    $.each(dados, function(chave,valor){
        $(chave).val(valor)
    });
};

$("#enviar").click(function(){
    $.ajax({
        url: "http://localhost:5000/realizar_operacao",
        type: "POST",
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify(preparar_dados_envio()),
        error: function(err){
            console.log(err)
        }
    }).done(function(dados){
        formatar_dados_resposta(dados)
    })
});