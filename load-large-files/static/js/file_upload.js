const uploadButton = document.getElementById('upload-button');
const fileInput = document.getElementById('file-input');

uploadButton.addEventListener('click', () => {
const file = fileInput.files[0];
const url = '/upload';
const formData = new FormData();
formData.append('file', file);

fetch(url, {
  method: 'POST',
  body: formData
})
.then(response => {
  console.log('File uploaded successfully');
})
.catch(error => {
  console.error(error);
});
});