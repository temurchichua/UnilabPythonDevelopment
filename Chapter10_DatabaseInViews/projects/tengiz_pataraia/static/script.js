const url = "https://misteraschat.herokuapp.com/chat"

const socket = io(url);

var room = 0;
var username = localStorage.getItem("username");

function addMessage(msg,received=true){
    row = document.createElement("div");
    row.className = "row no-gutters";
    col = document.createElement("div");

    if(received){
        col.className = "col-5";
    }else{
        col.className = "col-5 offset-7";
    }

    message = document.createElement("div");
    message.className = "message";
    
    message.innerHTML = msg;

    col.appendChild(message);
    row.appendChild(col);

    document.getElementById("messages").appendChild(row);
    document.getElementById("messages").scrollTop = document.getElementById("messages").scrollHeight;
}

function sendMessage(){
    var textarea = document.getElementById("textbox");
    var messageText = textarea.value;
    textarea.value = "";

    addMessage(messageText,false);

    socket.send({"text":messageText,"room":room});
}

function joinRoom(roomNumber){

    document.getElementById("messages").innerHTML = "";

    if(room != roomNumber){
        socket.emit("leave-room",room)
    }
    socket.emit("join-room",roomNumber);
    room = roomNumber;
    fetchMessages(room);
}

socket.on("message",(messageText) =>{
    addMessage(messageText); 
});

socket.on("old-messages",(data) =>{
    if(data.mine){
        addMessage(data.text,false);
    }else{
        addMessage(data.text);
    }
});

function fetchMessages(data){
    var reqUrl = `/oldMessages?room=${room}`;
    fetch(reqUrl)
    .then((response)=>{
        return response.json();
    }).then(data =>{
        data.forEach((message) =>{
            if(message.received){
                addMessage(message.text);
            }else{
                addMessage(message.text,false);
            }
        });
    });
}

window.onload = (event) => {
    joinRoom(room);
}