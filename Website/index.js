let utext = '';
let user_comp = 1;
let comp_msgs = ["Hello", "What is your name?", "Are you having a great day?"]
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
// start();
}
