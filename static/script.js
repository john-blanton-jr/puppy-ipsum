async function generateIpsum() {
  const numParagraphs = document.getElementById("numParagraphs").value;
  const startWith = document.getElementById("startWith").checked;

  fetch(`/generate_ipsum?numParagraphs=${numParagraphs}&startWith=${startWith}`)
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("ipsumText").innerText = data.text;
    });
}

async function copyText() {
  const textToCopy = document.getElementById("ipsumText").innerText;
  try {
      await navigator.clipboard.writeText(textToCopy);
      console.log('Text copied to clipboard');
  } catch (err) {
      console.error('Error copying text: ', err);
  }
}

function updateValue() {
  document.getElementById("rangeValue").textContent =
    document.getElementById("numParagraphs").value;
}

document.getElementById("generateButton").addEventListener('click', generateIpsum);
document.getElementById("copyButton").addEventListener('click', copyText);
document.getElementById("numParagraphs").addEventListener('input', updateValue);
