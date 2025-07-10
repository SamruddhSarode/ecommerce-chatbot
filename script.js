const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");

function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;

  appendMessage("You", message, "user");
  userInput.value = "";

  fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: message }),
  })
    .then((res) => res.json())
    .then((data) => {
      appendMessage("Bot", data.response, "bot");
    });
}

function appendMessage(sender, message, className) {
  const msg = document.createElement("p");
  msg.innerHTML = `<strong>${sender}:</strong> ${message}`;
  msg.classList.add(className);
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}