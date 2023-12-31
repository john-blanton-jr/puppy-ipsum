document.addEventListener('DOMContentLoaded', (event) => {
  let generateButton = document.querySelector('.btn-primary');
  let copyButton = document.querySelector('.btn-success'); 
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

    localStorage.setItem('generatedText', data.text);

    window.location.href = '/display_text';
  } catch (err) {
    console.error('Error generating ipsum: ', err);
  } finally {
    const numParagraphsElement = document.getElementById("numParagraphs");
    const rangeValueElement = document.getElementById("rangeValue");
    if (numParagraphsElement && rangeValueElement) {
      numParagraphsElement.value = '1';
      rangeValueElement.textContent = '1';
    }
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

document.addEventListener('DOMContentLoaded', (event) => {
  const numParagraphsElement = document.getElementById('numParagraphs');
  if (numParagraphsElement) {
      numParagraphsElement.value = '1';
  }
});

window.onload = function() {
  getPuppyImage();
};

function getPuppyImage() {
  fetch('/get_puppy_image')
  .then(response => response.json())
  .then(data => {
    if(data && data.photos && data.photos.length > 0) {
      const randomIndex = Math.floor(Math.random() * data.photos.length);
      const selectedPhoto = data.photos[randomIndex];
      const imgSrc = selectedPhoto.src.medium;
      const photographerName = selectedPhoto.photographer;
      const photoPageUrl = selectedPhoto.url;

      const puppyImageElement = document.getElementById('puppyImage');
      const photographerCreditElement = document.getElementById('photographerCredit');

      if (puppyImageElement && photographerCreditElement) {
        puppyImageElement.src = imgSrc;
        photographerCreditElement.innerHTML = `Photo by <a href="${photoPageUrl}" target="_blank">${photographerName}</a> on <a href="https://www.pexels.com" target="_blank">Pexels</a>`;
      } else {
        console.log('Element with ID "puppyImage" or "photographerCredit" is not on this page, skipping...');
      }
    } else {
      console.error('No photos available or error in API response');
    }
  })
  .catch(error => {
    console.error('Error fetching photo:', error);
  });
}

