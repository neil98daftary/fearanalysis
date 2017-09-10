

$('document').ready(function() {
  let utext = '';
  let user_comp = 1;
  let hello_msg = "Hello!";
  let name_input = "What's your name?";
  let welcome = "Welcome! Let's get started!";
  let q1 = "Knowing yourself, if you're ever faced with a situation that requires you to explore unfamiliar territory or take up the mantle of responsibility, you're more likely to";
  let q2 = "Which of the following do you most identify with in terms of social relations?";
  let q3 = "If you are out boating with your friend and he/she falls over into the water, what will you do ";
  let q4 = "You are at the Grand Canyon and you are out on the observation deck when you peer down. You will ";
  let q5 = "You and your friend are at the amusement park and are about to enter the hedge maze when your friend decides he/she doesn't want to go in. You will ";
  let comp_msgs_order = {'0': 'hello_msg', '1': 'name_input', '2': 'welcome', '3': 'q1', '4': 'q2', '5': 'q3', '6': 'q4', '7': 'q5'};
  // let comp_msgs = {hello_msg: hello_msg, name_input: name_input, welcome: welcome, q1: q1, q2: q2, q3: q3, q4: q4, q5: q5};
  let comp_msgs = {hello_msg, name_input, welcome, q1, q2, q3, q4, q5};
  let i = 0;
  let responses = {};

  function start() {
    $('#heading').text('Fear Analyzer');
    $("#textinput").prop('disabled', false);
    $("#textinput").focus();
    if (user_comp === 1) {
      $('<div/>', {
        class: 'comp-msg',
        text: comp_msgs[`${comp_msgs_order[i]}`],
      }).appendTo('#chat_div');
      user_comp = 0;
      i++;
      if(comp_msgs[`${comp_msgs_order[i-1]}`] === welcome) {
        user_comp = 1;
        $('#heading').text('Thinking....');
        $("#textinput").prop('disabled', true);
        setTimeout(start, 2000);
      }
      var elem = document.getElementById('chat_div');
      elem.scrollTop = elem.scrollHeight;
    }
  }
  $('#send_button').click(() => {
    utext = $("#textinput").val();
    if(utext !== '') {
      usertext();
      $("#textinput").val("");
    }
    var elem = document.getElementById('chat_div');
    elem.scrollTop = elem.scrollHeight;
  });

  function usertext() {
    $('<div/>', {
      class: 'user-msg',
      text: utext
    }).appendTo('#chat_div');
    user_comp = 1;
    responses[`${comp_msgs_order[i-1]}`] = utext;
    // console.log(responses);
    if(comp_msgs[`${comp_msgs_order[i-1]}`] === q5) {
      $("#textinput").prop('disabled', true);
      $.ajax({
        type: 'POST',
        url: '/result',
        data: responses,
      })
      .done(function(result){
        alert(JSON.stringify(result))
      });
    }
    else {
      $('#heading').text('Thinking....');
      $("#textinput").prop('disabled', true);
      setTimeout(start, 2000);
    }
  }

  $(document).keypress(function(e) {
    if(e.which == 13) {
      utext = $("#textinput").val();
      if(utext !== '') {
        usertext();
        $("#textinput").val("");
      }
      var elem = document.getElementById('chat_div');
      elem.scrollTop = elem.scrollHeight;
    }
  });

  $('#textinput').on('keydown', function(event) {
    if (this.selectionStart == 0 && event.keyCode >= 65 && event.keyCode <= 90 && !(event.shiftKey) && !(event.ctrlKey) && !(event.metaKey) && !(event.altKey)) {
      var $t = $(this);
      event.preventDefault();
      var char = String.fromCharCode(event.keyCode);
      $t.val(char + $t.val().slice(this.selectionEnd));
      this.setSelectionRange(1,1);
    }
  });
  start();
});
