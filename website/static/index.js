document.addEventListener("DOMContentLoaded", function () {
  const postItems = document.querySelectorAll(".list-group-item");

  postItems.forEach(function (item) {
    item.addEventListener("click", function () {
      const postId = this.dataset.postId;
      window.location.href = `/view-post/${postId}`;
    });
  });
});
