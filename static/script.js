document.addEventListener('DOMContentLoaded', (event) => {
  let generateButton = document.querySelector('.btn-primary');
  let copyButton = document.querySelector('.btn-secondary');
  let numParagraphs = document.getElementById("numParagraphs");

  if(generateButton) {
      generateButton.addEventListener('click', generateIpsum);
  }

  if(copyButton) {
      copyButton.addEventListener('click', copyText);
  }

  if(numParagraphs) {
      numParagraphs.addEventListener('input', updateValue);
  }
});

async function generateIpsum() {
  const numParagraphs = document.getElementById("numParagraphs").value;
  const startWith = document.getElementById("startWith").checked;

  try {
    const response = await fetch(`/generate_ipsum?numParagraphs=${numParagraphs}&startWith=${startWith}`);
    const data = await response.json();

    // Save the generated text to localStorage
    localStorage.setItem('generatedText', data.text);

    // Navigate to the new page
    window.location.href = '/display_text';
  } catch (err) {
    console.error('Error generating ipsum: ', err);
  }
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

document.addEventListener('DOMContentLoaded', function() {
  const ipsumTextElement = document.getElementById('ipsumText');
  if (ipsumTextElement) {
    const generatedText = localStorage.getItem('generatedText');
    if (generatedText) {
      ipsumTextElement.innerText = generatedText;
    }
  }
});
