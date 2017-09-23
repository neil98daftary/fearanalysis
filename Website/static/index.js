$('document').ready(function() {
  let no_of_fears = 5;
  let no_of_questions = 0
  let rej_levels = [];
  let utext = '';
  let user_comp = 1;
  let comp_msgs = [];
  let i = 0;
  let responses = {};
  let displayMessage;

  $.ajax({
    type: "GET",
    url: "/getquestions",
    dataType: "text",
    success: (data) => {
      organizeQuestions(data);
    }
 });

 function organizeQuestions(questions) {
   let index = 0;
   questions = questions.split(/\r\n|\n/);
   questions = questions.map((item) => {
     return item.split(',');
   });
   if(questions[0].length === no_of_fears) {
     for(let i = 0; i < no_of_fears; i++){
       let entry = {}
       for(let j = 0; j < questions.length - 1; j++) {
         if(j === 0) {
           entry["name"] = questions[j][i]
         }
         else {
           entry[j] = questions[j][i]
         }
         if(j !== 0) {
           comp_msgs.push({"question": questions[j][i], "fear": questions[0][i]});
           no_of_questions++;
           index++;
         }
       }
     }
   }
   else {
     console.log("ERROR!");
   }
   console.log(comp_msgs);
   start();
 }

 function start() {
   $('#heading').text('Fear Analyzer');
   $("#textinput").prop('disabled', false);
   $("#textinput").focus();
   if(user_comp === 1) {
     $('<div/>', {
       class: 'comp-msg',
       text: comp_msgs[i].question,
     }).appendTo('#chat_div');
     user_comp = 0;
     i++;
     let elem = document.getElementById('chat_div');
     elem.scrollTop = elem.scrollHeight;
   }
 }

 function clearResponseObject() {
   delete responses['question'];
   delete responses['answer'];
   delete responses['type'];
 }

 $('#send_button').click(() => {
   utext = $("#textinput").val();
   if(utext !== '') {
     usertext();
     $("#textinput").val("");
   }
   let elem = document.getElementById('chat_div');
   elem.scrollTop = elem.scrollHeight;
 });

 function drawChart() {
   google.charts.load('current', {packages: ['corechart', 'bar']});
   google.charts.setOnLoadCallback(drawMultSeries);
 }

 function drawMultSeries() {
      var data = google.visualization.arrayToDataTable([
        ['Fear', 'Value', { role: 'style' }],
        ['Rejection', result["level"], gold]
      ]);

      var options = {
        title: 'Population of Largest U.S. Cities',
        chartArea: {width: '50%'},
        hAxis: {
          title: 'Fear Percentage',
          minValue: 0
        },
        vAxis: {
          title: 'Fear  '
        }
      };

      var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
      chart.draw(data, options);
    }

 function usertext() {
   $('<div/>', {
     class: 'user-msg',
     text: utext
   }).appendTo('#chat_div');
   user_comp = 1;
   responses['question'] = `${comp_msgs[i-1].question}`;
   responses['answer'] = utext;
   responses['type'] = `${comp_msgs[i-1].fear}`;
   $.ajax({
     type: 'POST',
     url: '/result',
     data: responses,
   })
   .done(function(result) {
     if(Object.keys(result).length === 3) {
       clearResponseObject();
       if(result["level"] === 0) {
         displayMessage = 'Small talk'
       }
       else {
         displayMessage  = `You entered a level ${result["level"]} response`
         drawChart();
         rej_levels.push(result["level"]);
       }
       console.log(displayMessage);
     }
   });
   if(i === no_of_questions - 1) {
     $("#textinput").prop('disabled', true);
   }
   else {
     $('#heading').text('Thinking....');
     $("#textinput").prop('disabled', true);
     setTimeout(start, 1000);
   }
 }

 $(document).keypress(function(e) {
   if(e.which == 13) {
     utext = $("#textinput").val();
     if(utext !== '') {
       usertext();
       $("#textinput").val("");
     }
     let elem = document.getElementById('chat_div');
     elem.scrollTop = elem.scrollHeight;
   }
 });

 $('#textinput').on('keydown', function(event) {
   if (this.selectionStart == 0 && event.keyCode >= 65 && event.keyCode <= 90 && !(event.shiftKey) && !(event.ctrlKey) && !(event.metaKey) && !(event.altKey)) {
     let $t = $(this);
     event.preventDefault();
     let char = String.fromCharCode(event.keyCode);
     $t.val(char + $t.val().slice(this.selectionEnd));
     this.setSelectionRange(1,1);
   }
 });
});
