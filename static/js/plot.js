function plotHist(){

    var svg = dimple.newSvg("body", 600, 400);
    var data = [{'Sentimento': 'Negativo', 'Tweets': {{ cont[0] }}}, {'Sentimento': 'Neutro', 'Tweets': {{ cont[1] }}}, {'Sentimento': 'Positvo', 'Tweets': {{ cont[2] }}}];
    var chart = new dimple.chart(svg, data);
    chart.addCategoryAxis("x", "Sentimento");
    chart.addMeasureAxis("y", "Tweets");
    chart.addSeries(null, dimple.plot.bar);
    chart.draw();

    return false;
};

$('#formContainer').submit(plotHist);