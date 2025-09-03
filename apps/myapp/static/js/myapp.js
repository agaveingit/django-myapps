
document.addEventListener("DOMContentLoaded", function(){
    const loading1 = document.getElementById("loading1")
    const loading2 = document.getElementById("loading2")
    const loading3 = document.getElementById("loading3")
    const loading4 = document.getElementById("loading4")
    const konversi = document.getElementById("converter")
    const submitButton = document.getElementById("submitButton")

    if (konversi) {
        konversi.addEventListener("submit", function(){
            loading1.style.display = "block";
            loading2.style.display = "block";
            loading3.style.display = "block";
            loading4.style.display = "block";
            submitButton.disabled = true;
            submitButton.innerText = "Please Wait ...";
        })
    }
})