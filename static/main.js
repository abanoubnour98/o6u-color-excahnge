// image preview using DOM
document.addEventListener('DOMContentLoaded', () => {
  const inputElement = document.getElementById("imageInput");
  const previewImageElement = document.getElementById("previewImage");

  inputElement.addEventListener("change", (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();

    reader.readAsDataURL(file);

    reader.onload = (e) => {
      previewImageElement.src = e.target.result;
    }
  });
});


// JavaScript code
function updateColorPreview(hexCode) {
  var colorPreview = document.getElementById("color-preview-hex");
  colorPreview.style.backgroundColor = hexCode.trim();

  if (hexCode.trim() !== "") {
      colorPreview.classList.remove("hidden");
  } else {
      colorPreview.classList.add("hidden");
  }
}


// JavaScript code
var mageInput = document.getElementById("imageInput");
var imagePreview = document.getElementById("previewImage");

imageInput.addEventListener("change", function() {
    if (imageInput.files && imageInput.files[0]) {
        var reader = new FileReader();

        reader.onload = function(e) {
            imagePreview.setAttribute("src", e.target.result);
            imagePreview.parentNode.classList.remove("hidden");
        };

        reader.readAsDataURL(imageInput.files[0]);
    } else {
        imagePreview.setAttribute("src", "");
        imagePreview.parentNode.classList.add("hidden");
    }
});
