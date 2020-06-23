function preparar_dados_envio(classe){
    var dados = {};
    
    if (classe == "realizar_operacao"){
        dados["num1"] = $("#num1").val();
        dados["num2"] = $("#num2").val();
        dados["base"] = $("#base").val();
        dados["operador"] = $("#operador").val();
    }
    else if (classe == "converter_numero"){
        dados["numero"] = $("#numero").val();
        dados["base_entrada"] = $("#base_entrada").val();
        dados["base_saida"] = {};

        for (i=1; i<=cont_id; i++){
            var nome = "base_saida-" + i;
            dados["base_saida"][nome] = $("#"+nome).val();
        };
    };

    return(dados);
};

function formatar_dados_resposta(dados){
    $.each(dados, function(chave,valor){
        $(chave).val(valor)
    });
};

function del_saida(elemento){
    var seletor = $(elemento).attr("id")
    $('.'+seletor).remove()
};

var cont_id = 1;

$("#add_saida").click(function(){
    cont_id += 1;
    $("#extras").append(
        "<div class='"+cont_id+"'>"+ 
        "Base Saida: <input id='base_saida-"+cont_id+"' type='text'>&nbsp" +
        "Resultado: <input id='resultado-"+cont_id+"' type='text' readonly>&nbsp"+
        "<button id='"+cont_id+"' onclick='del_saida(this)' type='button'>Excluir</button><br>"+
        "</div>");    
});

$("#enviar").click(function(){
    var classe = $(this).attr("class");
    $.ajax({
        url: "http://localhost:5000/" + classe,
        type: "POST",
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify(preparar_dados_envio(classe)),
        error: function(err){
            console.log(err)
        }
    }).done(function(dados){
        formatar_dados_resposta(dados)
    })
});