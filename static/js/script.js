// static/js/script.js
document.getElementById("genForm")?.addEventListener("submit", function(e) {
    e.preventDefault();
    const formData = new FormData(document.getElementById("genForm"));
    fetch("/generate", {
      method: "POST",
      body: new URLSearchParams(formData)
    })
    .then(response => {
      const disposition = response.headers.get('Content-Disposition');
      if (disposition && disposition.indexOf('attachment') !== -1) {
        return response.blob().then(blob => {
          const url = window.URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.href = url;
          a.download = "generated_project.zip";
          document.body.appendChild(a);
          a.click();
          a.remove();
          return { message: "Project ZIP download started." };
        });
      } else {
        return response.json();
      }
    })
    .then(data => {
      document.getElementById("result").innerText = data.message || JSON.stringify(data, null, 2);
    })
    .catch(error => {
      document.getElementById("result").innerText = "Error: " + error;
    });
  });
  