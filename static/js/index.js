const _ = (e) => document.querySelector(e);
const render = _(".result");
const nothing = _(".nothing");
const downloadSection = _(".download-section");

// create video
const createVideo = (data) => {
  let v = document.createElement("video");
  v.id = "instavideo";
  v.src = data.content;
  v.controls = true;
  v.autoplay = true;
  v.classList.add("video");

  // // create info
  // let info = document.createElement("p");
  // info.textContent = "Click the right button on video and select save as.";

  render.innerHTML = "";
  render.appendChild(v);
  // render.appendChild(info);
};
// create image
const createImg = (data) => {
  // create image
  let i = document.createElement("img");
  i.id = "instaImg";
  i.src = data.content;
  i.classList.add("image");

  // create info

  render.innerHTML = "";
  render.appendChild(i);
};

const enableDownload = (data) => {
  let a = document.createElement("a");
  a.href = data.content;
  a.download = "true";
  a.target = "_blank";
  a.textContent = "Download";
  a.classList.add("download-btn");

  render.appendChild(a);
};
// extract html
const getMedia = () => {
  render.innerHTML = "<div class='image-placeholder'></div>";
  // get input value
  let url = _("input").value;
  if (url) {
    fetch(url)
      .then((r) => r.text())
      .then((r) => {
        // render html
        nothing.innerHTML = r;
        // wait, find meta and create video or image
        let w = setTimeout(() => {
          let v = _('meta[property="og:video"]');
          if (v) {
            createVideo(v);
            enableDownload(v);
            window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" });
          } else {
            let img = _('meta[property="og:image"]');
            if (img) {
              createImg(img);
              enableDownload(img);
              window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" });
            } else {
              alert("The entered url is invalid please recheck");
            }
          }
          clearTimeout(w);
        }, 200);
      });
  } else {
    _("input").setAttribute(
      "placeholder",
      "Invalid address, use a proper Insagram link"
    );
  }
};