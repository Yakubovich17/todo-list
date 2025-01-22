const tasks = document.querySelectorAll(".task");

tasks.forEach((task) => {
  const editIconHTML = '<i class="fa fa-edit"></i>';
  const saveIconHTML = '<i class="fa fa-save"></i>';

  const editButton = task.querySelector(".task-edit-button");
  const title = task.querySelector(".task-title");
  const description = task.querySelector(".task-description");

  editButton.addEventListener("click", () => {
    if (editButton.classList.contains("edit-mode")) {
      const taskId = task.id.split("-").at(-1);

      sendRequest(taskId, title.innerText, description.innerText);

      editButton.innerHTML = editIconHTML;

      title.contentEditable = "false";
      description.contentEditable = "false";

      title.classList.remove("form-control", "border", "rounded");
      description.classList.remove("form-control", "border", "rounded");
      editButton.classList.remove("edit-mode");
    } else {
      editButton.innerHTML = saveIconHTML;

      title.contentEditable = "true";
      description.contentEditable = "true";

      title.classList.add("form-control", "border", "rounded");
      description.classList.add("form-control", "border", "rounded");
      editButton.classList.add("edit-mode");

      title.focus();
    }
  });
});

const sendRequest = (id, title, description) => {
  const taskData = {
    title: title,
    description: description,
  };

  fetch(`/tasks/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(taskData),
  });
};
