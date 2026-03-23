document.addEventListener('DOMContentLoaded', function () {
  const hello = this.querySelector('#hello');

  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      hello.textContent = data.hello;
    });
});
