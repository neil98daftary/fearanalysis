let utext = '';
let user_comp = 1;
let hello_msg = "Hello!";
let name_input_message = "What's your name?";
let welcome_message = "Welcome! Let's get started! ";
let q1 = "Knowing yourself, if you're ever faced with a situation that requires you to explore unfamiliar territory or take up the mantle of responsibility, you're more likely to";
let q2 = "Which of the following do you most identify with in terms of social relations?";
let q3 = "If you are out boating with your friend and he/she falls over into the water, what will you do ";
let q4 = "You are at the Grand Canyon and you are out on the observation deck when you peer down. You will ";
let q5 = "You and your friend are at the amusement park and are about to enter the hedge maze when your friend decides he/she doesn't want to go in. You will ";
let comp_msgs = [hello_msg, name_input_message, welcome_message + q1, q2, q3, q4, q5];
let i=0;

function start() {
  if (user_comp==1) {
    $('<div/>', {
      class: 'comp-msg',
      text: comp_msgs[i]
  }).appendTo('#chat_column');
  user_comp=0;
  i++;
  }
}

function send() {
  console.log("Send was pressed");
  utext = $("#textinput").val();
  usertext();
  $("#textinput").val("");
}


function usertext() {
  console.log("User text was sent");
  $('<div/>', {
    class: 'user-msg',
    text: utext
  }).appendTo('#chat_column');
  user_comp=1;
  setTimeout(start, 2000);
}

$('document').ready(function() {

  $('.ui.sticky').sticky({
    offset       : 50,
    bottomOffset : 50,
    context: '.ui.grid'
  });

});
