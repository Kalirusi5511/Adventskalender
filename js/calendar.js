const cal = document.getElementById("calendar");
const content = document.getElementById("content");

for (let i = 1; i <= 25; i++) {
  const btn = document.createElement("button");
  btn.textContent = i;
  btn.onclick = () => openDoor(i);
  cal.appendChild(btn);
}

function canOpenDoor(n) {
  const today = new Date();
  return today.getMonth() === 11 && today.getDate() >= n;
}

async function openDoor(n) {
  if (!canOpenDoor(n)) {
    alert("🎄 Dieses Türchen ist noch geschlossen!");
    return;
  }

  const res = await fetch(`doors/door${String(n).padStart(2, "0")}.html`);
  const html = await res.text();
  content.innerHTML = html;
}
