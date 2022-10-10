(function () {
  const toastElement = document.getElementById("toast")
  const toastBody = document.getElementById("toast-body")
  // const toast = new bootstrap.Toast(toastElement, { delay: 2000 })

  htmx.on("showMessage", (e) => {
    toastBody.innerText = e.detail.value
    // toast.show();
    console.log('toast here');
    // toastElement.toast('show');
    $('.toast').toast('show');
  })
})();