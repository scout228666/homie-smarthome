/**
 * homie — auth page interactions
 * - four-box invite code: auto-advance, backspace-back, paste support
 * - password visibility toggles
 * No framework needed here; htmx handles the actual form submissions.
 */
 
 htmx.config.withCredentials = true;

(function initCodeGroup() {
  const group = document.querySelector("[data-code-group]");
  if (!group) return;

  const inputs = Array.from(group.querySelectorAll("[data-code-input]"));
  const hidden = document.getElementById("invite_code");
  const submitBtn = document.getElementById("invite-submit");

  function syncState() {
    const value = inputs.map((i) => i.value).join("");
    hidden.value = value;
    submitBtn.disabled = value.length !== inputs.length;
    inputs.forEach((i) => i.classList.toggle("is-filled", i.value !== ""));
  }

  function clearErrorState() {
    inputs.forEach((i) => i.classList.remove("is-error"));
  }

  inputs.forEach((input, index) => {
    input.addEventListener("input", (e) => {
      const digit = e.target.value.replace(/[^0-9]/g, "").slice(-1);
      e.target.value = digit;
      clearErrorState();
      if (digit && index < inputs.length - 1) {
        inputs[index + 1].focus();
      }
      syncState();
    });

    input.addEventListener("keydown", (e) => {
      if (e.key === "Backspace" && !input.value && index > 0) {
        inputs[index - 1].focus();
      }
      if (e.key === "ArrowLeft" && index > 0) {
        inputs[index - 1].focus();
      }
      if (e.key === "ArrowRight" && index < inputs.length - 1) {
        inputs[index + 1].focus();
      }
    });

    input.addEventListener("paste", (e) => {
      e.preventDefault();
      const digits = (e.clipboardData.getData("text") || "").replace(/[^0-9]/g, "").split("");
      digits.slice(0, inputs.length).forEach((d, i) => {
        inputs[i].value = d;
      });
      const nextEmpty = inputs.findIndex((i) => !i.value);
      (nextEmpty === -1 ? inputs[inputs.length - 1] : inputs[nextEmpty]).focus();
      clearErrorState();
      syncState();
    });
  });

  inputs[0].focus();

  // If the server rejects the code, it can add `.is-error` to #form-message's
  // sibling group via an out-of-band swap, or the view can render this class
  // server-side on the boxes directly on a full-page reload with `error`.
  if (group.dataset.hasError) {
    inputs.forEach((i) => i.classList.add("is-error"));
  }
})();

(function initPasswordToggles() {
  document.querySelectorAll("[data-password-toggle]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const targetId = btn.getAttribute("data-password-toggle");
      const field = document.getElementById(targetId);
      if (!field) return;
      const showing = field.type === "text";
      field.type = showing ? "password" : "text";
      btn.setAttribute("aria-label", showing ? "Показать пароль" : "Скрыть пароль");
      btn.style.color = showing ? "" : "var(--accent)";
    });
  });
})();
