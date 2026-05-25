if (window.location.pathname === "/") {
  const rangeInput = document.getElementById("grams_input");
  const rangeOutput = document.getElementById("grams_output");

  rangeInput.addEventListener("input", () => {
    rangeOutput.value = rangeInput.value;
  });
}
