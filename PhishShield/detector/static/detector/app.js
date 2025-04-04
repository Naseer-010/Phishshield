function updateSemiMeter() {
  event.preventDefault(); 

  const urlInput = document.getElementById('urlInput');
  const valueText = document.getElementById('semi-value');
  const fill = document.getElementById('semi-fill');
  
  
  const resultBox = document.querySelector('.result');

  const url = urlInput.value.trim();

  if (url === "") {
      
      resultBox.style.display = 'none';
      alert("Please enter a URL.");
      return;
  }

  
  resultBox.style.display = 'block';


  const p = Math.floor(Math.random() * 101);
  const percentage = 100-p; 

  const rotation = (percentage / 100) * 180;
  fill.style.transform = `rotate(${rotation}deg)`;
  valueText.textContent = `${percentage}%`;


  
}


function handleContactForm(event) {
  event.preventDefault();
  
  const name = document.getElementById('contactName').value.trim();
  const email = document.getElementById('contactEmail').value.trim();
  const message = document.getElementById('contactMessage').value.trim();

  if (!name || !email || !message) {
      showAlert("⚠️ Please fill in all fields.");
      return;
  }

  
  console.log("Message Sent:", { name, email, message });
  showAlert("✅ Message sent successfully!");
  
  
  document.querySelector(".contact-form").reset();
}
