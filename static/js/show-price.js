$(document).ready(function() {
$('#carPriceForm').submit(function(event) {
    event.preventDefault(); // Evita o recarregamento da página

    $.ajax({
    type: 'POST',
    url: '/evaluate',
    data: $(this).serialize(), // Pega os dados do formulário
    success: function(response) {
        $('#priceResult').text('$ ' + response.Price.toLocaleString('pt-BR'));
    },
    error: function() {
        $('#priceResult').text('Erro ao calcular preço.');
    }
    });
});
});
