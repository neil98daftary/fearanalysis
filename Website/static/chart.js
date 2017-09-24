$('document').ready(function() {

  chartData = {}
  colors = {}

  $.ajax({
    type: "GET",
    url: "/getchart",
    dataType: "text",
    success: (data) => {
      console.log(data);
      chartData = JSON.parse(data)
      setColors();
    }
  });

  function setColors() {
    for(prop in chartData) {
      if(parseInt(chartData[prop]) <= 1) {
        colors[prop] = "#00FF00"
      }
      else if(parseInt(chartData[prop]) <= 3) {
        colors[prop] = "#FFFF00"
      }
      else {
        colors[prop] = "#FF0000"
      }
    }
    drawChart();
  }

  function drawChart() {
    google.charts.load('current', {packages: ['corechart', 'bar']});
    google.charts.setOnLoadCallback(drawMultSeries);
  }

  function drawMultSeries() {
    console.log(chartData["0"]);
    var data = google.visualization.arrayToDataTable([
          ['Question', 'Class', {role: "style"}],
          ['Q1', parseInt(chartData["0"]), colors["0"]],
          ['Q2', parseInt(chartData["1"]), colors["1"]],
          ['Q3', parseInt(chartData["2"]), colors["2"]],
          ['Q4', parseInt(chartData["3"]), colors["3"]],
          ['Q5', parseInt(chartData["4"]), colors["4"]],
          ['Q6', parseInt(chartData["5"]), colors["5"]],
          ['Q7', parseInt(chartData["6"]), colors["6"]],
          ['Q8', parseInt(chartData["7"]), colors["7"]],
          ['Q9', parseInt(chartData["8"]), colors["8"]],
          ['Q10', parseInt(chartData["9"]), colors["9"]]
        ]);

    var view = new google.visualization.DataView(data);
    view.setColumns([0, 1,
                     { calc: "stringify",
                       sourceColumn: 1,
                       type: "string",
                       role: "annotation" },
                     2]);

      var options = {
        title: "Fear Chart",
        width: 600,
        height: 400,
        bar: {groupWidth: "80%"},
        legend: { position: "none" },
        hAxis: {
          title: 'Class'
        },
        vAxis: {
          title: 'Question'
        }
      };
      var chart = new google.visualization.BarChart(document.getElementById("chart_div"));
      chart.draw(view, options);
  }

});
